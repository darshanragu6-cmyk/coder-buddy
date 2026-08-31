import os
import streamlit as st
from tools import PROJECT_ROOT
from components import page_header

page_header("Files", "Browse and inspect everything Coder Buddy has generated.")

if not os.path.exists(PROJECT_ROOT) or not any(os.walk(PROJECT_ROOT)):
    st.info("No files yet — head to Build to generate a project first.")
    if st.button("⚡ Go to Build"):
        st.switch_page("pages/build.py")
    st.stop()

files = []
for root, _, filenames in os.walk(PROJECT_ROOT):
    for fname in filenames:
        rel = os.path.relpath(os.path.join(root, fname), PROJECT_ROOT)
        files.append(rel)
files = sorted(files)

col_tree, col_code, col_info = st.columns([1, 2, 1])

with col_tree:
    st.markdown('<div class="cb-card">', unsafe_allow_html=True)
    st.markdown("#### 📁 Explorer")
    search = st.text_input("Search files", label_visibility="collapsed", placeholder="Search files...")
    visible_files = [f for f in files if search.lower() in f.lower()] if search else files

    if "selected_file" not in st.session_state or st.session_state.selected_file not in files:
        st.session_state.selected_file = files[0] if files else None

    for f in visible_files:
        icon = "🟨" if f.endswith(".js") else "🟦" if f.endswith((".ts", ".tsx")) else \
               "🟧" if f.endswith(".html") else "🟪" if f.endswith(".css") else \
               "🐍" if f.endswith(".py") else "📄"
        is_active = f == st.session_state.selected_file
        label = f"**{icon} {f}**" if is_active else f"{icon} {f}"
        if st.button(label, key=f"file_{f}", use_container_width=True):
            st.session_state.selected_file = f
            st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

with col_code:
    st.markdown('<div class="cb-card">', unsafe_allow_html=True)
    selected = st.session_state.selected_file
    if selected:
        full_path = os.path.join(PROJECT_ROOT, selected)
        with open(full_path, "r", encoding="utf-8", errors="replace") as f:
            content = f.read()
        ext = selected.split(".")[-1]
        lang_map = {"html": "html", "css": "css", "js": "javascript", "py": "python", "json": "json", "md": "markdown"}
        st.markdown(f"**{selected}**")
        st.code(content, language=lang_map.get(ext, "text"), line_numbers=True)
        st.download_button("⬇️ Download this file", content, file_name=os.path.basename(selected))

        if selected.endswith(".html"):
            with st.expander("🔍 Live Preview", expanded=False):
                st.components.v1.html(content, height=450, scrolling=True)
    st.markdown('</div>', unsafe_allow_html=True)

with col_info:
    st.markdown('<div class="cb-card">', unsafe_allow_html=True)
    st.markdown("#### ℹ️ File Info")
    if selected:
        full_path = os.path.join(PROJECT_ROOT, selected)
        size_kb = os.path.getsize(full_path) / 1024
        st.write(f"**Path:** `{selected}`")
        st.write(f"**Size:** {size_kb:.1f} KB")
        st.write(f"**Type:** {selected.split('.')[-1].upper()}")
    st.markdown("---")
    st.markdown("#### 🤖 Ask AI about this file")
    q = st.text_input("Question", label_visibility="collapsed", placeholder="e.g. what does this do?")
    if st.button("Ask", use_container_width=True) and q:
        st.info("Hook this up to a code-Q&A chain when ready — placeholder for now.")
    st.markdown('</div>', unsafe_allow_html=True)
