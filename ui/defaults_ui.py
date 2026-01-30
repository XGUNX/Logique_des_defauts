# ui/defaults_ui.py

import streamlit as st
from utils.parser import parse_predicate
from logic.default_rule import DefaultRule

def defaults_ui(theory):
    st.subheader("📐 Règles de défaut (D)")

    # Affichage des défauts
    if theory.defaults:
        for i, d in enumerate(theory.defaults):
            col1, col2 = st.columns([6, 1])
            col1.write(str(d))
            if col2.button("❌", key=f"del_default_{i}"):
                theory.defaults.pop(i)
                st.rerun()
    else:
        st.info("Aucun défaut défini.")

    st.markdown("---")
    st.markdown("### ➕ Ajouter un défaut")

    prereq = st.text_input("Prérequis α (ex: Oiseau(x))")
    justif = st.text_input("Justification β (ex: ¬Autruche(x))")
    concl = st.text_input("Conclusion δ (ex: Vole(x))")

    if st.button("Ajouter le défaut"):
        try:
            α = parse_predicate(prereq)
            β = parse_predicate(justif)
            δ = parse_predicate(concl)

            theory.add_default(DefaultRule(α, β, δ))
            st.success("Défaut ajouté.")
            st.rerun()
        except Exception as e:
            st.error(str(e))
