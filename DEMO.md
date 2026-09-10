# AI Sales Automation Demo

## Demo Goal

Show how a business can turn raw leads into prioritized opportunities and ready-to-review Gmail drafts using AI and automation.

## Demo Flow

### 1. Start With Raw Leads

Open `leads.csv`.

Explain that the system receives basic lead information such as:

- name
- budget
- company size
- urgency
- email

### 2. Run the Full Automation

Run:

    python sales_automation.py

Explain that one command starts the entire workflow.

### 3. Show AI Lead Analysis

Open `ai_analyzed_leads.csv`.

Highlight that the AI generates:

- priority
- reason
- recommended next action

Show examples of HIGH, MEDIUM, and LOW leads.

### 4. Show AI Follow-Up Generation

Open `generated_follow_up_emails.csv`.

Explain that MEDIUM-priority leads automatically receive personalized follow-up drafts based only on the available lead data.

### 5. Show Prepared Email Drafts

Open `email_drafts.csv`.

Show the final:

- recipient
- subject
- email body

### 6. Show Gmail Drafts

Open Gmail Drafts.

Show that the system created real drafts automatically.

Important: the system creates drafts only and does not automatically send emails.

### 7. Demonstrate Duplicate Protection

Run the automation a second time:

    python sales_automation.py

Show:

    Total drafts created: 0
    Total duplicates skipped: 2

Explain that the system prevents duplicate Gmail drafts when the workflow is run again.

## Business Value

This automation can help a sales team:

- review leads faster
- prioritize better opportunities
- reduce repetitive email writing
- prepare follow-ups automatically
- avoid duplicate outreach
- keep a human review step before sending

## Demo Summary

Raw leads → AI qualification → lead routing → personalized follow-up → Gmail drafts → duplicate protection
