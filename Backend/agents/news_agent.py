import feedparser
import requests

def fetch_top_news(limit=5):
    """
    Fetches the latest national news headlines using Google News RSS.
    """
    print("Scout Agent: Looking for the latest global news...")
    
    # URL for Google News India (National Politics)
    url = "https://news.google.com/rss/headlines/section/topic/NATION?hl=en-IN&gl=IN&ceid=IN:en"
    
    # The Disguise: Tell Google we are a normal web browser, not a bot!
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    
    try:
        # 1. Fetch the raw XML data using our disguise
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status() # This will catch 403 Forbidden or 404 Not Found errors
        
        # 2. Hand the raw text over to feedparser
        feed = feedparser.parse(response.content)
        
        news_items = []
        
        # 3. Extract the stories
        for entry in feed.entries[:limit]:
            story = {
                "title": entry.title,
                "link": entry.link,
                # Sometimes published dates are missing, this safely grabs them
                "published": getattr(entry, 'published', 'Just now') 
            }
            news_items.append(story)
            
        return news_items
        
    except Exception as e:
        print(f"Scout Agent Error: {e}")
        return []

# --- TEST BLOCK ---
# This block only runs if we execute this specific file directly.
if __name__ == "__main__":
    top_stories = fetch_top_news(limit=3)
    
    print("\n--- TOP STORIES FOUND ---")
    if top_stories:
        for i, story in enumerate(top_stories, 1):
            print(f"{i}. {story['title']}")
            print(f"   Published: {story['published']}\n")
    else:
        print("The Scout failed to find any stories. Check your internet or headers!")