import json
import os
import hashlib
import streamlit as st

from styles import STARFIELD_CSS, STARFIELD_HTML

USERS_FILE = "users.json"


def _hash(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()


def _load_users() -> dict:
    if os.path.exists(USERS_FILE):
        with open(USERS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}


def _save_users(users: dict):
    with open(USERS_FILE, "w", encoding="utf-8") as f:
        json.dump(users, f)


def _signup(username: str, password: str):
    if not username or not password:
        return False, "Username and password can't be empty."
    users = _load_users()
    if username in users:
        return False, "That username is already taken."
    users[username] = _hash(password)
    _save_users(users)
    return True, "Account created — you can log in now."


def _login(username: str, password: str):
    users = _load_users()
    if username not in users:
        return False, "No account with that username."
    if users[username] != _hash(password):
        return False, "Incorrect password."
    return True, "Welcome back."


AUTH_CSS = """
<style>
.stApp {
    background:
        radial-gradient(ellipse 900px 600px at 15% 10%, rgba(139,92,246,0.20), transparent 60%),
        radial-gradient(ellipse 800px 500px at 85% 20%, rgba(56,189,248,0.16), transparent 60%),
        radial-gradient(ellipse at top left, #10132a 0%, #05060a 55%);
    font-family: 'Inter', 'Segoe UI', sans-serif;
}

/* ===== top bar, echoes the "wonderland" pill-nav look ===== */
.auth-topbar {
    position: relative;
    z-index: 1;
    display: flex;
    justify-content: space-between;
    align-items: center;
    max-width: 640px;
    margin: 1.5rem auto 0 auto;
    padding: 10px 6px;
}
.auth-logo {
    display: flex;
    align-items: center;
    gap: 8px;
    color: #f1f2f8;
    font-weight: 800;
    letter-spacing: 0.5px;
}
.auth-logo-badge {
    width: 30px; height: 30px; border-radius: 9px;
    background: linear-gradient(135deg, #8b5cf6, #38bdf8);
    display: flex; align-items: center; justify-content: center;
    font-size: 0.95rem;
}
.auth-burger { display: flex; flex-direction: column; gap: 4px; }
.auth-burger span { width: 26px; height: 2px; background: rgba(241,242,248,0.6); border-radius: 2px; }

/* ===== bold hero, styled after the reference "HEY! Stay Tuned" banner ===== */
.auth-hero {
    position: relative;
    z-index: 1;
    text-align: center;
    max-width: 640px;
    margin: 2.2rem auto 0.5rem auto;
    padding: 0 1rem;
}
.auth-hero-eyebrow {
    display: inline-block;
    padding: 5px 14px;
    border-radius: 999px;
    background: rgba(139, 92, 246, 0.12);
    border: 1px solid rgba(139, 92, 246, 0.35);
    color: #c3c8e4;
    font-size: 0.72rem;
    font-weight: 700;
    letter-spacing: 1.2px;
    text-transform: uppercase;
    margin-bottom: 0.9rem;
}
.auth-hero-title {
    font-size: clamp(2rem, 5vw, 3rem);
    font-weight: 800;
    line-height: 1.08;
    color: #f1f2f8;
    margin-bottom: 0.5rem;
}
.auth-hero-title .pop {
    background: linear-gradient(135deg, #a78bfa 0%, #8b5cf6 45%, #38bdf8 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    filter: drop-shadow(0 2px 14px rgba(139, 92, 246, 0.45));
}
.auth-hero-subtitle {
    color: #9aa0c0;
    font-size: 0.92rem;
    letter-spacing: 0.3px;
    max-width: 460px;
    margin: 0 auto;
}

.auth-card {
    position: relative;
    z-index: 1;
    background: rgba(18, 20, 36, 0.65);
    backdrop-filter: blur(16px);
    border: 1px solid rgba(139, 92, 246, 0.25);
    border-radius: 16px;
    padding: 2.2rem 2rem;
    max-width: 420px;
    margin: 1.8rem auto 3rem auto;
    box-shadow: 0 8px 40px rgba(0, 0, 0, 0.45);
}
.auth-title {
    text-align: center;
    font-size: 1.5rem;
    font-weight: 800;
    color: #f1f2f8;
    margin-bottom: 0.2rem;
}
.auth-subtitle {
    text-align: center;
    color: #9aa0c0;
    margin-bottom: 1.5rem;
    font-size: 0.88rem;
}
div[data-testid="stRadio"] > label { display: none; }
div[data-testid="stRadio"] > div {
    display: flex;
    background: rgba(255,255,255,0.04);
    border-radius: 9px;
    padding: 4px;
    gap: 4px;
}
div[data-testid="stRadio"] > div label {
    flex: 1;
    text-align: center;
    border-radius: 7px;
    padding: 6px 0;
    margin: 0 !important;
    cursor: pointer;
    color: #c3c8e4 !important;
    transition: all 0.25s ease;
}
div[data-testid="stRadio"] input:checked + div {
    background: linear-gradient(90deg, #8b5cf6, #38bdf8);
    border-radius: 7px;
    color: white !important;
}
.stTextInput input {
    background: rgba(255,255,255,0.03) !important;
    color: #f1f2f8 !important;
    border: 1px solid rgba(139, 92, 246, 0.25) !important;
    border-radius: 9px !important;
}
div.stButton > button {
    width: 100%;
    background: linear-gradient(90deg, #8b5cf6, #7c3aed);
    color: white;
    border: none;
    border-radius: 9px;
    padding: 0.6rem 0;
    font-weight: 700;
    transition: transform 0.15s ease, box-shadow 0.15s ease;
}
div.stButton > button:hover {
    transform: translateY(-1px);
    box-shadow: 0 6px 20px rgba(139, 92, 246, 0.4);
}
</style>
"""


def require_login():
    if st.session_state.get("logged_in"):
        return

    st.markdown(STARFIELD_CSS, unsafe_allow_html=True)
    st.markdown(AUTH_CSS, unsafe_allow_html=True)
    st.markdown(STARFIELD_HTML, unsafe_allow_html=True)

    st.markdown(
        """
        <div class="auth-topbar">
            <div class="auth-logo"><div class="auth-logo-badge">🤖</div> CODER BUDDY</div>
            <div class="auth-burger"><span></span><span></span><span></span></div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class="auth-hero">
            <div class="auth-hero-eyebrow">✨ AI Software Engineer</div>
            <div class="auth-hero-title">Hey! Welcome to <span class="pop">Coder Buddy</span></div>
            <div class="auth-hero-subtitle">Sign in and turn your ideas into working code — the agent is ready when you are.</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown('<div class="auth-card">', unsafe_allow_html=True)
    st.markdown('<div class="auth-title">🔐 Sign in</div>', unsafe_allow_html=True)
    st.markdown('<div class="auth-subtitle">Access your AI coding workspace</div>', unsafe_allow_html=True)

    mode = st.radio("mode", ["Login", "Sign Up"], horizontal=True, label_visibility="collapsed")
    username = st.text_input("Username", key="auth_username")
    password = st.text_input("Password", type="password", key="auth_password")

    if mode == "Login":
        if st.button("Log In"):
            ok, msg = _login(username, password)
            if ok:
                st.session_state.logged_in = True
                st.session_state.username = username
                st.rerun()
            else:
                st.error(msg)
    else:
        if st.button("Create Account"):
            ok, msg = _signup(username, password)
            if ok:
                st.success(msg + " Switch to Login above.")
            else:
                st.error(msg)

    st.markdown('</div>', unsafe_allow_html=True)
    st.stop()


def logout_button():
    if st.session_state.get("logged_in"):
        if st.button("🚪 Log out"):
            st.session_state.logged_in = False
            st.session_state.username = None
            st.rerun()
