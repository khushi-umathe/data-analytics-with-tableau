# Food Consumer Behavior Analytics Portal

A full-stack analytical web application built with Python Flask, HTML5/CSS3, and Tableau Public. The portal visualizes interactive consumer behavior metrics across 50,000 transaction records to deliver actionable marketing and inventory strategy insights.

- **Live Application URL**: https://food-consumer-analytics.onrender.com
- **GitHub Repository**: https://github.com/khushi-umathe/food-consumer-analytics

---

## 📌 Project Overview

Understanding consumer purchasing patterns across demographic segments is critical for retail and food distribution strategy. This portal bridges raw data processing and interactive executive reporting by integrating a 3x3 custom Tableau Public dashboard grid inside a Flask web application deployed to Render.com.

### Key Highlights
- **Dataset Scale**: Analyzed 50,000 retail food transaction records.
- **Calculated Fields**: Configured custom dynamic segmentation logic including dynamic age groups, spend brackets, and cross-category preference indices.
- **Interactive Tableau Dashboard**: Features a 3x3 layout with real-time filtering across age, location, item preference, and feedback ratings.
- **Cloud Architecture**: Deployed as a web service running Python 3 and Gunicorn on Render's cloud infrastructure.

---

## 🛠 Tech Stack & Dependencies

- **Frontend**: HTML5, CSS3, JavaScript, Tableau JavaScript API / Embed Script
- **Backend Framework**: Python 3.x, Flask 3.0.2
- **WSGI Production Server**: Gunicorn 21.2.0
- **Data Visualization**: Tableau Public Desktop / Web Authoring
- **Version Control & Hosting**: Git, GitHub, Render Web Services

---

## 📁 Repository Structure

```text
food-consumer-analytics/
│
├── app.py                 # Core Flask application route definitions
├── Procfile               # Deployment entry point for Gunicorn WSGI server
├── requirements.txt       # Production Python dependencies
├── README.md              # Project documentation
│
└── templates/
    └── index.html         # Responsive web UI embedding Tableau dashboard
