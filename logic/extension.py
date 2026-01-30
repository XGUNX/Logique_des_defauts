# logic/extension.py

class Extension:
    def __init__(self, beliefs=None, applied_defaults=None):
        # Ensemble de prédicats (faits + conclusions)
        self.beliefs = set(beliefs) if beliefs else set()

        # Défauts déjà appliqués dans cette extension
        self.applied_defaults = list(applied_defaults) if applied_defaults else []

    def is_consistent_with(self, predicate):
        """
        Vérifie qu'un prédicat n'entre pas en contradiction
        avec les croyances actuelles.
        """
        for belief in self.beliefs:
            if belief.is_contradictory(predicate):
                return False
        return True

    def add_belief(self, predicate):
        """
        Ajoute un prédicat si la consistance est respectée.
        """
        if not self.is_consistent_with(predicate):
            raise ValueError("Contradiction détectée")
        self.beliefs.add(predicate)

    def copy(self):
        """
        Copie profonde de l'extension (nécessaire pour le raisonnement)
        """
        return Extension(
            beliefs=self.beliefs.copy(),
            applied_defaults=self.applied_defaults.copy()
        )

    def signature(self):
        """
        Signature immuable utilisée par le Reasoner
        pour éviter les boucles infinies.
        """
        return frozenset(str(b) for b in self.beliefs)

    def __str__(self):
        return "{ " + ", ".join(str(b) for b in self.beliefs) + " }"

    def __repr__(self):
        return self.__str__()
