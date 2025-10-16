from flask import Flask, jsonify, request
import requests
import json

app = Flask(__name__)

# 🔗 Google Drive Direct Download Link
# Replace the ID with your file’s ID if reuploaded
DATA_URL = "https://drive.google.com/uc?export=download&id=1Tdvr6yJWMZctg-h7L1SxFidiX52x1J53"

# 🧠 Load JSON data from Google Drive
def load_data():
    try:
        response = requests.get(DATA_URL)
        response.raise_for_status()
        text = response.text.strip()

        # Handle potential malformed JSON (missing [ ])
        if not text.startswith("["):
            text = "[" + text
        if not text.endswith("]"):
            text = text + "]"

        data = json.loads(text)
        return data
    except Exception as e:
        return {"error": f"Failed to load data: {str(e)}"}

# 🏠 Home route
@app.route("/")
def home():
    query = request.args.get("userid")
    if query:
        return search_userid(query)
    return "✅ Telegram API live! Use ?userid=2133422 to search."

# 🔍 Search by account_id
def search_userid(user_id):
    data = load_data()
    if isinstance(data, dict) and "error" in data:
        return jsonify(data)

    results = [user for user in data if str(user.get("account_id")) == str(user_id)]
    if results:
        return jsonify(results[0])
    else:
        return jsonify({"message": "❌ No user found with that ID."})

# 📄 Get all data (for testing, optional)
@app.route("/data")
def get_all_data():
    data = load_data()
    return jsonify(data)

# ▶️ Run app
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)