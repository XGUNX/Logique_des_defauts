# ui/trace_ui.py

import streamlit as st
from utils.formatter import default_to_latex

def trace_ui():
    st.subheader("🧭 Traçage du raisonnement")

    if "trace" not in st.session_state or not st.session_state["trace"]:
        st.info("Aucun traçage disponible.")
        return

    for step, entry in enumerate(st.session_state["trace"], 1):
        st.markdown(f"### Étape {step}")
        st.latex(default_to_latex(entry["default"]))
        st.markdown(f"➡️ Conclusion ajoutée : **{entry['conclusion']}**")
