# auto_news_genie/app.py

from flask import Flask, render_template
from utils.fetch_news import get_latest_news
import os

app = Flask(__name__)

@app.route('/')
def homepage():
    news_items = get_latest_news()
    return render_template('index.html', news=news_items)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    app.run(debug=False, port=port)
