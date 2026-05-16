import requests
from bs4 import BeautifulSoup
import json
import datetime

SOURCES = [
    {
        "name": "TechCrunch AI",
        "url": "https://techcrunch.com/category/artificial-intelligence/",
        "company": "General",
        "tag": "h2"
    },
    {
        "name": "The Verge AI",
        "url": "https://www.theverge.com/ai-artificial-intelligence",
        "company": "General",
        "tag": "h2"
    },
    {
        "name": "VentureBeat AI",
        "url": "https://venturebeat.com/category/ai/",
        "company": "General",
        "tag": "h2"
    },
    {
        "name": "MIT Tech Review AI",
        "url": "https://www.technologyreview.com/topic/artificial-intelligence/",
        "company": "General",
        "tag": "h3"
    }
]

def scrape_articles():
    articles = []
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }

    for source in SOURCES:
        try:
            response = requests.get(source["url"], headers=headers, timeout=10)
            soup = BeautifulSoup(response.text, "html.parser")

            # Get headlines from h2 and h3 tags
            headlines = soup.find_all(["h2", "h3"])
            
            count = 0
            for headline in headlines:
                text = headline.get_text(strip=True)
                # Filter for real headlines — must be longer than 20 chars
                # and not contain common nav words
                nav_words = ["menu", "navigation", "logo", "home", "search", 
                           "subscribe", "sign in", "log in", "cookie"]
                
                if (len(text) > 20 and 
                    not any(word in text.lower() for word in nav_words) and
                    count < 8):
                    
                    articles.append({
                        "title": text,
                        "company": source["company"],
                        "source": source["name"],
                        "scraped_at": str(datetime.datetime.now())
                    })
                    count += 1

            print(f"✅ Scraped {count} articles from {source['name']}")

        except Exception as e:
            print(f"❌ Failed {source['name']}: {e}")

    # Save to data folder
    with open("data/raw_articles.json", "w", encoding="utf-8") as f:
        json.dump(articles, f, indent=2)

    print(f"\n📦 Total: {len(articles)} articles saved")
    return articles

if __name__ == "__main__":
    scrape_articles()