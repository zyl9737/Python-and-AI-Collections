import json

import requests

url = "https://openai.api2d.net/v1/chat/completions"

headers = {"Content-Type": "application/json", "Authorization": ""}

data = {
    "model": "gpt-3.5-turbo-0613",  # "gpt-4-0613",
    "messages": [
        {"role": "user", "content": "李华和小王是不是认识？"},
    ],
    "functions": [
        {
            "name": "get_connection",
            "description": "判断用户1和用户2 是否为朋友关系",
            "parameters": {
                "type": "object",
                "properties": {
                    "user_id1": {"type": "string", "description": "用户ID 1"},
                    "user_id2": {"type": "string", "description": "用户ID 2"},
                },
                "required": ["user_id1", "user_id2"],
            },
        }
    ],
}

response = requests.post(url, headers=headers, json=data)
print("Status Code", response.status_code)
print("JSON Response ", response.json())
