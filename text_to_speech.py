import requests
import base64
import json
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()
API_KEY = os.getenv('API_KEY')

url = "https://api.sarvam.ai/text-to-speech"

payload = {
    "inputs": ["The weather is sunny."],
    "target_language_code": "hi-IN",
    "speaker": "meera",
    "pitch": 0,
    "pace": 1.65,
    "loudness": 1.5,
    "speech_sample_rate": 8000,
    "enable_preprocessing": True,
    "model": "bulbul:v1"
}

headers = {
    'API-Subscription-Key': API_KEY
}

response = requests.request("POST", url, json=payload, headers=headers)
print(response)
print(response.text)
print(type(response.text))
json_data = json.loads(response.text)
print(json_data)
base64_string = json_data["audios"][0]
# Decode the base64 string
wav_data = base64.b64decode(base64_string)

# Write the decoded data to a WAV file
with open("output.wav", "wb") as wav_file:
    wav_file.write(wav_data)

print("WAV file has been created: output.wav")