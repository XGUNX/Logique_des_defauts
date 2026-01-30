# logic/theory.py

from logic.extension import Extension

class DefaultTheory:
    def __init__(self):
        self.facts = set()
        self.defaults = []

    def add_fact(self, fact):
        self.facts.add(fact.predicate)

    def add_default(self, default_rule):
        self.defaults.append(default_rule)

    def initial_extension(self):
        return Extension(beliefs=self.facts)
