import streamlit as st
from components import page_header, template_card_html

page_header("Templates", "Start from a ready-made stack instead of a blank prompt.")

TEMPLATES = [
    ("⚛️", "React", "A single-page app scaffold with components and routing.", ["React", "JavaScript"]),
    ("▲", "Next.js", "Full-stack React framework with SSR support.", ["Next.js", "React"]),
    ("🐍", "Python", "A clean Python project scaffold.", ["Python"]),
    ("🌶️", "Flask", "Lightweight Python web app with routes and templates.", ["Flask", "Python"]),
    ("⚡", "FastAPI", "A modern async Python API with auto docs.", ["FastAPI", "Python"]),
    ("🎈", "Streamlit", "A data app scaffold with widgets and layout.", ["Streamlit", "Python"]),
    ("🟩", "Node.js", "An Express-based backend scaffold.", ["Node.js", "Express"]),
    ("🌐", "HTML/CSS/JS", "A plain static site scaffold, no framework.", ["HTML", "CSS", "JS"]),
    ("🧩", "Full Stack", "Frontend + backend + database, wired together.", ["Full Stack"]),
]

cols = st.columns(3)
for i, (icon, name, desc, tags) in enumerate(TEMPLATES):
    with cols[i % 3]:
        st.markdown(template_card_html(icon, name, desc, tags), unsafe_allow_html=True)
        if st.button("Use Template", key=f"tpl_{name}", use_container_width=True):
            st.session_state.prompt_prefill = f"Create a {name} project: {desc}"
            st.switch_page("pages/build.py")
        st.markdown("<br>", unsafe_allow_html=True)
