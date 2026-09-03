leads = [
    {
        "name": "Alex",
        "budget": 12000,
        "company_size": 60,
        "urgent": True
    },
    {
        "name": "Sara",
        "budget": 6000,
        "company_size": 20,
        "urgent": False
    },
    {
        "name": "John",
        "budget": 2000,
        "company_size": 5,
        "urgent": True
    }
]
def score_lead(lead):
    score = 0

    if lead["budget"] >= 10000:
        score = score + 3
    elif lead["budget"] >= 5000:
        score = score + 2
    else:
        score = score + 1

    if lead["company_size"] >= 50:
        score = score + 3
    elif lead["company_size"] >= 10:
        score = score + 2
    else:
        score = score + 1

    if lead["urgent"] == True:
        score = score + 2

    return score

for lead in leads:
    score = score_lead(lead)
    print(f"Lead: {lead['name']}, Score: {score}")