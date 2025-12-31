import requests

url = "http://127.0.0.1:8000/query"
payload = {"query": "Provide a cost analysis of shipments grouped by status"}
response = requests.post(url, json=payload)

print(response.json())