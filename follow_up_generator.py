import os
import csv
import json
import sys

from dotenv import load_dotenv
from google import genai


load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

results = []
failed_count = 0

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
Do not use placeholders such as [Your Name], [Your Company], or [Company Name].
End the email with "Best regards," only, without adding a sender name or title.
Do not invent previous conversations, meetings, attachments, case studies, customer results, or company details that were not provided in the lead data.
Only use facts provided in the lead data.
If information is unknown, keep the email general instead of making assumptions.
"""
        try:
            interaction = client.interactions.create(
                model="gemini-3.5-flash-lite",
                input=prompt
            )

            email_data = json.loads(interaction.output_text)

            print(interaction.output_text)
            print("-" * 50)

            results.append({
                "name": lead["name"],
                "email": lead["email"],
                "budget": lead["budget"],
                "company_size": lead["company_size"],
                "subject": email_data["subject"],
                "body": email_data["body"]
            })

        except json.JSONDecodeError:
            print("Invalid JSON from Gemini.")
            print("Skipping lead:", lead["name"])
            print("-" * 50)

            failed_count += 1

        except Exception as error:
            print("Gemini API error:")
            print(error)
            print("Skipping lead:", lead["name"])
            print("-" * 50)

            failed_count += 1


with open("generated_follow_up_emails.csv", "w", newline="") as file:
    fieldnames = [
        "name",
        "email",
        "budget",
        "company_size",
        "subject",
        "body"
    ]

    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(results)


print("Follow-up emails saved to generated_follow_up_emails.csv")
print("Successful leads:", len(results))
print("Failed leads:", failed_count)


if failed_count > 0 and len(results) == 0:
    print("ERROR: All follow-up email generations failed.")
    sys.exit(1)