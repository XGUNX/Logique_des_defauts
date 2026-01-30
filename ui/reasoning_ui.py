# ui/reasoning_ui.py

import streamlit as st
from logic.reasoner import Reasoner

def reasoning_ui(theory):
    st.subheader("⚙️ Raisonnement")

    if st.button("▶️ Lancer le raisonnement"):
        reasoner = Reasoner(theory)
        extensions = reasoner.generate_extensions()

        st.session_state["extensions"] = extensions
        st.session_state["trace"] = reasoner.trace

        st.success(f"{len(extensions)} extension(s) générée(s).")
