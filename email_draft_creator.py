import csv

drafts = []

with open("generated_follow_up_emails.csv", "r") as file:
    reader = csv.DictReader(file)

    for email in reader:
        draft = {
            "to": email["email"],
            "subject": email["subject"],
            "body": email["body"]
        }

        drafts.append(draft)

        print(draft)
        print("-" * 50)

with open("email_drafts.csv", "w", newline="") as file:
    fieldnames = ["to", "subject", "body"]

    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(drafts)

print("Email drafts saved to email_drafts.csv")