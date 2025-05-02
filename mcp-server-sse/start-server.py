# Load environment variables from .env file
from dotenv import load_dotenv
from pathlib import Path
load_dotenv(dotenv_path=Path(__file__).parent.parent / ".env")

import subprocess
import os

def start_mcp_server(env: dict[str,str] = {}) -> subprocess.Popen:
  server_script_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../iceberg-mcp-server/server.py"))

  if not os.path.exists(server_script_path):
    raise FileNotFoundError(f"Server script not found at {server_script_path}. Make sure you cloned the submodule correctly.")

  exec_env = os.environ.copy() # inherit everything first :contentReference[oaicite:10]{index=10}
  exec_env.update(env)

  try:
    process = subprocess.Popen(
      ["uv", "run", server_script_path],
      env=exec_env,
    )
    print(f"MCP server started with PID: {process.pid}")
    return process
  except Exception as e:
    print(f"Failed to start MCP server: {e}")
    raise

if __name__ == "__main__":
  env = {
    "IMPALA_HOST": os.getenv("IMPALA_HOST"),
    "IMPALA_USER": os.getenv("IMPALA_USER"),
    "IMPALA_PASSWORD": os.getenv("IMPALA_PASSWORD"),
    "MCP_TRANSPORT": "sse"
  }
  server_process = start_mcp_server(env)
  try:
    server_process.wait()
  except KeyboardInterrupt:
    print("Shutting down MCP server...")
    server_process.terminate()
