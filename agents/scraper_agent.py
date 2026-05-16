import requests
from bs4 import BeautifulSoup
import json
import datetime

SOURCES = [
    {
        "name": "Anthropic",
        "url": "https://www.anthropic.com/news",
        "company": "Anthropic"
    },
    {
        "name": "OpenAI",
        "url": "https://openai.com/news",
        "company": "OpenAI"
    },
    {
        "name": "TechCrunch AI",
        "url": "https://techcrunch.com/tag/artificial-intelligence/",
        "company": "General"
    },
    {
        "name": "The Verge AI",
        "url": "https://www.theverge.com/ai-artificial-intelligence",
        "company": "General"
    }
]

def scrape_articles():
    articles = []
    headers = {"User-Agent": "Mozilla/5.0"}

    for source in SOURCES:
        try:
            response = requests.get(source["url"], headers=headers, timeout=10)
            soup = BeautifulSoup(response.text, "html.parser")

            # Get all links and text
            links = soup.find_all("a", href=True)
            for link in links[:10]:  # top 10 links per source
                text = link.get_text(strip=True)
                href = link["href"]
                if len(text) > 30:  # filter out short nav links
                    articles.append({
                        "title": text,
                        "url": href,
                        "company": source["company"],
                        "source": source["name"],
                        "scraped_at": str(datetime.datetime.now())
                    })

            print(f"✅ Scraped {source['name']}")

        except Exception as e:
            print(f"❌ Failed {source['name']}: {e}")

    # Save to data folder
    with open("data/raw_articles.json", "w") as f:
        json.dump(articles, f, indent=2)