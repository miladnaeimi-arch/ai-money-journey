import json


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


with open("leads.json", "r") as file:
    leads = json.load(file)


for lead in leads:
    score = score_lead(lead)
    print(f"{lead['name']} scored {score}")