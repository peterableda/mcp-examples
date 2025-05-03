# LangChain/LangGraph — SSE Example

This example shows how to run the [LangChain MCP SDK](https://github.com/langchain-ai/langchain-mcp-adapters) against a [Model Context Protocol (MCP)](https://modelcontextprotocol.io/introduction) Server using Server-Sent Events (SSE) and LLMs hosted by [Cloudera AI Inference service](https://www.cloudera.com/products/machine-learning/ai-inference-service.html).


## References

- LangChain MCP docs: https://langchain-ai.github.io/langgraph/agents/mcp/


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

{'messages': [HumanMessage(content="What information can I learn form the `airlines_snappy` table? I'm looking for a quick answer, don't ask for clarifying questions.", additional_kwargs={}, response_metadata={}, id='da9e645c-eba8-4e62-a73f-317a0f66ad7c'), AIMessage(content='', additional_kwargs={'tool_calls': [{'id': 'chatcmpl-tool-1116297b84b6416893e16c3f6ee6fdd4', 'function': {'arguments': '{}', 'name': 'get_schema'}, 'type': 'function'}], 'refusal': None}, response_metadata={'token_usage': {'completion_tokens': 22, 'prompt_tokens': 350, 'total_tokens': 372, 'completion_tokens_details': None, 'prompt_tokens_details': None}, 'model_name': 'meta/llama-3.1-8b-instruct', 'system_fingerprint': None, 'id': 'chat-acc06901f90f423788c157a04fa253ba', 'finish_reason': 'tool_calls', 'logprobs': None}, id='run-7cc217b5-9d1a-4536-9cd1-1a97aec5caac-0', tool_calls=[{'name': 'get_schema', 'args': {}, 'id': 'chatcmpl-tool-1116297b84b6416893e16c3f6ee6fdd4', 'type': 'tool_call'}], usage_metadata={'input_tokens': 350, 'output_tokens': 22, 'total_tokens': 372, 'input_token_details': {}, 'output_token_details': {}}), ToolMessage(content='["airlines_snappy", "airports_nifi_iceberg", "anomaly_detection", "churn_prototype", "home_credit_bureau", "home_credit_bureau_balance", "home_credit_credit_card_balance", "home_credit_installments_payments", "home_credit_pos_cash_balance", "home_credit_previous_application", "hospital_admissions", "taxi_zone_lookup_csv"]', name='get_schema', id='6c7debd5-a74e-46b7-b7d4-e583db28e292', tool_call_id='chatcmpl-tool-1116297b84b6416893e16c3f6ee6fdd4'), AIMessage(content='The `airlines_snappy` table is one of the 220 tables in the current Impala database, and hence, you can gather various pieces of information from it by querying the table. The schema of the table remains to be seen in order to know the type of information that can be extracted.', additional_kwargs={'refusal': None}, response_metadata={'token_usage': {'completion_tokens': 61, 'prompt_tokens': 2701, 'total_tokens': 2762, 'completion_tokens_details': None, 'prompt_tokens_details': None}, 'model_name': 'meta/llama-3.1-8b-instruct', 'system_fingerprint': None, 'id': 'chat-9e0640454025438fae1265e1d74769d8', 'finish_reason': 'stop', 'logprobs': None}, id='run-edc7f2a0-912e-44ec-8998-b7bfcab77f2b-0', usage_metadata={'input_tokens': 2701, 'output_tokens': 61, 'total_tokens': 2762, 'input_token_details': {}, 'output_token_details': {}})]}
```
