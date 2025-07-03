/frontend
├── index.html           # Web UI
├── css/
│   └── style.css        # Optional custom styles
├── js/
│   └── main.js          # JavaScript for login, API calls
├── images/
│   └── police-logo.png  # Haryana Police logo


/server
│
├── app.py               # Main Flask app
├── static/              # JS/CSS/Images
│   └── script.js        # JavaScript code (if separated)
├── templates/           # Optional: if using Jinja HTML rendering
│
├── utils/
│   ├── ip_lookup.py     # IP + geo lookup logic
│   ├── whois_info.py    # WHOIS extraction logic
│   └── phone_lookup.py  # Phone search logic (if supported)
