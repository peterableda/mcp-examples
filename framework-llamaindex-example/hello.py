import os
import asyncio


from llama_index.llms.nvidia import NVIDIA
from llama_index.tools.mcp import BasicMCPClient, McpToolSpec
from llama_index.core.agent.workflow import FunctionAgent, ToolCallResult, ToolCall
from llama_index.core.workflow import Context

# Load environment variables from .env file
from dotenv import load_dotenv
from pathlib import Path
load_dotenv(dotenv_path=Path(__file__).parent.parent / ".env")

API_KEY = os.getenv("API_KEY")
MODEL_NAME = os.getenv("MODEL_NAME", "meta/llama-3.1-8b-instruct")
BASE_URL = os.getenv(
    "BASE_URL",
    "https://ml-2dad9e26-62f.env.cloudera.site/namespaces/serving-default/endpoints/llama3-8b-throughput/v1/"
)  # Example Cloudera AI Inference service Endpoint


async def main():
    # Connect to MCP Server
    mcp_client = BasicMCPClient("http://127.0.0.1:8000/sse")
    mcp_tool = McpToolSpec(client=mcp_client)

    # Connect to Cloudera AI Inference service model
    model = NVIDIA(
        model = MODEL_NAME,
        base_url = BASE_URL,
        api_key = API_KEY,
        is_function_calling_model=True
    )

    # Create LlamaIndex agent with model & MCP server
    tools = await mcp_tool.to_tool_list_async()
    agent = FunctionAgent(
        name="Agent",
        description="An agent that can fetch the ip info of the user.",
        tools=tools,
        llm=model,
        system_prompt="You are an AI assistant.\n"+
                    "I'm looking for a quick answers, don't ask for clarifying questions.",
    )

    # Run the agent!
    agent_context = Context(agent)

    handler = agent.run("What information can I learn form the `airlines_snappy` table?", ctx=agent_context)
    async for event in handler.stream_events():
        if type(event) == ToolCall:
            print(f"Calling tool {event.tool_name} with kwargs {event.tool_kwargs}")
        elif type(event) == ToolCallResult:
            print(f"Tool {event.tool_name} returned {event.tool_output}")

    response = await handler

    print("Agent: ", str(response))


if __name__ == "__main__":
    asyncio.run(main())
