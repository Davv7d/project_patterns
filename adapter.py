class Figure():
    def __init__(self):
        pass
    def get_area(self):
        pass
    def add_area(self):
        pass
    def display(self):
        print("-_-")
    def fill(self):
        pass
    def add_colour(self):
        print("collor added")
    def remove(self):
        pass

class Square(Figure):
    def __init__(self):
        super().__init__()
        pass
    def display(self):
        print("draws a square")

class Circle(Figure):
    def __init__(self, xxCircle = None):
        super().__init__()
        self.xxCircle = xxCircle
    def display(self):
        print("draws a Circle  O")
        if(self.xxCircle != None):
            self.xxCircle.displayy()
class XXCircle:
    def __init__(self):
        pass
    def displayy(self):
        print("draw xxx circle  xxO")

obj1 = Figure()
obj1.display()
obj2 = Square()
obj2.display()
obj3 = Circle()
obj3.display()
obj4 = XXCircle()
obj4.displayy()
print("---")
obj3  = Circle(obj4)
obj3.display()