import feedparser

def fetch_top_news(limit=5):
    """
    Fetches the latest world news headlines using Google News RSS.
    """
    print("Scout Agent: Looking for the latest global news...")
    
    # URL for Google News World section
    # URL for Google News India (National Politics)
    url = "https://news.google.com/rss/headlines/section/topic/NATION?hl=en-IN&gl=IN&ceid=IN:en"
    
    # Parse the feed from the URL
    feed = feedparser.parse(url)
    
    news_items = []
    
    # Loop through the feed and grab the top stories up to our limit
    for entry in feed.entries[:limit]:
        story = {
            "title": entry.title,
            "link": entry.link,
            "published": entry.published
        }
        news_items.append(story)
        
    return news_items

# --- TEST BLOCK ---
# This block only runs if we execute this specific file directly.
# It's a great way to test our agent in isolation!
if __name__ == "__main__":
    top_stories = fetch_top_news(limit=3)
    
    print("\n--- TOP STORIES FOUND ---")
    for i, story in enumerate(top_stories, 1):
        print(f"{i}. {story['title']}")
        print(f"   Published: {story['published']}\n")