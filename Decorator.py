def dekorator_naglowek_1(lista):
    '''prosty dekorator w sytuacji gdy mamy kilka nagłówków'''
    if len(lista[0]) > 1:
        naglowek = lista[0]
        potwierdzenie = lista[1]
        stopka = lista[2]
        data = []
        for x in naglowek:
            data.append(x)
        data.append(potwierdzenie)
        data.append(stopka)
        return data
    else:
        return lista
def dekorator_naglowek_2(lista):
    '''nagloweki z dopiskiem xD gdy jest ich kilka'''
    if len(lista[0]) > 1:
        naglowek = lista[0]
        potwierdzenie = lista[1]
        stopka = lista[2]
        data = []
        for x in naglowek:
            data.append(x + "xD")
        data.append(potwierdzenie)
        data.append(stopka)
        return data
    else:
        return lista

def dekorator_stopka_1(lista):
    '''prosty dekorator w sytuacji gdy mamy kilka stopek'''
    if len(lista[2]) > 1:
        naglowek = lista[0]
        potwierdzenie = lista[1]
        stopka = lista[2]
        data = []
        data.append(naglowek)
        data.append(potwierdzenie)
        for x in stopka:
            data.append(x)
        return data
    else:
        return lista

def dekorator_stopka_2(lista):
    '''stopki z dopiskiem :( gdy jest ich kilka'''
    if len(lista[2]) > 1:
        naglowek = lista[0]
        potwierdzenie = lista[1]
        stopka = lista[2]
        data = []
        data.append(naglowek)
        data.append(potwierdzenie)
        for x in stopka:
            data.append(x+":(")
        return data
    else:
        return lista


class Konfiguracja_Potwierdzenia:
    def __init__(self, naglowek, potwierdzenie, stopka):
        self.dane_naglowek = naglowek
        self.dane_potwierdzenie = potwierdzenie
        self.dane_stopka = stopka
    def pobierz_potwierdzenie(self):
        return [self.dane_naglowek, self.dane_potwierdzenie, self.dane_stopka]

class Zamówienie:
    def __init__(self,naglowek,potwierdzenie,stopka):
        self.potwierdzenie = Konfiguracja_Potwierdzenia(naglowek,potwierdzenie,stopka)

    def drukuj(self,type = dekorator_naglowek_1):
        data = type(self.potwierdzenie.pobierz_potwierdzenie())
        for x in data:
            print(x)

if __name__ == "__main__":
    #print("hello word")
    zam1 = Zamówienie(["Naglowek 1","Naglowek 2"], "Potwierdzenie 1", "Stopka 1")
    zam1.drukuj()
    print("------")
    zam2 = Zamówienie("Naglowek 1", "Potwierdzenie 1", ["Stopka 1","Stopka 2"])
    zam2.drukuj(dekorator_stopka_1)
    print("------")
    zam3 = Zamówienie("Naglowek 1", "Potwierdzenie 1", ["Stopka 1", "Stopka 2"])
    zam3.drukuj(dekorator_stopka_2)
