from flask import Flask, request, jsonify, render_template
import requests, os
from datetime import datetime

app = Flask(__name__)

# ===================
# PG SCORE FUNCTION
# ===================
def calculate_pg_score(user):
    score = 0

    followers = user.get("followers", 0)
    if followers > 10000:
        score += 30
    elif followers > 1000:
        score += 20
    elif followers > 100:
        score += 10
    else:
        score += 5

    if user.get("isBlueVerified"):
        score += 15
    if user.get("description"):
        score += 5
    if user.get("profilePicture"):
        score += 5
    if user.get("coverPicture"):
        score += 5

    statuses = user.get("statusesCount", 0)
    media = user.get("mediaCount", 0)
    favs = user.get("favouritesCount", 0)
    engagement = statuses + media + favs
    if engagement > 1000:
        score += 15
    elif engagement > 100:
        score += 10
    else:
        score += 5

    created_at = user.get("createdAt")
    if created_at:
        try:
            created_date = datetime.fromisoformat(created_at)
            years_old = (datetime.now() - created_date).days / 365
            if years_old > 5:
                score += 15
            elif years_old > 1:
                score += 10
            else:
                score += 5
        except:
            score += 5

    if user.get("possiblySensitive"):
        score -= 10
    if user.get("isAutomated"):
        score -= 15
    if user.get("unavailable"):
        score -= 20

    return max(0, min(score, 100))


# ===================
# ROUTES
# ===================

# Serve website
@app.route("/")
def home():
    return render_template("index.html")

# API endpoint
@app.route("/pgscore", methods=["GET"])
def pg_score():
    username = request.args.get("userName")
    if not username:
        return jsonify({"error": "userName query param is required"}), 400

    # Example API call (replace with real one)
    api_url = "https://api.twitterapi.io/twitter/user/info"
    querystring = {"userName": username}
    headers = {"X-API-Key": "857f59e1a2354af0be65433b54da1309"}

    response = requests.get(api_url, params=querystring, headers=headers)
    if response.status_code != 200:
        return jsonify({"error": "Failed to fetch user data"}), 500

    data = response.json()
    user = data.get("data", {})
    score = calculate_pg_score(user)
    print(response.json())
    return jsonify({"userName": user.get("userName"), "PG_Score": score})


if __name__ == "__main__":
    app.run(debug=True)
