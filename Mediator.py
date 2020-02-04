class Zaliczenie:
    def __init__(self):
        pass
    def get_zaliczenie(self):
        pass
    def set_zaliczenie(self,zal):
        pass

class Cwiczenia(Zaliczenie):
    def __init__(self, mediator):
        self.__zaliczenie = False
        self.mediator = mediator
    def get_zaliczenie(self):
        return self.__zaliczenie
    def set_zaliczenie(self, zal):
        self.__zaliczenie = zal
        self.mediator.stan_zaliczen[0] = True

class Wyklad(Zaliczenie):
    def __init__(self, mediator):
        self.__zaliczenie = False
        self.mediator = mediator
    def get_zaliczenie(self):
        return self.__zaliczenie
    def set_zaliczenie(self,zal):
        if zal:
            self.__zaliczenie = zal
            self.mediator.cwiczenia.set_zaliczenie(True)
            self.mediator.stan_zaliczen[1] = True

class Konkurs(Zaliczenie):
    def __init__(self, mediator):
        self.__zaliczenie = False
        self.mediator = mediator
    def get_zaliczenie(self):
        return self.__zaliczenie
    def set_zaliczenie(self, zal):
        if zal:
            self.__zaliczenie = zal
            self.mediator.wyklad.set_zaliczenie(True)
            self.mediator.stan_zaliczen[2] = True



class Mediator:
    def __init__(self):
        self.cwiczenia = Cwiczenia(self)
        self.wyklad = Wyklad(self)
        self.konkurs = Konkurs(self)
        self.stan_zaliczen = [False, False, False]
    def menu(self):
        while(True):
            x = ["", "", ""]
            for i in range(3):
                if self.stan_zaliczen[i]:
                    x[i] = "X"
                else:
                    x[i] = ""
            print("1.Ćwiczenia zaliczone. ", x[0])
            print("2. Wykład (egzamin) zaliczony. ", x[1])
            print("3. Przedmiot zaliczony (wygrany konkurs). ", x[2])
            print("4. Wyjście z programu. \n")
            decyzja = input()
            print(decyzja)
            if decyzja == "1":
                self.cwiczenia.set_zaliczenie(True)
            elif decyzja == "2":
                self.wyklad.set_zaliczenie(True)
            elif decyzja == "3":
                self.konkurs.set_zaliczenie(True)
            elif decyzja == "4":
                return False
            else:
                print("złe dane wejsciowe")


if __name__ == "__main__":
    print("hello word")
    mediator = Mediator()
    mediator.menu()