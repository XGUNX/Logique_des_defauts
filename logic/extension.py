# logic/extension.py

class Extension:
    def __init__(self, beliefs=None, applied_defaults=None):
        self.beliefs = set(beliefs) if beliefs else set()
        self.applied_defaults = list(applied_defaults) if applied_defaults else []

    def is_consistent_with(self, predicate):
        for belief in self.beliefs:
            if belief.is_contradictory(predicate):
                return False
        return True

    def add_belief(self, predicate):
        if not self.is_consistent_with(predicate):
            raise ValueError("Contradiction détectée")
        self.beliefs.add(predicate)

    def copy(self):
        return Extension(
            beliefs=self.beliefs.copy(),
            applied_defaults=self.applied_defaults.copy()
        )

    def __str__(self):
        return "\n".join(str(b) for b in self.beliefs)

    def __repr__(self):
        return self.__str__()
