# utils/formatter.py

def format_predicate(predicate):
    """
    Format texte lisible
    """
    return str(predicate)


def format_default_rule(default):
    """
    α : β ⊢ δ
    """
    return f"{default.prerequisite} : {default.justification} ⊢ {default.conclusion}"


def predicate_to_latex(predicate):
    """
    Convertit un prédicat en LaTeX
    """
    args = ", ".join(predicate.arguments)
    name = predicate.name

    if predicate.negated:
        return rf"\neg {name}({args})"
    return rf"{name}({args})"


def default_to_latex(default):
    """
    α : β ⊢ δ en LaTeX
    """
    return (
        predicate_to_latex(default.prerequisite)
        + r" : "
        + predicate_to_latex(default.justification)
        + r" \vdash "
        + predicate_to_latex(default.conclusion)
    )


def extension_to_latex(extension):
    """
    Affiche une extension sous forme d'ensemble
    """
    beliefs = ", ".join(
        predicate_to_latex(p) for p in extension.beliefs
    )
    return r"\{" + beliefs + r"\}"
