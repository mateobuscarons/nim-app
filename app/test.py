from openai import OpenAI
# base url + /v1
client = OpenAI(
  base_url = "",
  api_key = ""
)

# List available model names
try:
    models = client.models.list()
    for model in models.data:
        print(model.id)
except Exception as e:
    print(f"Error listing models: {e}")
