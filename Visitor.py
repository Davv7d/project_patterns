import abc
class animal(abc.ABC):
    def __init__(self, name, typ, illness, price ):
        pass
    @abc.abstractmethod
    def visitor(self,visitor):
        pass

class Mammal(animal):
    #ssaki
    def __init__(self, name, typ, illness, price ):
        self.name = name
        self.type = typ
        self.illness = illness
        self.price = price
    def visitor(self,visitor):
        self.visit = visitor.add_animall(self)

class Birds(animal):
    #ptaki
    def __init__(self, name, typ, illness, price, pbm ):
        self.name = name
        self.type = typ
        self.illness = illness
        self.price = price
        self.price_black_market = pbm
    def visitor(self,visitor):
        self.visit = visitor.add_animall(self)

class Reptiles(animal):
    #gady
    def __init__(self, name, typ, illness, price ):
        self.name = name
        self.type = typ
        self.illness = illness
        self.price = price
    def visitor(self,visitor):
        self.visit = visitor.add_animall(self)

class Fishes(animal):
    #ryby
    def __init__(self, name, typ, illness, price ):
        self.name = name
        self.type = typ
        self.illness = illness
        self.price = price
    def visitor(self,visitor):
        self.visit = visitor.add_animall(self)

class Visitor_price_oficial:
    def __init__(self):
        self.__sum_price = 0
        self.__animals_in_shop = set()
    def add_animall(self,animal):
        self.__sum_price += animal.price
        self.__animals_in_shop.add(animal.name)
    def get_sum_price(self):
        print("sume price oficial: ",self.__sum_price)
    def get_all_animals_in_shope(self):
        print(self.__animals_in_shop)

class Visitor_price_real:
    def __init__(self):
        self.__sum_price = 0
    def add_animall(self,animal):
        try:
            if animal.price_black_market is not None:
                self.__sum_price += animal.price_black_market
            else:
                self.__sum_price += animal.price
        except:
            self.__sum_price += animal.price
    def get_sum_price(self):
        print("sume price real: ",self.__sum_price)

class Visitor_illnes:
    def __init__(self):
        self.animals = []
    def add_animall(self,animal):
        if animal.illness:
            self.animals.append(animal)
    def get_treatment(self):
        for animal in self.animals:
            try:
                if animal.price_black_market >= animal.price*2:
                    print("Animal: {} will receive expensive and exclusive treatment".format(animal.name))
                else:
                    print("Animal: {} will receive Poor  treatment, with antibiotic and diet".format(animal.name))
            except:
                print("Animal: {} will receive Poor  treatment, with antibiotic".format(animal.name))




if __name__ == "__main__":
    #print("hello word")
    visitor1 = Visitor_price_oficial()
    visitor2 = Visitor_price_real()
    visitor3 = Visitor_illnes()
    animal1 = Mammal("Tiger", "Mammal", False,10000)
    animal1.visitor(visitor1)
    animal1.visitor(visitor2)
    animal1.visitor(visitor3)
    animal2 = Mammal("Elephant", "Mammal", True, 20000)
    animal2.visitor(visitor1)
    animal2.visitor(visitor2)
    animal2.visitor(visitor3)

    animal3 = Birds("Nightingale", "Birds", True, 2040, 12030)
    animal3.visitor(visitor1)
    animal3.visitor(visitor2)
    animal3.visitor(visitor3)
    animal4 = Birds("Parrot", "Birds", True, 3000, 2000)
    animal4.visitor(visitor1)
    animal4.visitor(visitor2)
    animal4.visitor(visitor3)



    visitor1.get_all_animals_in_shope()
    visitor1.get_sum_price()
    visitor2.get_sum_price()
    visitor3.get_treatment()