import requests

url = "https://jsonplaceholder.typicode.com/posts"

data = {
    "title": "My First API Post",
    "body": "I am learning API automation with Python.",
    "userId": 1
}

response = requests.post(url, json=data)

print(response.status_code)
result = response.json()

print(f"Created post ID: {result['id']}")
print(f"Title: {result['title']}")