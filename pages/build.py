import os
import shutil
import streamlit as st
from agent import stream_run
from tools import PROJECT_ROOT
from components import page_header, timeline_step, badge, hero_banner

hero_banner(
    eyebrow="AI Software Engineer",
    title="Build Anything With Coder Buddy",
    accent_word="Coder Buddy",
    subtitle="Describe your idea and let AI turn it into a working project.",
)
st.markdown("<br>", unsafe_allow_html=True)

st.markdown('<div class="cb-card">', unsafe_allow_html=True)

task = st.text_area(
    "Describe what to build",
    value=st.session_state.get("prompt_prefill", ""),
    placeholder="e.g. Build a todo app with local storage, dark mode, and drag-to-reorder",
    height=110,
    key="build_prompt",
)
st.caption(f"{len(task)} characters · Ctrl+Enter inside the box also works in most browsers")

st.markdown("**Quick prompts**")
chip_cols = st.columns(5)
suggestions = [
    "Build a portfolio website",
    "Create a REST API",
    "Build a Python dashboard",
    "Create a CRUD application",
    "Build an AI chatbot",
]
for col, suggestion in zip(chip_cols, suggestions):
    with col:
        if st.button(suggestion, key=f"chip_{suggestion}", use_container_width=True):
            st.session_state.prompt_prefill = suggestion
            st.rerun()

ctrl1, ctrl2, ctrl3, ctrl4 = st.columns([2, 1, 1, 1])
with ctrl1:
    build_clicked = st.button("⚡ Build", type="primary", use_container_width=True)
with ctrl2:
    full_stack = st.toggle("🖥️ Full Stack", value=False)
with ctrl3:
    advanced = st.toggle("⚙️ Advanced", value=False)
with ctrl4:
    if st.button("✕ Clear", use_container_width=True):
        st.session_state.prompt_prefill = ""
        st.session_state.build_log = []
        st.rerun()

st.markdown('</div>', unsafe_allow_html=True)

# ================= BUILD EXECUTION =================
if build_clicked and not st.session_state.get("groq_api_key"):
    st.warning("Paste your Groq API key into the sidebar first — it's free at console.groq.com/keys.")

elif build_clicked and task.strip():
    st.session_state.stat_ai_requests += 1
    st.session_state.build_log = []

    effective_task = task
    if full_stack:
        effective_task += " (include both frontend and a simple backend)"
    if advanced:
        effective_task += " (add extra polish: error handling, comments, responsive design)"

    st.markdown('<div class="cb-card">', unsafe_allow_html=True)
    st.markdown("#### Build Pipeline")
    timeline_container = st.empty()

    steps = [
        {"key": "start", "title": "Build started", "desc": "Initializing project", "status": "active"},
        {"key": "analyze", "title": "Analyzing request", "desc": "Understanding requirements", "status": "pending"},
        {"key": "generate", "title": "Generating code", "desc": "Writing files and components", "status": "pending"},
        {"key": "done", "title": "Build completed", "desc": "Your project is ready", "status": "pending"},
    ]

    def render_timeline():
        with timeline_container.container():
            for s in steps:
                timeline_step(s["status"], s["title"], s["desc"])

    render_timeline()
    steps[0]["status"] = "done"
    steps[1]["status"] = "active"
    render_timeline()

    log_expander = st.expander("Live agent log", expanded=True)
    seen_first_tool = False

    try:
        with log_expander:
            for item in stream_run(effective_task, api_key=st.session_state.get("groq_api_key")):
                st.session_state.build_log.append(item)
                if item["type"] == "agent" and item["content"]:
                    st.markdown(f"**🧠 Agent:** {item['content']}")
                elif item["type"] == "tool":
                    if not seen_first_tool:
                        steps[1]["status"] = "done"
                        steps[2]["status"] = "active"
                        render_timeline()
                        seen_first_tool = True
                    st.code(item["content"][:1000])

        steps[2]["status"] = "done"
        steps[3]["status"] = "done"
        render_timeline()

        # count generated files for the dashboard stats
        file_count = 0
        if os.path.exists(PROJECT_ROOT):
            for _, _, filenames in os.walk(PROJECT_ROOT):
                file_count += len(filenames)
        st.session_state.stat_files = file_count
        st.session_state.stat_projects += 1
        st.session_state.recent_activity.append(f"Built: {task[:60]}")

        st.markdown('</div>', unsafe_allow_html=True)

        # ===== Success card =====
        st.markdown(
            """
            <div class="success-card">
                <h3>✓ Build completed successfully</h3>
                <p>Your project is ready!</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.toast("Build completed!", icon="✅")

        sc1, sc2, sc3 = st.columns(3)
        with sc1:
            if st.button("📁 View Files", use_container_width=True):
                st.switch_page("pages/files.py")
        with sc2:
            if st.button("🏠 Dashboard", use_container_width=True):
                st.switch_page("pages/dashboard.py")
        with sc3:
            if os.path.exists(PROJECT_ROOT) and file_count > 0:
                zip_path = shutil.make_archive("/tmp/generated_project", "zip", PROJECT_ROOT)
                with open(zip_path, "rb") as f:
                    st.download_button(
                        "⬇️ Download ZIP",
                        f,
                        file_name="generated_project.zip",
                        use_container_width=True,
                    )

    except Exception as e:
        steps[2]["status"] = "failed"
        render_timeline()
        st.error(f"Build failed: {e}")
        st.toast("Build failed", icon="❌")
        st.markdown('</div>', unsafe_allow_html=True)

elif build_clicked:
    st.warning("Describe what you'd like to build first.")

elif st.session_state.build_log:
    st.markdown('<div class="cb-card">', unsafe_allow_html=True)
    st.markdown("#### Last Build Log")
    with st.expander("View previous log", expanded=False):
        for item in st.session_state.build_log:
            if item["type"] == "agent" and item["content"]:
                st.markdown(f"**🧠 Agent:** {item['content']}")
            else:
                st.code(item["content"][:1000])
    st.markdown('</div>', unsafe_allow_html=True)
