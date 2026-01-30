# logic/reasoner.py

from logic.extension import Extension

class Reasoner:
    def __init__(self, theory):
        self.theory = theory
        self.extensions = []
        self.trace = []

    def generate_extensions(self):
        initial = self.theory.initial_extension()
        self.extensions = []
        self.trace = []
        self._expand_extension(initial)
        return self.extensions

    def _expand_extension(self, extension):
        applicable = []

        for d in self.theory.defaults:
            if d.is_applicable(extension):
                if extension.is_consistent_with(d.conclusion):
                    applicable.append(d)

        if not applicable:
            self.extensions.append(extension)
            return

        for default in applicable:
            new_extension = extension.copy()
            new_extension.add_belief(default.conclusion)
            new_extension.applied_defaults.append(default)

            self.trace.append({
                "extension": extension,
                "default": default,
                "conclusion": default.conclusion
            })

            self._expand_extension(new_extension)
