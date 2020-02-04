import math
class Rownanie_kwadratowe:
    def __init__(self, a, b, c):
        self.delta = self.delta_func(a, b, c)
        self.ilosc_pierwiastkow = self.ilosc_pierwiastkow_func(a,b,c)

    def delta_func(self, a, b, c):
        return (b*b - 4*a*c)

    def ilosc_pierwiastkow_func(self,a,b,c):
        if self.delta >0:
            self.x1 = ( (-b - math.sqrt(self.delta) ) / (2*a) )
            self.x2 = ( (-b + math.sqrt(self.delta) ) / (2*a) )
            return 2
        elif self.delta == 0:
            self.x1 = ( (-b) / (2*a) )
            return 1
        else:
            print("Równanie kwadratowe nie ma pierwiastków dla podanych parametrów")

    def pierwiastki_rownania(self):
        if self.ilosc_pierwiastkow == 2:
            return {"x1":self.x1,
                    "x2":self.x2}
        elif self.ilosc_pierwiastkow == 1:
            return {"x1":self.x1}
        else:
            return {"delta":"< 0"}


class Licz_rownanie_kwadratowe:
    '''Proxy class'''
    def __init__(self):
        self.znane_pierwiastki = {}

    def licz(self,a,b,c):
        if(0):
            return self.znane_pierwiastki[a,b,c]
        else:
            wynik = Rownanie_kwadratowe(a,b,c)
            self.znane_pierwiastki[a,b,c] = wynik.pierwiastki_rownania()
            return self.znane_pierwiastki[a,b,c]

if __name__ == "__main__":
    #print("hello word")
    Licz_funkcje_kwadratowa = Licz_rownanie_kwadratowe()
    k1 = Licz_funkcje_kwadratowa.licz(1, 5, 6)
    k2 = Licz_funkcje_kwadratowa.licz(2, 5, 6)
    k3 = Licz_funkcje_kwadratowa.licz(1, 2, 1)
    print(k1)
    print(k2)
    print(k3)