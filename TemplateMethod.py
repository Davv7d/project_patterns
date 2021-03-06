import  abc

class Szablon_zapytania:
    def wykonaj_zapytanie(self,nazwa_BD,specZapyt):
        self.komenda_DB = self.formatuj_connect(nazwa_BD)
        self.komenda_BD = self.formatuj_select(specZapyt)

    @abc.abstractmethod
    def formatuj_connect(self, nazwa_bd):
        pass
    @abc.abstractmethod
    def formatuj_select(self, specZapyt):
        pass

class Zapytanie_SQL_Server(Szablon_zapytania):

    def formatuj_connect(self,nazwa_bd):
        print(nazwa_bd)
        return nazwa_bd

    def formatuj_select(self, specZapyt):
        print(specZapyt)
        return specZapyt

class Zapytanie_Oracle(Szablon_zapytania):

    def formatuj_connect(self,nazwa_bd):
        nazwa_bd += ";"
        print(nazwa_bd)
        return nazwa_bd

    def formatuj_select(self, specZapyt):
        specZapyt += ";"
        print(specZapyt)
        return specZapyt


if __name__ == "__main__":
    # print("hello word")
    zap1 = Zapytanie_SQL_Server()
    zap1.wykonaj_zapytanie("select *from database","connect to database")
    print("----")
    zap2 = Zapytanie_Oracle()
    zap2.wykonaj_zapytanie("select *from database", "connect to database")