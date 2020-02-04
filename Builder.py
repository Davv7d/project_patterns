class RTF_Reader:
    __builder = None
    def __init__(self, html = " "):
        self.html = html
    def set_builder(self, builder):
        self.__builder = builder
        self.__builder.set_list(self.html)
    def parse_RTF(self, typ):
        if typ == 1:
            return self.__builder.convert_character()
        elif typ == 2:
            return self.__builder.convert_font_change()
        elif typ == 3:
            return self.__builder.convert_style()

class Buildger:
    def __init__(self, html = ""):
        self.html = html
        self.list = html_to_list.parse(html)
        self.text = ""
    def set_list(self,html):
        self.html = html
        self.list = html_to_list.parse(html)
        # print(self.list)
    def convert_character(self):
        pass
    def convert_font_change(self):
        pass
    def convert_paragraph(self):
        pass

class ASCIII_Converter(Buildger):
    def convert_character(self):
        self.text = ASCII_text.parse(self.list)
    def get_ASCIII_text(self):
        return self.text

class TeX_Converter(Buildger):
    def convert_character(self):
        self.convert_font_change()
        # print(self.list,self.text)
        self.text = ASCII_text.parse(self.text)
    def convert_font_change(self):
        self.text = TeX_text.parse(self.list)
    def get_ASCIII_text(self):
        return self.text

class Text_Widget_Converter(Buildger):
    def convert_character(self):
        self.text = Text_widget.parse(self.list)
    def get_ASCIII_text(self):
        return self.text

class Text_converter(Buildger):
    '''Concrete builder'''
    def convert_character(self):
        asii = ASCIII_Converter(self.html)
        asii.convert_character()
        return asii.get_ASCIII_text()
    def convert_font_change(self):
        Tex = TeX_Converter(self.html)
        Tex.convert_font_change()
        Tex.convert_character()
        return Tex.get_ASCIII_text()
    def convert_style(self):
        widg = Text_Widget_Converter(self.html)
        widg.convert_character()
        return  widg.get_ASCIII_text()

class html_to_list:
    '''zamieniam ciąg znaków html na liste w której znajdują kolejno elementy na:
    [][0] - <
    [][1] - >
    [][2] - /
    [][3] - znak w html
    [][4] - normalny znak
    '''
    @staticmethod
    def parse(html):
        list = []
        isHtml = False
        for x in html:
            if (x == "<"):
                list.append([x,0])
                isHtml = True
            elif (x == "/"):
                list.append([x,2])
            elif (x == ">"):
                list.append([x, 1])
                isHtml = False
            else:
                if isHtml:
                    list.append([x,3])
                else:
                    list.append([x,4])
        return list

class ASCII_text:
    @staticmethod
    def parse(html_parsed):
        asii = ""
        for xy in html_parsed:
            if xy[1] == 4:
                asii += xy[0]
        return asii

class TeX_text:
    @staticmethod
    def parse(html_parsed):
        tab = html_parsed
        pomiedzy_znakami_html = False
        i=0
        for xy in html_parsed:
            if xy[1] == 0:
                pomiedzy_znakami_html = True
            elif xy[1] == 2:
                pomiedzy_znakami_html = False
            elif pomiedzy_znakami_html == True:
                if xy[1] == 4:
                    tab[i][0] = xy[0].upper()
            i += 1
        return tab

class Text_widget:
    @staticmethod
    def parse(html_parsed):
        pomiedzy_znakami_html = False
        i = 0
        text = ""
        for xy in html_parsed:
            if xy[1] == 0:
                if pomiedzy_znakami_html == False:
                    pomiedzy_znakami_html = True
                else:
                    pomiedzy_znakami_html = False
            elif pomiedzy_znakami_html == True:
                if xy[1] == 3:
                    text +=  str("{" + xy[0] + "#")
                if xy[1] == 4:
                    text += str(xy[0]+"}")
            else:
                if xy[1] == 4:
                    text += xy[0]
            i += 1
        return text

if __name__ == "__main__":
    #print("hello word")
    html = "A<b>l</b>a ma <i>k</i>o<u>t</u>a"
    # print(list(html))
    #print(ASCII_text.parse(html_to_list.parse(html)))
    # print(html_to_list.parse(html))
    #print( ASCII_text.parse( TeX_text.parse( html_to_list.parse(html) ) ) )
    #print(Text_widget.parse(html_to_list.parse(html)))
    print("-------")
    builder = Text_converter()
    obj1 = RTF_Reader(html)
    obj1.set_builder(builder)
    print(obj1.parse_RTF(1))
    print(obj1.parse_RTF(2))
    print(obj1.parse_RTF(3))