# logic/reasoner.py

from logic.extension import Extension
from itertools import product
from logic.default_rule import DefaultRule
class Reasoner:
    def __init__(self, theory):
        self.theory = theory
        self.extensions = []
        self.trace = []
        self.visited = set()

    def generate_extensions(self):
        initial = self.theory.initial_extension()
        self.extensions = []
        self.trace = []
        self._expand_extension(initial)
        return self.extensions
   

    def _expand_extension(self, extension):

        signature = extension.signature()

        if signature in self.visited:
            return   # ⛔ extension déjà explorée

        self.visited.add(signature)

        applicable = []

        for d in self.theory.defaults:
            instantiated_defaults = self._instantiate_default(d)

            for default in instantiated_defaults:
                if default in extension.applied_defaults:
                    continue

                if (default.is_applicable(extension)
                        and default.conclusion not in extension.beliefs
                    ):
                    if extension.is_consistent_with(default.conclusion):
                        applicable.append(default)

        # Aucun défaut applicable → extension finale
        if not applicable:
            if extension not in self.extensions:
                self.extensions.append(extension)
            return

        # Sinon, on explore chaque branche
        for default in applicable:
            new_extension = extension.copy()
            new_extension.add_belief(default.conclusion)
            new_extension.applied_defaults.append(default)

            self.trace.append({
                "extension": extension.copy(),
                "default": default,                   
                "conclusion": default.conclusion       
            })


            self._expand_extension(new_extension)


            
            
    def _extract_constants(self):
        constants = set()
        for fact in self.theory.facts:
            for arg in fact.arguments:
                if not arg.islower():
                    constants.add(arg)
        return constants
    
    
    def _instantiate_default(self, default):
        constants = self._extract_constants()

        variables = set(
            arg
            for arg in default.prerequisite.arguments
            if arg.islower()
        )

        if not variables:
            return [default]

        instantiated = []

        for combo in product(constants, repeat=len(variables)):
            substitution = dict(zip(variables, combo))

            α = default.prerequisite.substitute(substitution)
            β = default.justification.substitute(substitution)
            δ = default.conclusion.substitute(substitution)

            instantiated.append(DefaultRule(α, β, δ))

        return instantiated
    
    
   