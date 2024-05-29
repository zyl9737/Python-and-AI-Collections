import requests

url = "https://openai.api2d.net/v1/embeddings"

headers = {"Content-Type": "application/json", "Authorization": ""}

data = {"model": "text-embedding-ada-002", "input": "魔兽世界坐骑去哪买"}
response = requests.post(url, headers=headers, json=data)
print("Status Code", response.status_code)
print("JSON Response ", response.json())
