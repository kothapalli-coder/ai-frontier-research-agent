from agents.scraper_agent import scrape_articles
from agents.summarizer_agent import summarize_articles
from agents.report_agent import generate_report

print("🚀 Starting AI Frontier Research Agent...\n")

print("📡 Step 1: Scraping AI news...")
scrape_articles()

print("\n🧠 Step 2: Summarizing with Claude...")
summarize_articles()

print("\n📝 Step 3: Generating research brief...")
generate_report()

print("\n✅ Done! Check data/daily_report.md for your report.")