import os

from crewai import LLM
from crewai import Agent, Crew, Task
from crewai_tools import MCPServerAdapter

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

def main():
    # Connect to Cloudera AI Inference service model
    model = LLM(
        model="openai/" + MODEL_NAME,
        api_key=API_KEY,
        base_url=BASE_URL
    )

    # Connect to MCP Server
    with MCPServerAdapter({"url": "http://localhost:8000/sse"}) as tools:
        # Define a single agent
        agent = Agent(
            role="Assistant",
            goal="Answer questions clearly and concisely without asking for clarifications. You can access tools to retrieve data from Iceberg via Impala.",
            backstory="You are a helpful assistant that specializes in answering questions.",
            llm=model,
            tools=tools, # tools is now a list of CrewAI Tools matching 1:1 with the MCP server's tools
            verbose=True
        )

        # Define a single task
        task = Task(
            description=(
                """Answer this question by readig a few rows from the data:
                What information can I learn from the `airlines_snappy` table?
                """
            ),
            expected_output="A short english summary of the available data.",
            agent=agent
        )

        # Create a crew with the agent and task
        crew = Crew(agents=[agent], tasks=[task])
        crew.kickoff()


if __name__ == "__main__":
    main()
