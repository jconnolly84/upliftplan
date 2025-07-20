import streamlit as st
from auth_utils import (
    get_google_auth_url,
    get_microsoft_auth_url,
    handle_google_callback,
    handle_microsoft_callback,
)
from upliftplan_ui import render_upliftplan_ui

st.set_page_config(page_title="UpLiftPlan", page_icon="favicon.png", layout="centered")

def handle_callback():
    query_params = st.query_params
    if "code" in query_params:
        provider = st.session_state.get("oauth_provider", "google")
        code = query_params["code"]
        if provider == "google":
            handle_google_callback(code)
        elif provider == "microsoft":
            handle_microsoft_callback(code)
        st.rerun()

handle_callback()

if "user" in st.session_state:
    render_upliftplan_ui()
else:
    st.image("uplift_plan.png", width=200)  # <-- New logo
    st.title("Login to UpLiftPlan")
    col1, col2 = st.columns(2)
    with col1:
        st.image("google_logo.png", width=40)
        auth_url = get_google_auth_url()
        if st.button("Login with Google"):
            st.session_state['oauth_provider'] = 'google'
            st.write(f"[Click here to log in with Google]({auth_url})", unsafe_allow_html=True)
    with col2:
        st.image("microsoft_logo.png", width=40)
        ms_auth_url = get_microsoft_auth_url()
        if st.button("Login with Microsoft"):
            st.session_state['oauth_provider'] = 'microsoft'
            st.write(f"[Click here to log in with Microsoft]({ms_auth_url})", unsafe_allow_html=True)
