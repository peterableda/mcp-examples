# mcp-server-sse

Starts the [Cloudera Iceberg MCP Server](https://github.com/cloudera/iceberg-mcp-server) via its SSE endpoint.

## Requirements
- A `.env` file in project root with or the same ENV variables set for the process.
```ini
IMPALA_HOST = "<coordinator-service.env.cloudera.site>"
IMPALA_USER = "<username>"
IMPALA_PASSWORD = "<password>"
```

# Installation & Usage
```bash
uv pip install .
FASTMCP_PORT=9000 uv run start-server.py
```

Server listens on `localhost:9000`.
