import anthropic
import json
import os
from dotenv import load_dotenv

load_dotenv()

client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

def summarize_articles():
    # Load raw articles
    with open("data/raw_articles.json", "r") as f:
        articles = json.load(f)

    summaries = []

    for article in articles[:15]:  # summarize top 15
        try:
            prompt = f"""You are an AI investment research analyst.
            
Analyze this AI news headline and provide:
1. A 2-sentence summary
2. Company tag (Anthropic/OpenAI/Google/Meta/xAI/General)
3. Sentiment (breakthrough/positive/neutral/negative)
4. Potential market impact (high/medium/low)

Headline: {article['title']}
Source: {article['source']}

Respond in JSON format only:
{{
  "summary": "...",
  "company": "...",
  "sentiment": "...",
  "market_impact": "...",
  "title": "{article['title']}"
}}"""

            response = client.messages.create(
                model="claude-sonnet-4-20250514",
                max_tokens=300,
                messages=[{"role": "user", "content": prompt}]
            )

            raw = response.content[0].text.strip()
            # Clean response if wrapped in markdown
            if "```json" in raw:
                raw = raw.split("```json")[1].split("```")[0].strip()
            elif "```" in raw:
                raw = raw.split("```")[1].split("```")[0].strip()

            result = json.loads(raw)
            summaries.append(result)
            print(f"✅ Summarized: {article['title'][:50]}...")

        except Exception as e:
            print(f"❌ Failed: {e}")

    # Save summaries
    with open("data/summaries.json", "w") as f:
        json.dump(summaries, f, indent=2)

    print(f"\n📦 Saved {len(summaries)} summaries")
    return summaries

if __name__ == "__main__":
    summarize_articles()