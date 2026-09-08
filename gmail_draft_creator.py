import os
import csv
import base64

from email.message import EmailMessage

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build


SCOPES = ["https://www.googleapis.com/auth/gmail.compose"]

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

created_count = 0

with open("email_drafts.csv", "r") as file:
    reader = csv.DictReader(file)

    for draft_data in reader:
        message = EmailMessage()

        message["To"] = draft_data["to"]
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

        print("Gmail draft created successfully!")
        print("Draft ID:", draft["id"])
        print("Recipient:", draft_data["to"])
        print("-" * 50)

print(f"Total drafts created: {created_count}")