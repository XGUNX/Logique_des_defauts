# logic/predicate.py

class Predicate:
    def __init__(self, name, arguments=None, negated=False):
        self.name = name
        self.arguments = arguments if arguments else []
        self.negated = negated

    def negate(self):
        return Predicate(
            self.name,
            self.arguments,
            not self.negated
        )

    def is_contradictory(self, other):
        return (
            self.name == other.name
            and self.arguments == other.arguments
            and self.negated != other.negated
        )

    def __eq__(self, other):
        return (
            self.name == other.name
            and self.arguments == other.arguments
            and self.negated == other.negated
        )

    def __hash__(self):
        return hash((self.name, tuple(self.arguments), self.negated))

    def __str__(self):
        args = ", ".join(self.arguments)
        prefix = "¬" if self.negated else ""
        return f"{prefix}{self.name}({args})"

    def __repr__(self):
        return self.__str__()
