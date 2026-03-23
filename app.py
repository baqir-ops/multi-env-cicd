from flask import Flask, jsonify
import os

app = Flask(__name__)
ENVIRONMENT = os.getenv("APP_ENV", "development")

@app.route("/")
def home():
    return jsonify({
        "message": "Multi-Env CI/CD App",
        "environment": ENVIRONMENT,
        "status": "running"
    })

@app.route("/health")
def health():
    return jsonify({"status": "healthy"}), 200

@app.route("/about")
def about():
    return jsonify({
        "project": "Project 2 - Multi-Env Pipeline",
        "author": "baqir-ops",
        "version": "1.0.0"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
