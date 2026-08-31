import os
import subprocess
from langchain_core.tools import tool

PROJECT_ROOT = "generated_project"

def _safe_path(path: str) -> str:
    """Keep all file operations inside the generated_project folder."""
    os.makedirs(PROJECT_ROOT, exist_ok=True)
    full_path = os.path.join(PROJECT_ROOT, path)
    full_path = os.path.normpath(full_path)
    if not full_path.startswith(os.path.normpath(PROJECT_ROOT)):
        raise ValueError("Path escapes project root — not allowed.")
    return full_path


@tool
def write_file(path: str, content: str) -> str:
    """Write content to a file inside the generated project. Creates folders as needed.
    path: relative file path, e.g. 'index.html' or 'css/style.css'
    content: the full text content to write into the file
    """
    full_path = _safe_path(path)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    with open(full_path, "w", encoding="utf-8") as f:
        f.write(content)
    return f"Wrote {len(content)} chars to {path}"


@tool
def read_file(path: str) -> str:
    """Read and return the content of a file inside the generated project.
    path: relative file path, e.g. 'index.html'
    """
    full_path = _safe_path(path)
    if not os.path.exists(full_path):
        return f"ERROR: {path} does not exist."
    with open(full_path, "r", encoding="utf-8") as f:
        return f.read()


@tool
def list_files() -> str:
    """List all files currently in the generated project."""
    os.makedirs(PROJECT_ROOT, exist_ok=True)
    files = []
    for root, _, filenames in os.walk(PROJECT_ROOT):
        for fname in filenames:
            rel = os.path.relpath(os.path.join(root, fname), PROJECT_ROOT)
            files.append(rel)
    return "\n".join(files) if files else "No files yet."


@tool
def run_command(command: str) -> str:
    """Run a shell command inside the generated project folder (e.g. 'npm install').
    Use sparingly and only for setup/build commands, not destructive operations.
    """
    os.makedirs(PROJECT_ROOT, exist_ok=True)
    try:
        result = subprocess.run(
            command,
            shell=True,
            cwd=PROJECT_ROOT,
            capture_output=True,
            text=True,
            timeout=60,
        )
        output = result.stdout + result.stderr
        return output[-2000:] if output else "Command ran with no output."
    except subprocess.TimeoutExpired:
        return "ERROR: command timed out."
    except Exception as e:
        return f"ERROR: {e}"


ALL_TOOLS = [write_file, read_file, list_files, run_command]
