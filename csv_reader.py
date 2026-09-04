import csv

def score_lead(budget, company_size, urgent):
    score = 0

    if budget >= 10000:
        score = score + 3
    elif budget >= 5000:
        score = score + 2
    else:
        score = score + 1

    if company_size >= 50:
        score = score + 3
    elif company_size >= 10:
        score = score + 2
    else:
        score = score + 1

    if urgent == "yes":
        score = score + 2

    return score


with open("leads.csv", "r") as input_file:
    reader = csv.DictReader(input_file)

    with open("scored_leads.csv", "w", newline="") as output_file:
        fieldnames = ["name", "budget", "company_size", "urgent", "score"]

        writer = csv.DictWriter(output_file, fieldnames=fieldnames)
        writer.writeheader()

        for lead in reader:
            name = lead["name"]
            budget = int(lead["budget"])
            company_size = int(lead["company_size"])
            urgent = lead["urgent"]

            score = score_lead(budget, company_size, urgent)

            writer.writerow({
                "name": name,
                "budget": budget,
                "company_size": company_size,
                "urgent": urgent,
                "score": score
            })

            print(f"{name} scored {score}")