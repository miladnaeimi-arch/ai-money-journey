import os
import csv
import base64

from email.message import EmailMessage

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build


SCOPES = ["https://www.googleapis.com/auth/gmail.compose"]
PROCESSED_FILE = "processed_drafts.csv"

creds = None

if os.path.exists("token.json"):
    creds = Credentials.from_authorized_user_file(
        "token.json",
        SCOPES
    )

if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
    else:
        flow = InstalledAppFlow.from_client_secrets_file(
            "credentials.json",
            SCOPES
        )
        creds = flow.run_local_server(port=0)

    with open("token.json", "w") as token:
        token.write(creds.to_json())


service = build("gmail", "v1", credentials=creds)

processed_emails = set()

if os.path.exists(PROCESSED_FILE):
    with open(PROCESSED_FILE, "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            if row.get("email"):
                processed_emails.add(row["email"])


created_count = 0
skipped_count = 0

with open("email_drafts.csv", "r") as file:
    reader = csv.DictReader(file)

    for draft_data in reader:
        email = draft_data["to"]

        if email in processed_emails:
            print("Skipping duplicate draft:")
            print("Recipient:", email)
            print("Subject:", draft_data["subject"])
            print("-" * 50)

            skipped_count += 1
            continue

        message = EmailMessage()

        message["To"] = email
        message["Subject"] = draft_data["subject"]
        message.set_content(draft_data["body"])

        encoded_message = base64.urlsafe_b64encode(
            message.as_bytes()
        ).decode()

        create_message = {
            "message": {
                "raw": encoded_message
            }
        }

        draft = service.users().drafts().create(
            userId="me",
            body=create_message
        ).execute()

        created_count += 1
        processed_emails.add(email)

        with open(PROCESSED_FILE, "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([email])

        print("Gmail draft created successfully!")
        print("Draft ID:", draft["id"])
        print("Recipient:", email)
        print("-" * 50)

print(f"Total drafts created: {created_count}")
print(f"Total duplicates skipped: {skipped_count}")