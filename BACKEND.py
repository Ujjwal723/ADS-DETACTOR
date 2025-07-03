from flask import Flask, request, jsonify
from flask_cors import CORS
import socket
import requests
from urllib.parse import urlparse
from flask import Flask, request, jsonify
from bs4 import BeautifulSoup
import requests
import re

app = Flask(__name__)
CORS(app)

# Dummy login database
users = {
    "admin": "admin123",
    "police": "inspector123"
}

# In-memory ad storage
ads = []
ad_id_counter = 1

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")
    if users.get(username) == password:
        return jsonify({"status": "success"})
    else:
        return jsonify({"status": "failure"}), 401

@app.route('/ads', methods=['POST'])
def add_ad():
    global ad_id_counter
    data = request.get_json()
    data['id'] = ad_id_counter
    data['flagged'] = False
    ads.append(data)
    ad_id_counter += 1
    return jsonify({"status": "ad added"}), 200

@app.route('/ads', methods=['GET'])
def get_ads():
    return jsonify(ads)
@app.route('/extract_phone', methods=['POST'])
def extract_phone():
    data = request.get_json()
    url = data.get('url')

    try:
        response = requests.get(url, timeout=10)
        soup = BeautifulSoup(response.text, 'html.parser')
        text = soup.get_text()

        phones = re.findall(r'(?:(?:\+91[\-\s]?)?[6-9]\d{9})', text)

        return jsonify({"phones": phones})
    except Exception as e:
        return jsonify({"error": str(e)}), 400
# ✅ Trace IP + Geolocation info from URL
@app.route('/trace', methods=['POST'])
def trace_url():
    data = request.get_json()
    input_url = data.get('url')

    try:
        parsed_url = urlparse(input_url)
        hostname = parsed_url.netloc or parsed_url.path
        ip_address = socket.gethostbyname(hostname)

        geo = requests.get(f"https://ipinfo.io/{ip_address}/json").json()

        return jsonify({
            "host": hostname,
            "ip": geo.get("ip"),
            "country": geo.get("country"),
            "region": geo.get("region"),
            "city": geo.get("city"),
            "org": geo.get("org")
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 400


if __name__ == '__main__':
    app.run(debug=True)

