import requests

response = requests.get("https://www.github.com/")
print(response.status_code)