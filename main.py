from flask import Flask, jsonify
import requests
import json

app = Flask(__name__)

# Google Drive direct link to your JSON file
DATA_URL = "https://drive.google.com/uc?export=download&id=1Tdvr6yJWMZctg-h7L1SxFidiX52x1J53"

@app.route("/")
def home():
    return "✅ API is running successfully!"

@app.route("/data", methods=["GET"])
def get_data():
    try:
        response = requests.get(DATA_URL)
        data = json.loads(response.text)
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)