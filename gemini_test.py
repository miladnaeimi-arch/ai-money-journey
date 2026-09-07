import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input="Write one short sentence explaining why AI automation is useful for small businesses."
)

print(interaction.output_text)
