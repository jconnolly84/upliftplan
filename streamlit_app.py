import streamlit as st
from auth_utils import get_google_auth_url, get_microsoft_auth_url

st.set_page_config(page_title="UpliftPlan", page_icon="🧠")

st.image("assets/upliftplan_logo.png", width=220)
st.title("Welcome to UpliftPlan")

st.markdown("### Sign in to continue")

col1, col2 = st.columns(2)

with col1:
    if st.button("Sign in with Google"):
        st.experimental_redirect(get_google_auth_url())

with col2:
    if st.button("Sign in with Microsoft"):
        st.experimental_redirect(get_microsoft_auth_url())