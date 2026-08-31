import streamlit as st
from styles import STARFIELD_HTML


def starfield():
    """Render the animated space/stars background layer. Call once per page load."""
    st.markdown(STARFIELD_HTML, unsafe_allow_html=True)


def stat_card(icon: str, value: str, label: str):
    st.markdown(
        f"""
        <div class="stat-card">
            <div class="stat-icon">{icon}</div>
            <div class="stat-value">{value}</div>
            <div class="stat-label">{label}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def badge(text: str):
    return f'<span class="badge">{text}</span>'


def timeline_step(status: str, title: str, desc: str):
    """status: 'done' | 'active' | 'pending' | 'failed'"""
    icons = {"done": "✓", "active": "◉", "pending": "○", "failed": "✕"}
    st.markdown(
        f"""
        <div class="timeline-step">
            <div class="timeline-icon ts-{status}">{icons.get(status, "○")}</div>
            <div>
                <div class="timeline-title">{title}</div>
                <div class="timeline-desc">{desc}</div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def template_card_html(icon: str, name: str, desc: str, tags: list) -> str:
    tag_html = "".join(badge(t) for t in tags)
    return f"""
    <div class="tpl-card">
        <div class="tpl-icon">{icon}</div>
        <div class="tpl-name">{name}</div>
        <div class="tpl-desc">{desc}</div>
        <div>{tag_html}</div>
    </div>
    """


def chat_bubble(role: str, content: str):
    css_class = "chat-bubble-user" if role == "user" else "chat-bubble-ai"
    st.markdown(f'<div class="{css_class}">{content}</div>', unsafe_allow_html=True)


def sidebar_profile(username: str):
    initial = (username or "?")[0].upper()
    st.markdown(
        f"""
        <div class="sidebar-profile">
            <div class="sidebar-avatar">{initial}</div>
            <div>
                <div class="sidebar-username">{username}</div>
                <div class="sidebar-role">Developer</div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def groq_api_key_input():
    """Sidebar field for a user-supplied Groq API key.

    Stored only in st.session_state for the life of the browser session —
    never written to disk, .env, or the repo, so nothing ends up in git for
    GitHub's secret scanner to flag.
    """
    if "groq_api_key" not in st.session_state:
        st.session_state.groq_api_key = ""
    if "show_groq_api_key" not in st.session_state:
        st.session_state.show_groq_api_key = False

    st.markdown(
        """
        <div class="groq-key-row">
            <span>Groq API Key</span>
        </div>
        """,
        unsafe_allow_html=True,
    )

    col_input, col_eye = st.columns([6, 1])
    with col_input:
        key = st.text_input(
            "Groq API Key",
            value=st.session_state.groq_api_key,
            type="default" if st.session_state.show_groq_api_key else "password",
            placeholder="gsk_...",
            label_visibility="collapsed",
            help="Get a free key at console.groq.com/keys. Kept only in this "
                 "browser session — never saved to a file or committed to git.",
            key="groq_api_key_widget",
        )
    with col_eye:
        icon = "🙈" if st.session_state.show_groq_api_key else "👁️"
        if st.button(icon, key="toggle_groq_key_visibility", help="Show/hide key"):
            st.session_state.show_groq_api_key = not st.session_state.show_groq_api_key
            st.rerun()

    st.session_state.groq_api_key = key

    if key:
        st.markdown(
            '<div class="groq-key-status ok">🟢 Key set for this session</div>',
            unsafe_allow_html=True,
        )
    else:
        st.markdown(
            '<div class="groq-key-status warn">⚪ No key yet — required to build or chat</div>',
            unsafe_allow_html=True,
        )

    return key


def sidebar_status_card():
    st.markdown(
        """
        <div class="sidebar-status-card">
            <div><span class="status-dot"></span><b>Coder Buddy AI</b></div>
            <div class="timeline-desc">Your AI-powered coding assistant</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def page_header(title: str, subtitle: str):
    st.markdown(f'<div class="cb-h1">{title}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="cb-sub">{subtitle}</div>', unsafe_allow_html=True)


def hero_banner(eyebrow: str, title: str, accent_word: str, subtitle: str):
    """Big bold marketing-style header, black-navbar tone."""
    title_html = title.replace(accent_word, f'<span class="accent">{accent_word}</span>') if accent_word else title
    st.markdown(
        f"""
        <div class="hero-eyebrow">{eyebrow}</div>
        <div class="hero-title">{title_html}</div>
        <div class="hero-subtitle">{subtitle}</div>
        """,
        unsafe_allow_html=True,
    )


def wix_navbar(username: str, active_label: str = ""):
    st.markdown(
        f"""
        <div class="wix-navbar">
            <div class="wix-logo">
                <div class="wix-logo-badge">🤖</div>
                CODER BUDDY
            </div>
            <div class="wix-nav-links">
                <a href="#">Dashboard</a>
                <a href="#">Build</a>
                <a href="#">Files</a>
                <a href="#">Templates</a>
            </div>
            <div class="wix-pill-btn">{username or "Account"}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )
