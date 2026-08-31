import os
from typing import TypedDict, List, Annotated, Optional
import operator

from dotenv import load_dotenv
from langgraph.graph import StateGraph, END
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage, ToolMessage

from tools import ALL_TOOLS

# Local dev convenience only: if a .env with GROQ_API_KEY exists it's used as a
# fallback default. Nothing here is required — in the Streamlit app the key is
# typed into the sidebar each session and never touches disk or the repo.
load_dotenv()

MAX_RETRIES = 3


def resolve_api_key(explicit_key: Optional[str] = None) -> Optional[str]:
    """Resolve a Groq API key with priority:
    1. explicit_key passed in (e.g. from the sidebar / session_state)
    2. GROQ_API_KEY environment variable / local .env (dev convenience)
    3. st.secrets, if running under Streamlit and configured
    Returns None if nothing is found — callers decide how to handle that.
    """
    if explicit_key:
        return explicit_key

    env_key = os.getenv("GROQ_API_KEY")
    if env_key:
        return env_key

    try:
        import streamlit as st
        return st.secrets.get("GROQ_API_KEY")
    except Exception:
        return None


def _build_llm(api_key: str):
    return ChatGroq(model="openai/gpt-oss-120b", temperature=0, api_key=api_key)


# ---- State ----
class AgentState(TypedDict):
    messages: Annotated[List, operator.add]
    task: str
    retries: int
    done: bool


PLANNER_SYSTEM_PROMPT = """You are an expert software engineer AI agent building a complete,
functional web application based on the user's request.

You have tools to write_file, read_file, list_files, and run_command.

Rules:
- Build a COMPLETE, working app (HTML/CSS/JS, or a simple framework if it fits better).
- Always create at minimum: index.html, a CSS file, and a JS file, properly linked together.
- Write clean, functional code — no placeholders like "TODO" or "add logic here".
- Use the write_file tool to create every file. Do not just describe the code in text.
- After writing all files, call list_files to confirm, then explain briefly what you built.
- If something fails, fix it and retry rather than giving up.
"""


def _build_graph(llm_with_tools):
    def agent_node(state: AgentState):
        messages = state["messages"]
        if not messages:
            messages = [
                SystemMessage(content=PLANNER_SYSTEM_PROMPT),
                HumanMessage(content=state["task"]),
            ]
        response = llm_with_tools.invoke(messages)
        return {"messages": [response]}

    def tool_node(state: AgentState):
        last_message = state["messages"][-1]
        tool_messages = []
        for call in last_message.tool_calls:
            tool_fn = next((t for t in ALL_TOOLS if t.name == call["name"]), None)
            if tool_fn is None:
                result = f"ERROR: unknown tool {call['name']}"
            else:
                try:
                    result = tool_fn.invoke(call["args"])
                except Exception as e:
                    result = f"ERROR running {call['name']}: {e}"
            tool_messages.append(
                ToolMessage(content=str(result), tool_call_id=call["id"])
            )
        return {"messages": tool_messages}

    def should_continue(state: AgentState):
        last_message = state["messages"][-1]
        if isinstance(last_message, AIMessage) and last_message.tool_calls:
            return "tools"
        return END

    graph = StateGraph(AgentState)
    graph.add_node("agent", agent_node)
    graph.add_node("tools", tool_node)
    graph.set_entry_point("agent")
    graph.add_conditional_edges("agent", should_continue, {"tools": "tools", END: END})
    graph.add_edge("tools", "agent")
    return graph.compile()


def get_llm(api_key: Optional[str] = None):
    """Build a plain (no-tools) ChatGroq instance for chat-style usage (e.g. the Chat page)."""
    key = resolve_api_key(api_key)
    if not key:
        raise ValueError(
            "No Groq API key available. Paste one into the sidebar's 'Groq API Key' field "
            "(get a free key at https://console.groq.com/keys)."
        )
    return _build_llm(key)


def stream_run(task: str, api_key: Optional[str] = None):
    """Generator version of run() — yields dicts so a UI (Streamlit, etc.) can display
    progress live instead of only printing to console.
    Yields: {"type": "agent"|"tool", "content": str}
    """
    key = resolve_api_key(api_key)
    if not key:
        yield {
            "type": "agent",
            "content": (
                "⚠️ No Groq API key found. Paste your key into the sidebar's "
                "'Groq API Key' field and try again."
            ),
        }
        return

    llm = _build_llm(key)
    llm_with_tools = llm.bind_tools(ALL_TOOLS)
    app = _build_graph(llm_with_tools)

    for event in app.stream(
        {"messages": [], "task": task, "retries": 0, "done": False},
        {"recursion_limit": 50},
    ):
        for node_name, node_output in event.items():
            for msg in node_output.get("messages", []):
                if isinstance(msg, AIMessage) and msg.content:
                    yield {"type": "agent", "content": msg.content}
                elif isinstance(msg, ToolMessage):
                    yield {"type": "tool", "content": msg.content}


def run(task: str, api_key: Optional[str] = None):
    for item in stream_run(task, api_key=api_key):
        if item["type"] == "agent":
            print(f"\n[agent] {item['content']}")
        else:
            print(f"[tool result] {item['content'][:200]}")
    print("\n✅ Done. Check the ./generated_project folder.")
