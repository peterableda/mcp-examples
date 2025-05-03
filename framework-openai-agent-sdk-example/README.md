# OpenAI Agent SDK — SSE Example

This example shows how to run the [OpenAI Agent SDK](https://github.com/openai/openai-agents-python) against a [Model Context Protocol (MCP)](https://modelcontextprotocol.io/introduction) Server using Server-Sent Events (SSE) and LLMs hosted by [Cloudera AI Inference service](https://www.cloudera.com/products/machine-learning/ai-inference-service.html).


## References

- OpenAI MCP docs: https://openai.github.io/openai-agents-python/mcp/
- Example code: https://github.com/openai/openai-agents-python/blob/main/examples/mcp/sse_example/main.py


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

Running: Can you tell me the schema of the `airlines_snappy` table?

Answer: The schema of the `airlines_snappy` table is as follows:

"""
["air_data", "air_food", "air_acct_date", "air_unique customers", "air_customer_id", "air_favourite_colour", "air_destination", "air_discount", "air_m       length", "air_woo_lllaguage", "air_Factors_change", "air_route", "air_Product_Four_Cs", "air_airline", "air_route#", "firsttakeoff", "air_totalplan", "takingtal", "air_ metric_a"]
"""

This schema includes 19 fields.
```
