import streamlit as st
from agent import get_llm
from components import page_header
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage

page_header("Chat", "Talk to Coder Buddy about anything code-related.")

col_main, col_side = st.columns([3, 1])

with col_side:
    st.markdown('<div class="cb-card">', unsafe_allow_html=True)
    st.markdown("#### Suggested")
    for prompt in ["Explain this error", "Refactor a function", "Write unit tests", "Optimize this query"]:
        if st.button(prompt, use_container_width=True, key=f"sugg_{prompt}"):
            st.session_state.chat_prefill = prompt
            st.rerun()
    st.markdown("---")
    if st.button("🗑️ Clear conversation", use_container_width=True):
        st.session_state.chat_history = []
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

with col_main:
    for msg in st.session_state.chat_history:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    prefill = st.session_state.pop("chat_prefill", None)
    user_input = st.chat_input("Ask Coder Buddy anything...")
    if prefill and not user_input:
        user_input = prefill

    if user_input and not st.session_state.get("groq_api_key"):
        st.warning("Paste your Groq API key into the sidebar first — it's free at console.groq.com/keys.")

    elif user_input:
        st.session_state.stat_ai_requests += 1
        st.session_state.chat_history.append({"role": "user", "content": user_input})
        with st.chat_message("user"):
            st.markdown(user_input)

        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                try:
                    llm = get_llm(st.session_state.get("groq_api_key"))
                    history_msgs = [SystemMessage(content="You are Coder Buddy, a helpful AI coding assistant.")]
                    for m in st.session_state.chat_history[:-1]:
                        if m["role"] == "user":
                            history_msgs.append(HumanMessage(content=m["content"]))
                        else:
                            history_msgs.append(AIMessage(content=m["content"]))
                    history_msgs.append(HumanMessage(content=user_input))
                    response = llm.invoke(history_msgs)
                    st.markdown(response.content)
                    reply_content = response.content
                except Exception as e:
                    reply_content = f"⚠️ Error: {e}"
                    st.error(reply_content)

        st.session_state.chat_history.append({"role": "assistant", "content": reply_content})
