# Disable tracing
from agents import set_tracing_disabled
set_tracing_disabled(True)

import os
import asyncio
from pathlib import Path

from openai import AsyncOpenAI
from agents import Agent, Runner, OpenAIChatCompletionsModel
from agents.mcp import MCPServer, MCPServerSse

# Load environment variables from .env file
from dotenv import load_dotenv
load_dotenv(dotenv_path=Path(__file__).parent.parent / ".env")

API_KEY = os.getenv("API_KEY")
MODEL_NAME = os.getenv("MODEL_NAME", "meta/llama-3.1-8b-instruct")
BASE_URL = os.getenv(
    "BASE_URL",
    "https://ml-2dad9e26-62f.env.cloudera.site/namespaces/serving-default/endpoints/llama3-8b-throughput/v1/"
)  # Example Cloudera AI Inference service Endpoint

async def main():
    async with MCPServerSse(
        name="Cloudera Iceberg MCP Server",
        params={
            "url": "http://localhost:8000/sse",
        },
        client_session_timeout_seconds=30.0
    ) as mcp_server:
        # Connect to Cloudera AI Inference service model
        model = OpenAIChatCompletionsModel(
            model = MODEL_NAME,
            openai_client = AsyncOpenAI(
                api_key = API_KEY,
                base_url = BASE_URL
            )
        )

        # Create OpenAI agent with model & MCP server
        agent = Agent(
            name="Assistant",
            instructions="Answer questions, use tools that are available for you.",
            model=model,
            mcp_servers=[mcp_server],
        )

        message = "Can you tell me the schema of the `airlines_snappy` table?"
        print(f"Running: {message}")
        result = await Runner.run(starting_agent=agent, input=message)
        print(f"\nAnswer: {result.final_output}")


if __name__ == "__main__":
    asyncio.run(main())
