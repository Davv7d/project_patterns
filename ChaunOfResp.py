import  abc
class ahelp(abc.ABC):
    @abc.abstractmethod
    def handle_help(self):
        pass
    @abc.abstractmethod
    def show_help(self):
        pass

class A_Print_button(ahelp):
    def handle_help(self):
        print("aPrintButton: wyświetlam pomoc")
    def show_help(self):
        pass

class An_Ok_Button(ahelp):
    def handle_help(self):
        print("anOKButton: wyświetlam pomoc")
    def show_help(self):
        pass

class A_Save_Dialog(ahelp):
    def handle_help(self):
        print("aSaveDialog: wyświetlam pomoc")
    def show_help(self):
        pass

class A_Print_Dialog(ahelp):
    def handle_help(self):
        print("aPrintDialog: wyświetlam pomoc")
    def show_help(self, x):
        if x == 2:
            self.handle_help()
        else:
            print("aPrintDialog: nie może obsłużyć problemu przekazuje dalej")
            if(x == 3):
                aprint = A_Print_button()
                aprint.handle_help()
            elif(x == 4):
                anOK = An_Ok_Button()
                anOK.handle_help()

class An_Aplication(ahelp):
    def handle_help(self):
        print("anAplication: wyświetlam pomoc")
    def show_help(self,x = 0):
        if x == 0:
            self.handle_help()
        else:
            print("anAplication: nie może obsłużyć problemu przekazuje dalej")
            if x == 1:
                asave = A_Save_Dialog()
                asave.handle_help()
            else:
                aprint = A_Print_Dialog()
                aprint.show_help(x)

class Konfig_help:
    @staticmethod
    def show_help(typ):
        if typ == 0:
            apk = An_Aplication()
            apk.handle_help()
        else:
            if typ == 1:
                apk = A_Save_Dialog()
                apk.handle_help()
            else:
                if typ == 2:
                    apk = A_Print_Dialog()
                    apk.handle_help()
                else:
                    if typ == 3:
                        apk = A_Print_button()
                        apk.handle_help()
                    elif typ == 4:
                        apk = An_Ok_Button()
                        apk.handle_help()
                    else:
                        print("not suported")


if __name__ == "__main__":
    print("hello word")
    aplication = An_Aplication()
    aplication.show_help(0)
    print("---")
    aplication.show_help(1)
    print("---")
    aplication.show_help(2)
    print("---")
    aplication.show_help(3)
    print("---")
    aplication.show_help(4)
    print("---")
    ## Z wykorzystaniem konfiga
    print("----------------------------------")
    Konfig_help.show_help(1)
    Konfig_help.show_help(2)
    Konfig_help.show_help(3)
    Konfig_help.show_help(4)
    Konfig_help.show_help(5)