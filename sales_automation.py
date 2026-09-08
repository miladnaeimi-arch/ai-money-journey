import subprocess
import sys

print("Starting AI Sales Automation...")

step1 = subprocess.run(["python", "ai_lead_analyzer.py"])

if step1.returncode != 0:
    print("Step 1 failed: Lead analysis stopped.")
    sys.exit(1)

print("Step 1 complete: Lead analysis finished.")

step2 = subprocess.run(["python", "follow_up_generator.py"])

if step2.returncode != 0:
    print("Step 2 failed: Follow-up generation stopped.")
    sys.exit(1)

print("Step 2 complete: Follow-up emails generated.")

step3 = subprocess.run(["python", "email_draft_creator.py"])

if step3.returncode != 0:
    print("Step 3 failed: Email draft creation stopped.")
    sys.exit(1)

print("Step 3 complete: Email drafts prepared.")

step4 = subprocess.run(["python", "gmail_draft_creator.py"])

if step4.returncode != 0:
    print("Step 4 failed: Gmail draft creation stopped.")
    sys.exit(1)

print("Step 4 complete: Gmail drafts created.")

print("AI Sales Automation complete!")