import requests

url = "https://jsonplaceholder.typicode.com/users"

response = requests.get(url)

print(response.status_code)
data = response.json()

for user in data:
    print(f"Name: {user['name']}")
    print(f"Email: {user['email']}")
    print("-----")