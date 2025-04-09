from flask import Flask, request, jsonify, render_template
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# Load config from environment (to be set via ConfigMap)
api_key = os.environ.get("API_KEY")
base_url = os.environ.get("API_BASE_URL", "https://integrate.api.nvidia.com/v1")
model_name = os.environ.get("MODEL_NAME", "nvidia/llama-3.3-nemotron-super-49b-v1")

client = OpenAI(
    base_url=base_url,
    api_key=api_key
)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    user_prompt = request.json.get('prompt', '')
    if not user_prompt:
        return jsonify({"error": "No prompt provided"}), 400

    try:
        completion = client.chat.completions.create(
            model=model_name,
            messages=[
                {"role": "system", "content": "You are a Finance expert assistant. Provide helpful, accurate, and concise responses about finance topics. Format your responses using Markdown for better readability when appropriate."},
                {"role": "user", "content": user_prompt}
            ],
            temperature=0.6,
            top_p=0.7,
            max_tokens=1024,
            frequency_penalty=0,
            presence_penalty=0
        )
        return jsonify({"response": completion.choices[0].message.content})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
