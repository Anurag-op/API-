from flask import Flask, request, jsonify
import requests
import json

app = Flask(__name__)

# your google drive link
JSON_URL = "https://drive.google.com/uc?export=download&id=1Tdvr6yJWMZctg-h7L1SxFidiX52x1J53"

@app.route('/')
def home():
    return jsonify({"message": "Telegram Account ID API is live 🚀"})

@app.route('/search')
def search_by_id():
    account_id = request.args.get("id")
    if not account_id:
        return jsonify({"error": "Please provide ?id=ACCOUNT_ID"}), 400

    try:
        text_data = requests.get(JSON_URL).text
        # Split line by line and convert each JSON
        data = [json.loads(line.strip().rstrip(',')) for line in text_data.splitlines() if line.strip()]
    except Exception as e:
        return jsonify({"error": f"Failed to read data: {e}"}), 500

    # Find user
    result = [u for u in data if str(u.get("account_id")) == str(account_id)]

    if not result:
        return jsonify({"message": "No user found with that account_id"})
    return jsonify(result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)