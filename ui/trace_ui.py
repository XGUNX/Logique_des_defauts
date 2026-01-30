import streamlit as st
from utils.formatter import default_to_latex, predicate_to_latex

def trace_ui():
    if "trace" not in st.session_state or not st.session_state["trace"]:
        st.info("Aucune trace de raisonnement.")
        return

    st.subheader("🧠 Trace du raisonnement")

    for step, entry in enumerate(st.session_state["trace"], 1):
        st.markdown(f"### Étape {step}")

        # Défaut appliqué
        st.latex(default_to_latex(entry["default"]))

        # Conclusion ajoutée
        st.markdown(
            f"➡️ Conclusion ajoutée : "
            f"${predicate_to_latex(entry['conclusion'])}$"
        )
