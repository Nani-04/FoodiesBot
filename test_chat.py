import requests

url = "http://127.0.0.1:5000/chat"
data = {"message": "show me your menu"}
response = requests.post(url, json=data)

print("Response:", response.json())
