# mcp-server-sse

Starts the [Cloudera Iceberg MCP Server](https://github.com/cloudera/iceberg-mcp-server) via its SSE endpoint.

## Prerequisites
A `.env` file in project root with or the same ENV variables set for the process.
```ini
IMPALA_HOST = "<coordinator-service.env.cloudera.site>"
IMPALA_USER = "<username>"
IMPALA_PASSWORD = "<password>"
```

# Installation & Usage
```bash
FASTMCP_PORT=8000 uv run start-server.py
```

Server listens on `localhost:8000`.
