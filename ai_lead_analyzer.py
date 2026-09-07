import csv
import os
import json
from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

results = []

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

        interaction = client.interactions.create(
            model="gemini-3.5-flash-lite",
            input=prompt
        )
        analysis = json.loads(interaction.output_text)

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
print(analysis["priority"])
print(analysis["reason"])
print(analysis["next_action"])