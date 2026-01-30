# ui/facts_ui.py

import streamlit as st
from utils.parser import parse_predicate
from utils.validators import validate_fact

def facts_ui(theory):
    st.subheader("📌 Faits (W)")

    # Affichage des faits existants
    if theory.facts:
        for i, f in enumerate(sorted(theory.facts, key=str)):
            col1, col2 = st.columns([5, 1])
            col1.write(str(f))
            if col2.button("❌", key=f"del_fact_{i}"):
                theory.facts.remove(f)
                st.rerun()
    else:
        st.info("Aucun fait défini.")

    st.markdown("---")
    st.markdown("### ➕ Ajouter un fait")

    fact_input = st.text_input("Fait (ex: Oiseau(Tweety))")

    if st.button("Ajouter le fait"):
        try:
            predicate = parse_predicate(fact_input)
            validate_fact(predicate, theory.facts)
            theory.add_fact(type("Fact", (), {"predicate": predicate})())
            st.success("Fait ajouté.")
            st.rerun()
        except Exception as e:
            st.error(str(e))
