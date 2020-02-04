import abc

class Konfiguracja:
    def __init__(self,type = "niska"):
        self.type = type
    def sterownik(self):
        if (self.type == "niska"):
            return Fabryka_nis_roz()
        else:
            return Fabryka_wys_roz()

class Ap_nadzorujaca:
    def __init__(self, konfig = Konfiguracja()):
        self.fabryka = Fabryka_ster(konfig.sterownik())
        self.ster_ekran = self.fabryka.pobierz_ster_ekran()
        self.ster_druk =  self.fabryka.pobierz_ster_druk()
    def rysuj(self):
        self.ster_ekran.rysuj()
    def drukuj(self):
        self.ster_druk.drukuj()

class Fabryka_ster:
    def __init__(self, fabryka):
        self.fabryka = fabryka
    def pobierz_ster_ekran(self):
        return self.fabryka.pobierz_ster_ekran()
    def pobierz_ster_druk(self):
        return self.fabryka.pobierz_ster_druk()

class Fabryka_nis_roz(Fabryka_ster):
    def __init__(self):
        pass
    def pobierz_ster_ekran(self):
        return  Sterownik_Ekranu_Nis_Roz()
    def pobierz_ster_druk(self):
        return  Sterownik_Drukarki_Nis_Roz()

class Fabryka_wys_roz(Fabryka_ster):
    def __init__(self):
        pass
    def pobierz_ster_ekran(self):
        return Sterownik_Ekranu_Wys_Roz()
    def pobierz_ster_druk(self):
        return Sterownik_Drukarki_Wys_Roz()


class Sterownik_Ekranu(abc.ABC):
    @abc.abstractmethod
    def rysuj(self):
        pass
class Sterownik_Drukarki(abc.ABC):
    @abc.abstractmethod
    def drukuj(self):
        pass

class Sterownik_Ekranu_Nis_Roz(Sterownik_Ekranu):
    def rysuj(self):
        SENR.rysuj()

class Sterownik_Ekranu_Wys_Roz(Sterownik_Ekranu):
    def rysuj(self):
        SEWR.rysuj()

class Sterownik_Drukarki_Nis_Roz(Sterownik_Drukarki):
    def drukuj(self):
        SENR.drukuj()

class Sterownik_Drukarki_Wys_Roz(Sterownik_Drukarki):
    def drukuj(self):
        SEWR.drukuj()

class SENR:
    @staticmethod
    def rysuj():
        print("rysuje niska rozdzielczoc")
    @staticmethod
    def drukuj():
        print("drukuje niska rozdzielczoc")

class SEWR:
    @staticmethod
    def rysuj():
        print("rysuje WYSOKA rozdzielczoc")
    @staticmethod
    def drukuj():
        print("drukuje WYSOKA rozdzielczoc")

if __name__ == "__main__":
    #print("hello word")
    niskaRoz = Ap_nadzorujaca()
    niskaRoz.rysuj()
    niskaRoz.drukuj()
    print("-------------")
    wysokaRoz = Ap_nadzorujaca(Konfiguracja("wysoka"))
    wysokaRoz.rysuj()
    wysokaRoz.drukuj()