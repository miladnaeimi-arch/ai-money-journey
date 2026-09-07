import requests
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("TEST_API_KEY")

if api_key:
    print("API key is ready!")
else:
    print("API key is missing!")

headers = {
    "Authorization": f"Bearer {api_key}"
}

url = "https://jsonplaceholder.typicode.com/users/1"

response = requests.get(url, headers=headers)

print(response.status_code)
print(response.json()["name"])