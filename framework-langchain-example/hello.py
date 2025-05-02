import os
import asyncio

from langchain_openai import ChatOpenAI
from mcp import ClientSession
from mcp.client.sse import sse_client
from langgraph.prebuilt import create_react_agent
from langchain_mcp_adapters.tools import load_mcp_tools


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
    # Connect to Cloudera AI Inference service model
    model = ChatOpenAI(
        model = MODEL_NAME,
        base_url = BASE_URL,
        api_key = API_KEY
    )

    # Connect to MCP Server
    async with sse_client(url = "http://localhost:8000/sse") as (read, write):
        async with ClientSession(read, write) as session:
            # Initialize the connection
            await session.initialize()

            # Get tools
            tools = await load_mcp_tools(session)

            # Create and run the agent
            agent = create_react_agent(model, tools)
            agent_response = await agent.ainvoke({"messages": "What information can I learn form the `airlines_snappy` table? I'm looking for a quick answer, don't ask for clarifying questions."})

            print(agent_response)

            # print(agent_response['messages'][3].content)


if __name__ == "__main__":
    asyncio.run(main())
