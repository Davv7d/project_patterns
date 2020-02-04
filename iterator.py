class Collection:
    def __init__(self,list = []):
        self.list_main = list
        self.list_interator_full = None
        self.list_interator_no_zero = None
        self.update()
    def add(self,value):
        self.list_main.append(value)
        print("new value ({}) added at the end of the list".format(value))
        self.update()
    def remove(self,index):
        removed_item = self.list_main[index]
        self.list_main.remove(index)
        print("You delate ([{}] = {}) from list".format(index,removed_item))
        self.update()
    def __str__(self):
        return str(self.list_main)
    def update(self):
        self.list_interator_full = Iterator_full(self.list_main)
        self.list_interator_no_zero = Iterator_no_zero(self.list_main)

class Iterator_full:
    def __init__(self,list):
        self.index_current = 0
        self.index_last = (len(list) -1)
        self.list_iter =list
    def first(self):
        self.index_current = 0
        return self.list_iter[0]
    def next(self):
        if (self.index_current < self.index_last):
            self.index_current += 1
            return self.list_iter[self.index_current]
        else:
            return self.is_done()
    def is_done(self):
        print("there are no more items")
        return None
    def current_item(self):
        return self.list_iter[self.index_current]
    def previous(self):
        if (self.index_current > 0):
            self.index_current -= 1
            return self.list_iter[self.index_current]
        else:
            return self.is_done()

class Iterator_no_zero:
    def __init__(self,list):
        self.index_current = 0
        self.index_last = (len(list) - 1)
        self.list_iter = list
    def first(self):
        self.index_current = 0
        return self.list_iter[0]
    def next(self):
        if (self.index_current < self.index_last):
            self.index_current += 1
            if (self.list_iter[self.index_current] > 0):
                return self.list_iter[self.index_current]
        elif(self.index_current > self.index_last):
            print("stop that")
            return self.is_done()
    def current_item(self):
        return self.list_iter[self.index_current]
    def previous(self):
        if (self.index_current > 0):
            self.index_current -= 1
            if (self.list_iter[self.index_current] != 0):
                return self.list_iter[self.index_current]
            else:
                self.previous()
        else:
            return self.is_done()
    def is_done(self):
        print("there are no more items")
        return None

if __name__ == "__main__":
    print("Hello world")
    list_example = Collection([0,1,0,2,0,3,0,4,0,5,6,0,7,0,8,0,9,0])
    print(list_example)
    # list_example.add(10)
    # list_example.remove(0)
    print("----- Full -----")
    while True:
        if( list_example.list_interator_full.next() != None ):
            print(list_example.list_interator_full.current_item())
        else:
            break
    print(list_example.list_interator_full.previous())
    print(list_example.list_interator_full.first())
    print("----- No Zero -----")
    for x in range(list_example.list_interator_no_zero.index_last):
        if( list_example.list_interator_no_zero.next() != None ):
            print(list_example.list_interator_no_zero.current_item())
    print("End")
