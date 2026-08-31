import streamlit as st
from components import page_header

page_header("Settings", "Manage your account and preferences.")

tabs = st.tabs(["Account", "Appearance", "AI Model", "Notifications", "Security", "Preferences"])

with tabs[0]:
    st.markdown('<div class="cb-card">', unsafe_allow_html=True)
    st.write(f"**Username:** {st.session_state.get('username', 'user')}")
    st.text_input("Display name", value=st.session_state.get("username", ""))
    st.text_input("Email", placeholder="you@example.com")
    st.button("Save changes")
    st.markdown('</div>', unsafe_allow_html=True)

with tabs[1]:
    st.markdown('<div class="cb-card">', unsafe_allow_html=True)
    st.toggle("Dark mode", value=True, disabled=True, help="Coder Buddy is dark-themed by default in this build.")
    st.selectbox("Accent color", ["Purple / Blue (default)", "Cyan", "Emerald"])
    st.markdown('</div>', unsafe_allow_html=True)

with tabs[2]:
    st.markdown('<div class="cb-card">', unsafe_allow_html=True)
    st.selectbox("Model", ["openai/gpt-oss-120b (Groq)", "llama-3.3-70b-versatile (Groq)"])
    st.slider("Temperature", 0.0, 1.0, 0.0, 0.1)
    st.caption("Changing these here doesn't rewire the backend yet — hook into agent.py's llm init when ready.")
    st.markdown('</div>', unsafe_allow_html=True)

with tabs[3]:
    st.markdown('<div class="cb-card">', unsafe_allow_html=True)
    st.toggle("Email me when a build completes", value=False)
    st.toggle("Desktop notifications", value=True)
    st.markdown('</div>', unsafe_allow_html=True)

with tabs[4]:
    st.markdown('<div class="cb-card">', unsafe_allow_html=True)
    st.text_input("Change password", type="password")
    st.text_input("Confirm password", type="password")
    st.button("Update password")
    st.markdown('</div>', unsafe_allow_html=True)

with tabs[5]:
    st.markdown('<div class="cb-card">', unsafe_allow_html=True)
    st.selectbox("Default build mode", ["Standard", "Full Stack", "Advanced"])
    st.toggle("Auto-open Files tab after a build", value=True)
    st.markdown('</div>', unsafe_allow_html=True)
