from django.test import TestCase

import requests
import json

url = "http://localhost:8000/your-receive-data-endpoint/"  # Replace with your URL
data = {
    "temperature": 25.5,
    "humidity": 28,  # Below threshold (30) to trigger email
    "luminosity": 800,
    "pH": 6.5
}

headers = {"Content-Type": "application/json"}

response = requests.post(url, data=json.dumps(data), headers=headers)
print(response.status_code)
print(response.json())