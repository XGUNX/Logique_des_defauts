# logic/fact.py

from logic.predicate import Predicate

class Fact:
    def __init__(self, predicate: Predicate):
        self.predicate = predicate

    def __str__(self):
        return str(self.predicate)

    def __repr__(self):
        return self.__str__()
