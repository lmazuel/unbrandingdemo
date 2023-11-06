# Adapted from:
# https://github.com/openai/openai-python/blob/main/examples/demo.py

import os
from openai import OpenAIClient
from corehttp.credentials import ServiceKeyCredential

api_key = os.getenv("OPENAI_API_KEY")

client = OpenAIClient(ServiceKeyCredential(api_key))

print("----- standard request -----")
completion = client.chat_completions.create_chat_completion(
    {
        "model": "gpt-4",
        "messages": [
            {
                "role": "user",
                "content": "Say this is a test",
            },
        ],
    }
)
print(completion.choices[0].message.content)

print("\n----- failed request -----")
completion = client.chat_completions.create_chat_completion(
    {
        #    "model": "gpt-4",
        "messages": [
            {
                "role": "user",
                "content": "Say this is a test",
            },
        ],
    }
)
