from flask import Flask, render_template, from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from openai import OpenAI
import os

app = Flask(__name__)
CORS(app)

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message")

    try:
        response = client.responses.create(
            model="gpt-4o-mini",
            input=[
                {"role": "system", "content": "आप एक मददगार AI असिस्टेंट हैं। हमेशा हिंदी में उत्तर दें।"},
                {"role": "user", "content": user_message}
            ]
        )

        reply = response.output_text
        return jsonify({"reply": reply})

    except Exception as e:
        return jsonify({"reply": str(e)}), 500