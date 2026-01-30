# utils/parser.py

import re
from logic.predicate import Predicate

PREDICATE_REGEX = r"(¬)?([A-Za-z_][A-Za-z0-9_]*)\((.*?)\)"

def parse_predicate(text: str) -> Predicate:
    """
    Parse une chaîne du type :
    - Oiseau(Tweety)
    - ¬Pacifiste(Nixon)
    - Vole(x)

    Retourne un objet Predicate
    """
    text = text.strip()

    match = re.fullmatch(PREDICATE_REGEX, text)
    if not match:
        raise ValueError(f"Format de prédicat invalide : {text}")

    negation, name, args = match.groups()

    arguments = []
    if args:
        arguments = [arg.strip() for arg in args.split(",")]

    return Predicate(
        name=name,
        arguments=arguments,
        negated=bool(negation)
    )
