import csv
import os
import json
from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

results = []
high_priority_leads = []
with open("leads.csv", "r") as file:
    reader = csv.DictReader(file)

    for lead in reader:
        prompt = f"""
Analyze this sales lead:

Name: {lead['name']}
Budget: ${lead['budget']}
Company size: {lead['company_size']} employees
Urgent: {lead['urgent']}

Return ONLY valid JSON in exactly this format:

{{
  "priority": "HIGH, MEDIUM, or LOW",
  "reason": "one short sentence",
  "next_action": "one short sentence"
}}

Do not include markdown or any text outside the JSON.

"""

    
        try:
            analysis = json.loads(interaction.output_text)
        except json.JSONDecodeError:
            print(f"⚠️ Could not parse AI response for {lead['name']}")
            analysis = {
                "priority": "UNKNOWN",
                "reason": "AI response could not be parsed.",
                "next_action": "Review this lead manually."
            }
            

        
        if analysis["priority"] == "HIGH":
            print(f"🔥 SALES ALERT: Contact {lead['name']} immediately!")
            
            high_priority_leads.append({
                "name": lead["name"],
                "budget": lead["budget"],
                "company_size": lead["company_size"],
                "urgent": lead["urgent"],
                "reason": analysis["reason"],
                "next_action": analysis["next_action"]
            })

        elif analysis["priority"] == "MEDIUM":
            print(f"📧 FOLLOW UP: Contact {lead['name']} this week.")

        else:
            print(f"📝 LOW PRIORITY: Add {lead['name']} to the nurture list.")
        results.append({
            "name": lead["name"],
            "budget": lead["budget"],
            "company_size": lead["company_size"],
            "urgent": lead["urgent"],
            "priority": analysis["priority"],
            "reason": analysis["reason"],
            "next_action": analysis["next_action"]
        })

        print(f"\nLead: {lead['name']}")
        print(interaction.output_text)
        print("-" * 50)
        

with open("ai_analyzed_leads.csv", "w", newline="") as file:
    fieldnames = [
    "name",
    "budget",
    "company_size",
    "urgent",
    "priority",
    "reason",
    "next_action"
]

    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(results)

print("AI analysis saved to ai_analyzed_leads.csv")
with open("high_priority_leads.csv", "w", newline="") as file:
    fieldnames = [
        "name",
        "budget",
        "company_size",
        "urgent",
        "reason",
        "next_action"
    ]

    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(high_priority_leads)

print("High priority leads saved to high_priority_leads.csv")