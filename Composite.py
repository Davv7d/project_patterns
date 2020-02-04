class Graphic:
    def draw(self):
        pass
    def add(self,graphic):
        pass
    def remove(self,graphic):
        pass
    def get_child(self,id):
        pass

class Line(Graphic):
    def draw(self):
        print("Line")

class Rectangle(Graphic):
    def draw(self):
        print("Rectangle")

class Text(Graphic):
    def draw(self):
        print("Text")

class Picture(Graphic):
    def __init__(self):
        self.graphic = []
    def draw(self):
        for g in self.graphic:
            print(g)
    def add(self,graphic):
        for g in graphic:
            self.graphic.append(g)
    def get_child(self,id):
        if ( id < len(self.graphic)):
            print(self.graphic[id])
        else:
            print("index out of rage")

if __name__ == "__main__":
    #print("hello word")
    aLine = Line()
    aLine.draw()
    aRectangle = Rectangle()
    aRectangle.draw()
    print("------------")
    aPicture = Picture()
    aPicture.add(["aText","aLine","aRectangle"])
    aPicture.draw()
    print("------------")
    aLine.draw()