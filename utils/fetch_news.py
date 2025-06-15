# auto_news_genie/utils/fetch_news.py

import feedparser

def get_latest_news():
    feeds = [
        "http://feeds.bbci.co.uk/news/rss.xml",
        "https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml",
        "https://www.thehindu.com/news/national/feeder/default.rss"
    ]

    news_items = []

    for feed_url in feeds:
        try:
            parsed_feed = feedparser.parse(feed_url)
            for entry in parsed_feed.entries[:5]:  # Top 5 from each source
                news_items.append({
                    'title': entry.get('title', ''),
                    'link': entry.get('link', ''),
                    'summary': entry.get('summary', '')[:200] + '...',
                    'source': parsed_feed.feed.get('title', 'Unknown Source')
                })
        except Exception as e:
            print(f"Failed to fetch from {feed_url}: {e}")

    return news_items
