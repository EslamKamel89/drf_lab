import requests

base_url = "http://127.0.0.1:8000"

response = requests.get(f"{base_url}/api")
print(response.json())
print(response.status_code)
