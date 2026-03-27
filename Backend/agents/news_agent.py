import feedparser
import requests

def fetch_top_news(limit=5):
    """
    Fetches the latest national news headlines using multiple fallbacks.
    """
    print("Scout Agent: Looking for the latest news...")
    
    # The Scout's hit-list. If one blocks us, it automatically tries the next!
    rss_feeds = [
        "https://timesofindia.indiatimes.com/rssfeeds/-2128936835.cms", # TOI India News
        "https://feeds.feedburner.com/ndtvnews-top-stories",            # NDTV Top Stories
        "https://www.thehindu.com/news/national/feeder/default.rss"     # The Hindu National
    ]
    
    # The Disguise
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    
    for url in rss_feeds:
        try:
            print(f"Scout Agent is knocking on: {url} ...")
            response = requests.get(url, headers=headers, timeout=10)
            response.raise_for_status() # Catch 403s and 503s immediately
            
            # Parse the feed
            feed = feedparser.parse(response.content)
            
            # If the feed is empty, Google/Website might be blocking the content
            if not feed.entries:
                print("Feed was empty, moving to backup...")
                continue 
                
            news_items = []
            
            # Extract the stories
            for entry in feed.entries[:limit]:
                story = {
                    "title": entry.title,
                    "link": entry.link,
                    "published": getattr(entry, 'published', 'Just now') 
                }
                news_items.append(story)
                
            print(f"✅ Scout successfully found {len(news_items)} stories!")
            return news_items # Success! Break out of the loop and return the news.
            
        except Exception as e:
            print(f"⚠️ Scout got blocked by {url}. Error: {e}")
            continue # Try the next backup URL in the list
            
    # If the loop finishes and all feeds failed
    print("❌ Scout Agent Critical Failure: All news sources blocked us.")
    return []

# --- TEST BLOCK ---
if __name__ == "__main__":
    top_stories = fetch_top_news(limit=3)
    
    print("\n--- TOP STORIES FOUND ---")
    if top_stories:
        for i, story in enumerate(top_stories, 1):
            print(f"{i}. {story['title']}")
            print(f"   Published: {story['published']}\n")