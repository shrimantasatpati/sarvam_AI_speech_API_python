import requests
import requests
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()
API_KEY = os.getenv('API_KEY')

url = "https://api.sarvam.ai/translate"

payload = {
    "input": "The weather is sunny.",
    "source_language_code": "en-IN",
    "target_language_code": "hi-IN",
    # Whether the translation is formal or colloquial
    # Available options: formal, code-mixed
    "mode": "formal", 
    "model": "mayura:v1",
    # This will enable custom preprocessing of the input text which can result in better translations.
    "enable_preprocessing": True
}
headers = {
    'API-Subscription-Key': API_KEY
}

response = requests.request("POST", url, json=payload, headers=headers)
print(response.text)