import os
import csv
import json
from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

results = []

with open("follow_up_leads.csv", "r") as file:
    reader = csv.DictReader(file)

    for lead in reader:
        print(lead)

        prompt = f"""
Write a short professional follow-up email for this sales lead.

Name: {lead['name']}
Budget: ${lead['budget']}
Company size: {lead['company_size']} employees
Reason: {lead['reason']}
Recommended next action: {lead['next_action']}

Return ONLY valid JSON in exactly this format:

{{
  "subject": "short email subject",
  "body": "short professional email body"
}}

Do not include markdown or any text outside the JSON.
"""

        interaction = client.interactions.create(
            model="gemini-3.5-flash-lite",
            input=prompt
        )

        email_data = json.loads(interaction.output_text)

        print(interaction.output_text)
        print("-" * 50)

        results.append({
            "name": lead["name"],
            "budget": lead["budget"],
            "company_size": lead["company_size"],
            "subject": email_data["subject"],
            "body": email_data["body"]
        })

with open("generated_follow_up_emails.csv", "w", newline="") as file:
    fieldnames = ["name", "budget", "company_size", "subject", "body"]

    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(results)

print("Follow-up emails saved to generated_follow_up_emails.csv")