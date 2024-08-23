import requests
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()
API_KEY = os.getenv('API_KEY')

url = "https://api.sarvam.ai/speech-to-text"
headers = {
    'API-Subscription-Key': API_KEY
}

# Prepare the multipart form data
files = {
    'file': ('0.mp3', open('0.mp3', 'rb'), 'audio/mpeg')
}

data = {
    'language_code': 'bn-IN',
    'model': 'saarika:v1'
}

response = requests.post(url, headers=headers, files=files, data=data)
print(response.text)