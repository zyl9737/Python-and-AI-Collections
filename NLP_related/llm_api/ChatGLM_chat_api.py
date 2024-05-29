import time

import jwt  # pip install pyjwt
import requests


def generate_token(apikey: str, exp_seconds: int):
    try:
        id, secret = apikey.split(".")
    except Exception as e:
        raise Exception("Invalid API Key", e)

    payload = {
        "api_key": id,
        "exp": int(round(time.time()) * 1000) + exp_seconds * 1000,
        "timestamp": int(round(time.time()) * 1000),
    }

    return jwt.encode(
        payload,
        secret,
        algorithm="HS256",
        headers={"alg": "HS256", "sign_type": "SIGN"},
    )


url = "https://open.bigmodel.cn/api/pass/v4/chat/completions"
headers = {
    "Content-Type": "application/json",
    "Authorization": generate_token("", 1000),
}

data = {
    "model": "glm-3-turbo",
    "messages": [{"role": "user", "content": """你好"""}],
}

response = requests.post(url, headers=headers, json=data)

print("Status Code", response.status_code)
print("JSON Response ", response.json())
