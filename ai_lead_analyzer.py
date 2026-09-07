import csv
import os
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

Return your answer in exactly this format:

Priority: HIGH, MEDIUM, or LOW
Reason: one short sentence
Next Action: one short sentence
"""

        interaction = client.interactions.create(
            model="gemini-3.5-flash-lite",
            input=prompt
        )

        results.append({
            "name": lead["name"],
            "budget": lead["budget"],
            "company_size": lead["company_size"],
            "urgent": lead["urgent"],
            "ai_analysis": interaction.output_text
        })

        print(f"\nLead: {lead['name']}")
        print(interaction.output_text)
        print("-" * 50)

with open("ai_analyzed_leads.csv", "w", newline="") as file:
    fieldnames = ["name", "budget", "company_size", "urgent", "ai_analysis"]

    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(results)

print("AI analysis saved to ai_analyzed_leads.csv")