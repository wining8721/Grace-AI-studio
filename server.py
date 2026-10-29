import os
from flask import Flask, jsonify

app = Flask(__name__)
@app.after_request
def allow_website(response):
    response.headers["Access-Control-Allow-Origin"] = "https://wining8721.github.io"
    return response
    
@app.route("/")
def home():
    return jsonify({
        "app": "Grace AI Studio",
        "message": "Welcome to Grace AI Studio!",
        "status": "Backend is running"
    })

@app.route("/health")
def health():
    return jsonify({"status": "ok"})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
