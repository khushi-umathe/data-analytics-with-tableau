import os
from flask import Flask, render_template

app = Flask(__name__)

TABLEAU_DASHBOARD_URL = "https://public.tableau.com/views/analysisoffoodconsumerbehaviour/Dashboard1"

@app.route('/')
def home():
    """Renders the main page with embedded Tableau Dashboard."""
    return render_template('index.html', tableau_url=TABLEAU_DASHBOARD_URL)

if __name__ == '__main__':
    # Automatically binds to cloud platform assigned PORT, or defaults to 5000 locally
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)