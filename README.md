
---

# 📊 PG Score Flask API & Website

A Flask-based application that calculates a **PG Score** (credibility/engagement score) for users based on their social profile data.
It fetches data from an external API (using a username query), processes it, and returns a score between **0–100**.
Includes a simple web frontend for checking PG scores.

---

## 🚀 Features

* Flask API endpoint: `/pgscore?userName=<username>`
* Fetches user JSON data from an external API
* Calculates a weighted PG Score using followers, verification, activity, etc.
* Frontend website (`/`) with an input box to check scores
* API Key support (Bearer token in headers)
* JSON response output (easy to integrate with other apps)

---

## 📂 Project Structure

```
pgscore_app/
│── app.py              # Main Flask app
│── templates/
│     └── index.html    # Web frontend
│── README.md           # Documentation
```

---

## ⚙️ Installation

### 1. Clone repo

```bash
git clone https://github.com/yourusername/pgscore-app.git
cd pgscore-app
```

### 2. Create virtual environment

```bash
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
```

### 3. Install dependencies

```bash
pip install flask requests
```

### 4. Set API key (if required by your external API)

```bash
export API_KEY="your-secret-key"    # Mac/Linux
setx API_KEY "your-secret-key"      # Windows
```

---

## ▶️ Running the App

Start the Flask server:

```bash
python app.py
```

By default, it runs on:

```
http://127.0.0.1:5000
```

---

## 🌐 Usage

### 1. API (JSON Response)

Send a request:

```bash
http://127.0.0.1:5000/pgscore?userName=johndoe
```

Response example:

```json
{
  "userName": "johndoe",
  "PG_Score": 82
}
```

### 2. Website (Frontend)

Open in browser:

```
http://127.0.0.1:5000/
```

* Enter a username in the input box
* Click **Check**
* See PG Score displayed on the page

---

## 📊 PG Score Calculation (Simplified)

* **Followers count** → up to 30 pts
* **Blue Verified** → +15 pts
* **Profile completeness** (bio, pic, cover) → +15 pts
* **Engagement (tweets, media, likes)** → up to 15 pts
* **Account age** → up to 15 pts
* **Penalties** (sensitive, automated, unavailable) → -10 to -20 pts

Final score is normalized between **0–100**.

---

## 🛠️ Example API Integration

If you want to call this API from another service:

```python
import requests

res = requests.get("http://127.0.0.1:5000/pgscore?userName=johndoe")
print(res.json())
```

---

## 📌 Notes

* Replace `https://example.com/api/user` in `app.py` with your actual data source.
* If your API requires authentication, ensure `API_KEY` is set.
* Handle missing users gracefully (`data = response.json(); user = data.get("data") or {}`).

---



