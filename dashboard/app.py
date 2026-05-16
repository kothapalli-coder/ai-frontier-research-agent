import streamlit as st
import json
import os
import sys

# Add parent directory to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

st.set_page_config(
    page_title="AI Frontier Research Agent",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 AI Frontier Research Agent")
st.subheader("Daily Investment Research Brief")
st.divider()

# Run Pipeline Button
if st.button("🚀 Run Pipeline Now", type="primary"):
    with st.spinner("Running agents..."):
        from agents.scraper_agent import scrape_articles
        from agents.summarizer_agent import summarize_articles
        from agents.report_agent import generate_report
        scrape_articles()
        summarize_articles()
        generate_report()
    st.success("✅ Pipeline complete!")
    st.rerun()

st.divider()

col1, col2 = st.columns(2)

# Load summaries
with col1:
    st.subheader("📊 Today's AI News Summaries")
    try:
        with open("data/summaries.json", "r") as f:
            summaries = json.load(f)

        if summaries:
            for item in summaries:
                sentiment_color = {
                    "breakthrough": "🟢",
                    "positive": "🔵",
                    "neutral": "⚪",
                    "negative": "🔴"
                }.get(item.get("sentiment", "").lower(), "⚪")

                impact_color = {
                    "high": "🔴",
                    "medium": "🟡",
                    "low": "🟢"
                }.get(item.get("market_impact", "").lower(), "⚪")

                with st.expander(f"{sentiment_color} {item.get('title', 'No title')[:60]}..."):
                    st.write(f"**Summary:** {item.get('summary', 'N/A')}")
                    st.write(f"**Company:** {item.get('company', 'N/A')}")
                    st.write(f"**Sentiment:** {item.get('sentiment', 'N/A')}")
                    st.write(f"**Market Impact:** {impact_color} {item.get('market_impact', 'N/A')}")
        else:
            st.info("No summaries yet. Click Run Pipeline!")

    except FileNotFoundError:
        st.info("No data yet. Click Run Pipeline to start!")

# Sentiment Chart
with col2:
    st.subheader("📈 Sentiment Breakdown")
    try:
        with open("data/summaries.json", "r") as f:
            summaries = json.load(f)

        if summaries:
            sentiment_counts = {}
            for item in summaries:
                s = item.get("sentiment", "unknown").lower()
                sentiment_counts[s] = sentiment_counts.get(s, 0) + 1

            import pandas as pd
            df = pd.DataFrame(
                list(sentiment_counts.items()),
                columns=["Sentiment", "Count"]
            )
            st.bar_chart(df.set_index("Sentiment"))
        else:
            st.info("No data yet!")

    except FileNotFoundError:
        st.info("No data yet. Click Run Pipeline!")

st.divider()

# Full Report
st.subheader("📝 Full Research Brief")
try:
    with open("data/daily_report.md", "r", encoding="utf-8") as f:
        report = f.read()
    st.markdown(report)

    # Download Button
    st.download_button(
        label="📥 Download Report",
        data=report,
        file_name="ai_research_brief.md",
        mime="text/markdown"
    )

except FileNotFoundError:
    st.info("No report yet. Click Run Pipeline to generate!")

st.divider()
st.caption("Built by Jeeshitha Kothapalli | MS Data Science, UT Arlington | Powered by Claude API")