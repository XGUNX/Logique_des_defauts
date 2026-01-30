# utils/validators.py

def check_no_contradiction(predicates):
    """
    Vérifie qu'il n'y a pas p et ¬p dans un ensemble
    """
    for p in predicates:
        for q in predicates:
            if p.is_contradictory(q):
                return False
    return True


def validate_fact(predicate, facts):
    """
    Vérifie qu'un fait n'entre pas en contradiction
    avec les faits existants
    """
    for fact in facts:
        if predicate.is_contradictory(fact):
            raise ValueError(
                f"Contradiction détectée avec le fait existant : {fact}"
            )


def validate_default_rule(default_rule):
    """
    Vérifie la cohérence interne d'un défaut
    """
    if default_rule.prerequisite.is_contradictory(default_rule.conclusion):
        raise ValueError(
            "Un défaut ne peut pas conclure la négation de son prérequis"
        )
