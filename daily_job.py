# auto_news_genie/daily_job.py

from utils.fetch_news import get_latest_news
import json

# This is a simulated daily update job. In a real use-case,
# you'd store this data in a database or generate static HTML.

def run_daily_update():
    news_items = get_latest_news()
    with open('latest_news.json', 'w', encoding='utf-8') as f:
        json.dump(news_items, f, ensure_ascii=False, indent=2)
    print("✅ Daily news updated successfully!")

if __name__ == '__main__':
    run_daily_update()
