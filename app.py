# auto_news_genie/app.py

from flask import Flask, render_template
import os
import json

# If utils isn't recognized as a package
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from utils.fetch_news import get_latest_news

app = Flask(__name__)

@app.route('/')
def home():
    # Try loading news from file written by daily_job.py
    news = []
    try:
        with open('latest_news.json', 'r') as f:
            news = json.load(f)
    except Exception as e:
        print("Error loading news:", e)
        # Fallback: fetch fresh news
        news = get_latest_news()

    return render_template('index.html', news_items=news)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
