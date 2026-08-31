import datetime
import streamlit as st
from components import stat_card, page_header

hour = datetime.datetime.now().hour
greeting = "Good morning" if hour < 12 else "Good afternoon" if hour < 18 else "Good evening"

page_header(f"{greeting} 👋", "Here's what's happening in your workspace.")

c1, c2, c3, c4 = st.columns(4)
with c1:
    stat_card("📦", str(st.session_state.get("stat_projects", 0)), "Total Projects")
with c2:
    stat_card("📄", str(st.session_state.get("stat_files", 0)), "Files Generated")
with c3:
    stat_card("🤖", str(st.session_state.get("stat_ai_requests", 0)), "AI Requests")
with c4:
    stat_card("⚡", str(len(st.session_state.get("recent_activity", []))), "Recent Actions")

st.markdown("<br>", unsafe_allow_html=True)

col_left, col_right = st.columns([2, 1])

with col_left:
    st.markdown('<div class="cb-card">', unsafe_allow_html=True)
    st.markdown("#### Recent Activity")
    activity = st.session_state.get("recent_activity", [])
    if activity:
        for item in reversed(activity[-8:]):
            st.markdown(f"- {item}")
    else:
        st.caption("Nothing yet — head to Build to create your first project.")
    st.markdown('</div>', unsafe_allow_html=True)

with col_right:
    st.markdown('<div class="cb-card">', unsafe_allow_html=True)
    st.markdown("#### Quick Actions")
    if st.button("⚡ New Build", use_container_width=True):
        st.switch_page("pages/build.py")
    if st.button("📁 View Files", use_container_width=True):
        st.switch_page("pages/files.py")
    if st.button("🧩 Browse Templates", use_container_width=True):
        st.switch_page("pages/templates.py")
    st.markdown('</div>', unsafe_allow_html=True)
