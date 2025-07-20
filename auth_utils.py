import os
import streamlit as st
from urllib.parse import urlencode

def get_google_auth_url():
    params = {
        "response_type": "code",
        "client_id": os.environ.get("GOOGLE_OAUTH_CLIENT_ID"),
        "redirect_uri": os.environ.get("GOOGLE_OAUTH_REDIRECT_URI"),
        "scope": "openid email profile",
        "access_type": "offline",
        "prompt": "consent"
    }
    return f"https://accounts.google.com/o/oauth2/auth?{urlencode(params)}"

def get_microsoft_auth_url():
    tenant = os.environ.get("MS_TENANT_ID")
    params = {
        "client_id": os.environ.get("MS_CLIENT_ID"),
        "response_type": "code",
        "redirect_uri": os.environ.get("MS_REDIRECT_URI"),
        "response_mode": "query",
        "scope": "openid email profile offline_access",
        "prompt": "select_account"
    }
    return f"https://login.microsoftonline.com/{tenant}/oauth2/v2.0/authorize?{urlencode(params)}"