# logic/default_rule.py

class DefaultRule:
    def __init__(self, prerequisite, justification, conclusion):
        self.prerequisite = prerequisite
        self.justification = justification
        self.conclusion = conclusion

    def is_applicable(self, extension):
        # α ∈ E
        if self.prerequisite not in extension.beliefs:
            return False

        # ¬β ∉ E
        if self.justification.negate() in extension.beliefs:
            return False

        # ne pas réappliquer un défaut déjà utilisé
        if self in extension.applied_defaults:
            return False

        return True

    def __str__(self):
        return f"{self.prerequisite} : {self.justification} ⊢ {self.conclusion}"

    def __repr__(self):
        return self.__str__()
