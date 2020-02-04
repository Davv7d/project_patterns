# podczas robienia tego zadania korzystałem z tego przykładu:
# https://sourcemaking.com/design_patterns/observer/python/1
# oraz dostosowałem się do konwencji w nim odnośnie nazw np z _
# dodaje tą informacje na wypadek gdyby moja praca była podobna do czyjeś innej

import abc
import datetime
class Subject(abc.ABC):
    def __init__(self):
        self._observers = set()
        self._subject_state = None
    def attach(self,observer):
        observer._subcject = self
        self._observers.add(observer)
    def detach(self,observer):
        observer._subcject = None
        self._observers.discard(observer)
    def _notify(self):
        for observer in self._observers:
            observer.update(self._subject_state)

class Concrete_Subject(Subject):
    def get_state(self):
        return self._subject_state
    def set_state(self,arg):
        self._subject_state = arg
        self._notify()


class Observer(abc.ABC):
    def __init__(self):
        self._subcject = None
        self._obserw_state = []
    @abc.abstractmethod
    def update(self, arg):
        pass

class Concret_obsrever(Observer):
    def update(self, subcject):
        self._obserw_state.append((self._subcject,subcject,datetime.datetime.now()))
        print("update  ",self._obserw_state)


if __name__ == "__main__":
    print("hello word")
    subject = Concrete_Subject()
    concrete_observer_1 = Concret_obsrever()
    concrete_observer_2 = Concret_obsrever()
    subject.attach(concrete_observer_1)
    subject.attach(concrete_observer_2)
    subject.set_state(123)
    subject.set_state(12)
    subject.set_state(1)
    print(subject.get_state())