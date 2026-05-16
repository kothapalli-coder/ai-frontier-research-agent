import anthropic
import json
import os
import datetime
from dotenv import load_dotenv

load_dotenv()

client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

def generate_report():
    # Load summaries
    with open("data/summaries.json", "r") as f:
        summaries = json.load(f)

    summaries_text = json.dumps(summaries, indent=2)

    prompt = f"""You are a senior AI investment research analyst at a hedge fund.

Based on these AI news summaries from today, generate a professional daily research brief:

{summaries_text}

Your report should include:
1. Executive Summary (3-4 sentences)
2. Key Developments by Company
3. Breakthrough Alerts (if any high impact items)
4. Market Implications
5. Watch List for Tomorrow

Format as a clean markdown report. Be concise and investment-focused."""

    response = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=1000,
        messages=[{"role": "user", "content": prompt}]
    )

    report = response.content[0].text

    # Save report
    date = datetime.datetime.now().strftime("%Y-%m-%d")
    with open(f"data/daily_report_{date}.md", "w", encoding="utf-8") as f:
        f.write(report)

    with open("data/daily_report.md", "w", encoding="utf-8") as f:
        f.write(report)

    print("✅ Report generated!")
    print(report)
    return report

if __name__ == "__main__":
    generate_report()