# LlamaIndex SDK — SSE Example

This example shows how to run the [LlamaIndex](https://docs.llamaindex.ai/en/stable/) against a [Model Context Protocol (MCP)](https://modelcontextprotocol.io/introduction) Server using Server-Sent Events (SSE) and LLMs hosted by [Cloudera AI Inference service](https://www.cloudera.com/products/machine-learning/ai-inference-service.html).


## References

- NVIDIA LlamaIndex support: https://docs.llamaindex.ai/en/stable/examples/llm/nvidia/
- LlamaIndex MCP docs: https://docs.llamaindex.ai/en/stable/api_reference/tools/mcp/
- Example code: https://github.com/run-llama/llama_index/blob/main/llama-index-integrations/tools/llama-index-tools-mcp/examples/mcp.ipynb


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

Calling tool get_schema with kwargs {}
Tool get_schema returned meta=None content=[TextContent(type='text', text='["airlines_snappy", "airports_nifi_iceberg", "anomaly_detection", "churn_prototype", "home_credit_bureau", "home_credit_bureau_balance", "home_credit_credit_card_balance", "home_credit_installments_payments", "home_credit_pos_cash_balance", "home_credit_previous_application", "hospital_admissions", "taxi_zone_lookup_csv"]', annotations=None)] isError=False

Agent:  The `airlines_snappy` table is one of the tables in the current Impala database. It is likely a table related to airlines, but without more information, it is difficult to determine the exact nature of the table.
```
