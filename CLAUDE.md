# AI Frontier Research Agent

## Project Overview
An autonomous multi-agent system that monitors frontier AI labs 
(Anthropic, OpenAI, Google DeepMind, Meta, xAI) and generates 
daily investment-grade research briefs for AI/tech equity analysis.

## Why This Exists
AI is reshaping every industry. Investors need real-time intelligence 
on AI breakthroughs, model releases, and capability jumps to make 
informed decisions on AI infrastructure stocks.

## Agent Architecture

### Agent 1 — Scraper Agent (scraper_agent.py)
- Scrapes latest news from AI lab blogs and tech news sources
- Sources: Anthropic, OpenAI, Google DeepMind, The Verge, TechCrunch
- Output: Raw articles saved to data/raw_articles.json

### Agent 2 — Summarizer Agent (summarizer_agent.py)
- Takes raw articles as input
- Uses Claude API to summarize each article
- Tags by company and sentiment (breakthrough/positive/negative/neutral)
- Output: Structured summaries saved to data/summaries.json

### Agent 3 — Report Agent (report_agent.py)
- Takes summaries as input
- Uses Claude API to generate a daily research brief
- Highlights key developments and potential market impact
- Output: Markdown report saved to data/daily_report.md

## How To Run
1. Set your API key: `export ANTHROPIC_API_KEY=your_key`
2. Run the pipeline: `python main.py`
3. View dashboard: `streamlit run dashboard/app.py`

## Tech Stack
- Python, Anthropic Claude API, LangChain
- BeautifulSoup4 for scraping
- FAISS for vector storage
- Streamlit for dashboard