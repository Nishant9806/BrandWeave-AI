import os
from dotenv import load_dotenv
from google import genai

# Load environment variables
load_dotenv()

# Get API key
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("Gemini API key not found in .env")

# Initialize Gemini
client = genai.Client(api_key=api_key)

# Send a test request
response = client.models.generate_content(
    model="gemini-3.8-flash",
    contents="Explain brand tone analysis in two simple sentences."
)

print("\n--- GEMINI RESPONSE ---")
print(response.text)