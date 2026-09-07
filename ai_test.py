import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=api_key)

response = client.responses.create(
    model="gpt-5.2",
    input="Write one short sentence explaining why AI automation is useful for small businesses."
)

print(response.output_text)
