# ui/results_ui.py

import streamlit as st
from utils.formatter import extension_to_latex

def results_ui():
    st.subheader("📊 Extensions")

    if "extensions" not in st.session_state:
        st.info("Aucune extension calculée.")
        return

    for i, ext in enumerate(st.session_state["extensions"], 1):
        with st.expander(f"Extension {i}"):
            st.latex(extension_to_latex(ext))
