# auto_news_genie/utils/fetch_news.py

import feedparser

RSS_FEEDS = [
    'https://feeds.bbci.co.uk/news/rss.xml',
    'https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml',
    'https://www.thehindu.com/news/national/feeder/default.rss'
]

def get_latest_news():
    news_items = []
    for url in RSS_FEEDS:
        feed = feedparser.parse(url)
        for entry in feed.entries[:5]:
            news_items.append({
                'title': entry.title,
                'summary': entry.get('summary', '')[:200],
                'link': entry.link,
                'image': entry.get('media_content', [{'url': ''}])[0]['url'] if entry.get('media_content') else '',
                'source': feed.feed.title
            })
    return news_items
