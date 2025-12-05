import requests

base_url = "http://127.0.0.1:8000"

response = requests.get(
    f"{base_url}/api",
    params={"name": "Eslam", "age": 40},
    json={"programming": "professional"},
)
print(response.text)
print(response.status_code)
