# AI Frontier Research Agent 🤖
**An autonomous AI agent pipeline that tracks frontier AI labs daily and generates investment-grade research briefs — powered by Claude API.**

## 🚀 Why This Exists
AI breakthroughs at Anthropic, OpenAI, Google DeepMind, and Meta move markets every day. Investors need real-time intelligence to act on these developments. This project automates that research process using a 3-agent AI pipeline that scrapes, analyzes, and summarizes AI news into professional investment briefs — the way a junior analyst would, but autonomously.

## 🧠 How It Works
**Agent 1 — Scraper** 🕷️
Visits Anthropic, OpenAI, TechCrunch AI, and The Verge daily. Collects latest headlines and saves to raw_articles.json
**Agent 2 — Summarizer** 🔍
Sends each headline to Claude API. Returns structured JSON with summary, company tag, sentiment, and market impact rating.
**Agent 3 — Report Generator** 📝
Synthesizes all summaries into a professional daily research brief with Executive Summary, Breakthrough Alerts, Market Implications, and Watch List.

## 📊 Sample Report Output
**Executive Summary**
OpenAI released GPT-5 with significant reasoning improvements, representing a potential inflection point for enterprise AI adoption...
**Breakthrough Alerts**
🚨 HIGH IMPACT — Anthropic Claude 4 demonstrates 40% improvement in coding benchmarks
**Market Implications**
Short-term bullish for NVIDIA supply chain. Potential pressure on legacy software vendors.

## 🛠 Tech Stack
Python · Anthropic Claude API · LangChain · BeautifulSoup4 · FAISS · Streamlit

## ▶️ Run It
git clone https://github.com/kothapalli-coder/ai-frontier-research-agent
pip install -r requirements.txt
Add ANTHROPIC_API_KEY to .env
python main.py

## 📁 Project Structure
.claude/settings.json — Claude Code configuration
agents/scraper_agent.py — Web scraping agent
agents/summarizer_agent.py — Claude-powered summarizer
agents/report_agent.py — Research brief generator
dashboard/app.py — Streamlit dashboard
CLAUDE.md — Full agent documentation
main.py — Pipeline orchestrator

## 🎯 Planned Improvements
Add arXiv and SEC filing sources
Vector memory for historical research
Automated daily scheduling
Stock price correlation analysis

## 👩‍💻 Author
Jeeshitha Kothapalli
MS Data Science — University of Texas at Arlington