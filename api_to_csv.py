import requests
import csv

url = "https://jsonplaceholder.typicode.com/users"

response = requests.get(url)
data = response.json()

with open("api_users.csv", "w", newline="") as file:
    fieldnames = ["name", "email", "city", "company"]

    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()

    for user in data:
        writer.writerow({
            "name": user["name"],
            "email": user["email"],
            "city": user["address"]["city"],
            "company": user["company"]["name"]
        })

print("API data saved to api_users.csv")