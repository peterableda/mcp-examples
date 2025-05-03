# OpenAI Agent SDK — SSE Example

This example shows how to run the [CrewAI SDK](https://github.com/crewAIInc/crewAI-tools) against a [Model Context Protocol (MCP)](https://modelcontextprotocol.io/introduction) Server using Server-Sent Events (SSE) and LLMs hosted by [Cloudera AI Inference service](https://www.cloudera.com/products/machine-learning/ai-inference-service.html).


## References

- CrewAI docs: https://github.com/crewAIInc/crewAI-tools


## Prerequisites
A `.env` file in project root with (or set these env-vars in your shell):
```ini
API_KEY="<your JWT token>"
MODEL_NAME="<your model name>"
BASE_URL="<your Cloudera AI Inference endpoint>"
```

Obtain a JWT token → see [Cloudera AI auth guide](https://docs.cloudera.com/machine-learning/cloud/ai-inference/topics/ml-caii-authentication.html)

Find your model name & endpoint → see [Cloudera AI inference guide](https://docs.cloudera.com/machine-learning/cloud/ai-inference/topics/ml-caii-inference-using-openai-phython-sdk-session.html)

## Running the Example
```bash
uv run ./hello.py
```

### Example run
```
✗ uv run ./hello.py

# Agent: Assistant
## Task: Answer this question by readig a few rows from the data:
                What information can I learn from the `airlines_snappy` table?


# Agent: Assistant
## Thought: Thought:
## Using tool: execute_query
## Tool Input:
"{\"query\": \"DESCRIBE airlines_snappy\"}"
## Tool Output:
[["month", "int", ""], ["dayofmonth", "int", ""], ["dayofweek", "int", ""], ["deptime", "int", ""], ["crsdeptime", "int", ""], ["arrtime", "int", ""], ["crsarrtime", "int", ""], ["uniquecarrier", "string", ""], ["flightnum", "int", ""], ["tailnum", "string", ""], ["actualelapsedtime", "int", ""], ["crselapsedtime", "int", ""], ["airtime", "int", ""], ["arrdelay", "int", ""], ["depdelay", "int", ""], ["origin", "string", ""], ["dest", "string", ""], ["distance", "int", ""], ["taxiin", "int", ""], ["taxiout", "int", ""], ["cancelled", "int", ""], ["cancellationcode", "string", ""], ["diverted", "string", ""], ["carrierdelay", "int", ""], ["weatherdelay", "int", ""], ["nasdelay", "int", ""], ["securitydelay", "int", ""], ["lateaircraftdelay", "int", ""], ["year", "int", ""]]


# Agent: Assistant
## Final Answer:
The available data includes information about flights such as their departure and arrival times, delays, and distances. It also includes information about the airlines, flights, and destinations. This can be used to analyze flight schedules, delays, and other metrics related to airline operations.
```
