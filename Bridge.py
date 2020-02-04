class BG1:
    @staticmethod
    def rysuj_linie():
        print("rysuje linie BG1")
    @staticmethod
    def rysuj_okrag():
        print("rysuje okrag BG1")

class BG2:
    @staticmethod
    def rysuj_linie():
        print("rysuje linie BG2")
    @staticmethod
    def rysuj_okrag():
        print("rysuje okrag BG2")

class BibliotekaV1:
    def rysuj_linie(self):
        BG1.rysuj_linie()
    def rysuj_okrag(self):
        BG1.rysuj_okrag()

class BibliotekaV2:
    def rysuj_linie(self):
        BG2.rysuj_linie()
    def rysuj_okrag(self):
        BG2.rysuj_okrag()

class Biblioteka:
    def __init__(self, typ = BibliotekaV1()):
        self.typ = typ
    def rysuj_linie(self):
        self.typ.rysuj_linie()
    def rysuj_okrag(self):
        self.typ.rysuj_okrag()

class Figura:
    def __init__(self, typ_biblioteki):
        self.biblioteka = typ_biblioteki
    def rysuj_linie(self):
        self.biblioteka.rysuj_linie()
    def rysuj_okrag(self):
        self.biblioteka.rysuj_okrag()

class Prostokat(Figura):
    def __init__(self, typ_biblioteki = BibliotekaV1()):
        super().__init__(typ_biblioteki)
    def rysuj(self):
        super().rysuj_linie()
        super().rysuj_linie()
        super().rysuj_linie()
        super().rysuj_linie()

class Okrag(Figura):
    def __init__(self, typ_biblioteki = BibliotekaV1()):
        super().__init__(typ_biblioteki)
    def rysuj(self):
        super().rysuj_okrag()

if __name__ == "__main__":
    # print("hello word")
    okrag = Okrag(BibliotekaV2())
    prostokat = Prostokat()
    okrag.rysuj()
    print("---")
    prostokat.rysuj()