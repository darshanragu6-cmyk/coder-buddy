import streamlit as st
from auth import require_login, logout_button
from styles import GLOBAL_CSS
from components import sidebar_profile, sidebar_status_card, wix_navbar, starfield, groq_api_key_input

st.set_page_config(page_title="Coder Buddy", page_icon="🤖", layout="wide", initial_sidebar_state="expanded")

require_login()

st.markdown(GLOBAL_CSS, unsafe_allow_html=True)
starfield()

# session-wide counters used by the Dashboard
for key, default in [
    ("stat_projects", 0),
    ("stat_files", 0),
    ("stat_ai_requests", 0),
    ("recent_activity", []),
    ("build_log", []),
    ("chat_history", []),
    ("prompt_prefill", ""),
]:
    if key not in st.session_state:
        st.session_state[key] = default

with st.sidebar:
    sidebar_profile(st.session_state.get("username", "user"))
    st.markdown("<br>", unsafe_allow_html=True)
    groq_api_key_input()

pages = {
    "Workspace": [
        st.Page("pages/dashboard.py", title="Dashboard", icon="🏠"),
        st.Page("pages/build.py", title="Build", icon="⚡", default=True),
        st.Page("pages/files.py", title="Files", icon="📁"),
        st.Page("pages/chat.py", title="Chat", icon="💬"),
        st.Page("pages/templates.py", title="Templates", icon="🧩"),
        st.Page("pages/settings.py", title="Settings", icon="⚙️"),
    ]
}

nav = st.navigation(pages)

wix_navbar(st.session_state.get("username", "Account"))

with st.sidebar:
    sidebar_status_card()
    logout_button()

nav.run()
