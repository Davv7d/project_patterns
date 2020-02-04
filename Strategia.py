class Konfiguracja:
    '''klasa decydujaca którą metode do obliczen wykorzystac '''
    def __init__(self, parametr):
        self.parametr = parametr
    def jak_liczyc(self):
        if(self.parametr == 1):
            return Podatek_Polska()
        else:
            return Podatek_Niemcy()

class Zamowienie:
    '''glowna klasa zawierajaca dane, funkcje i inne odniesienia do innych klass niezbędne do dokonania zamowienia '''
    def __init__(self, klient, ceny, konfiguracja):
        self.klient = klient
        # self.towar = towar
        self.cena = sum(ceny)
        self.konfiguracja = konfiguracja
        self.podatek = self.oblicz_podatek()
    def oblicz_podatek(self):
        return self.konfiguracja.kwota_podatku()

    def __str__(self):
        return " Cena towaru wynosi: {} + podatek w wyskosci {}".format(self.cena,self.podatek)
class Klient:
    '''Dane indywidualne klienta'''
    def __init__(self, imie, nazwisko, adres):
        self.imie = imie
        self.nazwisko = nazwisko
        self.adres = adres

class Oblicz_podatek:
    '''Ogólna postać klassy do liczenia podatku'''
    def __init__(self, cena = 0, metoda = 0, artykul = "wc", ilosc = 2):
        self.artykul = artykul
        self.ilosc = ilosc
        self.cena = cena
        self._metoda = metoda

class Podatek_Polska(Oblicz_podatek):
    '''Obliczanie podatku w Polsce (1zł od każdej transakcji)'''
    def __init__(self):
        super().__init__()
    def kwota_podatku(self):
        return 1

class Podatek_Niemcy(Oblicz_podatek):
    '''Obliczanie podatku w Niemczech (100euro od każdej transakcji)'''
    def __init__(self):
        super().__init__()
    def kwota_podatku(self):
        return 100

if __name__ == "__main__":
    # print("hello word")
    konfiguracja1 = Konfiguracja(1)
    konfiguracja2 = Konfiguracja(2)
    klient1 = Klient("Zdziś","Zdzisiowski","Daleko 123")
    zamowienie1 = Zamowienie(klient1, [3,2.54,5.32], konfiguracja1.jak_liczyc())
    print(zamowienie1)

    klient1 = Klient("Zdziś", "Zdzisiowski", "Daleko 123")
    zamowienie2 = Zamowienie(klient1, [3, 2.54, 5.32], konfiguracja2.jak_liczyc())
    print(zamowienie2)