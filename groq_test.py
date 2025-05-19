import os
from langchain_groq import ChatGroq

llm = ChatGroq(model="qwen-qwq-32b", api_key="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")
response = llm.invoke([{"role": "user", "content": "Hello!"}])
print(response) 