# app.py

import streamlit as st

from logic.theory import DefaultTheory

from ui.facts_ui import facts_ui
from ui.defaults_ui import defaults_ui
from ui.reasoning_ui import reasoning_ui
from ui.results_ui import results_ui
from ui.trace_ui import trace_ui

# -------------------------------------------------
# Configuration Streamlit
# -------------------------------------------------
st.set_page_config(
    page_title="Logique des Défauts – Reiter",
    layout="wide"
)

st.title("🧠 Logique des Défauts (Default Logic)")
st.caption("Implémentation pédagogique de la logique des défauts de Reiter")

# -------------------------------------------------
# Initialisation de l'état global
# -------------------------------------------------
if "theory" not in st.session_state:
    st.session_state["theory"] = DefaultTheory()

theory = st.session_state["theory"]

# -------------------------------------------------
# Barre latérale
# -------------------------------------------------
with st.sidebar:
    st.header("📂 Projet")

    if st.button("🆕 Nouvelle théorie"):
        st.session_state.clear()
        st.session_state["theory"] = DefaultTheory()
        st.success("Nouvelle théorie créée.")
        st.rerun()

    st.markdown("---")
    st.markdown("### ℹ️ Rappel du formalisme")
    st.latex(r"\alpha : \beta \;\vdash\; \delta")
    st.caption(
        "Si α est prouvé et si ¬β n'est pas prouvable, "
        "alors on peut conclure δ."
    )

# -------------------------------------------------
# Mise en page principale
# -------------------------------------------------
col_left, col_center, col_right = st.columns([1.2, 1.2, 1.6])

# -------------------------------------------------
# Colonne gauche : Faits
# -------------------------------------------------
with col_left:
    facts_ui(theory)

# -------------------------------------------------
# Colonne centrale : Défauts + Raisonnement
# -------------------------------------------------
with col_center:
    defaults_ui(theory)
    st.markdown("---")
    reasoning_ui(theory)

# -------------------------------------------------
# Colonne droite : Résultats
# -------------------------------------------------
with col_right:
    results_ui()
    st.markdown("---")
    trace_ui()

# -------------------------------------------------
# Pied de page
# -------------------------------------------------
st.markdown("---")
st.caption(
    "Projet académique – Représentation des connaissances avancée | "
    "Logique non monotone – Logique des défauts"
)
