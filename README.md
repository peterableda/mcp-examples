# MCP Examples

This repository contains minimal, end-to-end examples for utilizing [Model Context Protocol (MCP)](https://modelcontextprotocol.io/introduction) in a variety of frameworks—LangChain, CrewAI, OpenAI Agent SDK, LlamaIndex, Microsoft AutoGen—backed by open-source LLMs hosted on [Cloudera AI Inference service](https://www.cloudera.com/products/machine-learning/ai-inference-service.html).

MCP is everywhere these days. This project is a hands‑on way to test MCP and assess its adoption across the AI ecosystem.

## Components
### MCP Server
The examples use a standalone Cloudera Iceberg MCP server to provide data as context for LLMs. This server connects to sample Apache Iceberg tables through Impala, runs as an independent process, and exposes the Server‑Sent Events (SSE) endpoint.

See [mcp-server-sse/](mcp-server-sse/) for the standalone SSE‑based Iceberg server.

### Model
The examples connect to Cloudera AI Inference service, Cloudera’s model‑serving platform that offers OpenAI‑compatible endpoints with end‑to‑end privacy for both public‑cloud and on‑premises deployments. Built on KServe, it can serve any Hugging Face open‑source model as well as NVIDIA‑optimized NIM containers for maximum performance.

In these examples, we call the [meta/llama-3.1-8b-instruct](https://catalog.ngc.nvidia.com/orgs/nim/teams/meta/containers/llama-3.1-8b-instruct) NVIDIA NIM (hosted by Cloudera AI Inference Service) to drive our LLM workloads.

### Frameworks
Each framework directory is a standalone UV project and includes its own README with full instructions.
The example scripts in each directory will:
1) Load your .env settings (for connection and auth details for the Cloudera AI Inference model and Impala endpoints).
2) Connect to the MCP server over SSE.
3) Initialize the OpenAI compatible client to point at Cloudera AI Inference.
4) Spin up an Agent that listens for context updates.
5) Send a sample query.
6) Route context via SSE and LLM calls through Cloudera AI.
7) Output the Agent’s answer to your console.


| Framework                 | Location                              |
| ------------------------- | ------------------------------------- |
| **CrewAI**                | [framework-crewai-example](framework-crewai-example/) |
| **OpenAI Agent SDK**      | [framework-openai-agent-sdk-example](framework-openai-agent-sdk-example/) |
| **LangChain / LangGraph** | [framework-langchain-example](framework-langchain-example/) |
| **LlamaIndex**            | [framework-llamaindex-example](framework-llamaindex-example/) |
| **Microsoft Autogen (WIP)**     | [framework-autogen-example](framework-autogen-example/) |
