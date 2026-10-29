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

@app.route("/api/script", methods=["POST"])
def create_script():
    from flask import request

    data = request.get_json(silent=True) or {}
    idea = str(data.get("idea", "")).strip()

    if not idea:
        return jsonify({"error": "Please enter your movie idea."}), 400

    script = (
        "GRACE AI STUDIO - STORY DRAFT\n\n"
        f"Story idea: {idea}\n\n"
        "SCENE 1 - THE BEGINNING\n"
        f"Introduce the characters and setting for: {idea}\n\n"
        "SCENE 2 - THE CHALLENGE\n"
        "Show the main character facing an important problem.\n\n"
        "SCENE 3 - THE TURNING POINT\n"
        "Show a decision that changes the story.\n\n"
        "SCENE 4 - THE ENDING\n"
        "Bring the story to a meaningful conclusion."
    )

    return jsonify({"script": script})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
