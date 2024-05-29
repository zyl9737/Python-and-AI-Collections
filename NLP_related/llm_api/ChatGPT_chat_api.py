import requests

url = "https://openai.api2d.net/v1/chat/completions"

headers = {"Content-Type": "application/json", "Authorization": ""}

data = {
    "model": "gpt-3.5-turbo",
    "messages": [
        {"role": "user", "content": """你好"""},
    ],
}

response = requests.post(url, headers=headers, json=data)
print("Status Code", response.status_code)
print("Json Response", response.json())
