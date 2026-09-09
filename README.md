# AI Sales Automation System

An end-to-end AI-powered sales automation system built with Python, Gemini, and the Gmail API.

The system helps businesses process incoming leads, prioritize sales opportunities, generate personalized follow-up emails, and automatically prepare Gmail drafts for sales teams.

## Business Problem

Sales teams often spend time manually:

- reviewing incoming leads

- deciding which leads deserve attention

- writing follow-up emails

- preparing email drafts

- tracking which leads have already been contacted

This project automates that workflow.

## How It Works

```text

leads.csv

    ↓

AI Lead Analysis

    ↓

HIGH / MEDIUM / LOW Routing

    ↓

AI Follow-Up Generation

    ↓

Email Draft Preparation

    ↓

Duplicate Protection

    ↓

Gmail API

    ↓

Real Gmail Drafts

```

## Key Features

- AI-powered lead qualification

- HIGH / MEDIUM / LOW lead routing

- personalized AI follow-up generation

- structured JSON processing

- automatic email draft preparation

- Gmail API integration

- duplicate draft protection

- API error handling

- invalid JSON handling

- workflow failure detection

- end-to-end automation from one command

## Technology Stack

- Python

- Google Gemini API

- Gmail API

- OAuth 2.0

- CSV / JSON

- Git

- GitHub

## Automation Workflow

### 1. Lead Analysis

The system reads incoming leads and uses Gemini to evaluate:

- budget

- company size

- urgency

Gemini returns:

- priority

- reason

- recommended next action

### 2. Lead Routing

Leads are automatically routed into:

- HIGH — immediate sales attention

- MEDIUM — follow-up workflow

- LOW — nurture workflow

### 3. AI Follow-Up Generation

MEDIUM-priority leads are sent to Gemini to generate personalized:

- email subjects

- email bodies

The output is returned as structured JSON and saved for the next stage.

### 4. Email Draft Preparation

Generated emails are converted into structured email drafts containing:

- recipient

- subject

- body

### 5. Gmail Integration

The Gmail API automatically creates real Gmail drafts.

The system creates drafts only — it does not automatically send emails.

### 6. Duplicate Protection

Processed recipients are tracked so repeated workflow runs do not create duplicate Gmail drafts.

### 7. Reliability

The workflow includes protection for:

- invalid AI JSON responses

- Gemini API failures

- individual lead failures

- complete follow-up generation failure

- duplicate Gmail drafts

If a critical workflow step fails, the automation stops instead of incorrectly reporting success.

## Run the Full Automation

The complete workflow can be started with:

```bash

python sales_[automation.py](http://automation.py)

```

## Project Goal

This project demonstrates how AI and automation can reduce repetitive sales work and help businesses respond to leads more efficiently.

It is designed as a practical foundation for customized AI sales automation solutions for real businesses.

## Security

Sensitive credentials are not stored in the repository.

Files such as the following are excluded from Git:

- `.env`

- `credentials.json`

- `token.json`

- `processed_drafts.csv`

## Status

Active development — currently being prepared as a client-ready AI automation demo.

