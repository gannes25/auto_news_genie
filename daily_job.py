# auto_news_genie/daily_job.py

import json
import os
import sys

# Add current directory to path for utils
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from utils.fetch_news import get_latest_news

def save_daily_news():
    news = get_latest_news()
    with open('latest_news.json', 'w') as f:
        json.dump(news, f, indent=2)
    print("🗞️ Daily news saved to latest_news.json")

if __name__ == '__main__':
    save_daily_news()
