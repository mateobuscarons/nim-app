from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

# Create client with a longer timeout
client = OpenAI(
  base_url = "https://integrate.api.nvidia.com/v1",
  api_key = "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"
)

try:
    print("Testing connection to NVIDIA API...")
    completion = client.chat.completions.create(
        model="nvidia/llama-3.3-nemotron-super-49b-v1",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Hello"}
        ],
        max_tokens=50
    )
    print("Connection successful!")
    print(completion.choices[0].message.content)
except Exception as e:
    print(f"Connection failed: {e}")