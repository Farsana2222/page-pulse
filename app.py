from flask import Flask, render_template, request, jsonify
from parser import analyze_page

app = Flask(__name__)

# Home Page
@app.route("/")
def home():
    return render_template("index.html")

# API Endpoint
@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.get_json()

    if not data or "url" not in data:
        return jsonify({"error": "Please enter a URL"}), 400

    url = data["url"]

    result = analyze_page(url)

    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True)