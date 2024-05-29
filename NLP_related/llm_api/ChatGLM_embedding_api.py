import time

import jwt
import requests

url = "https://open.bigmodel.cn/api/paas/v4/embeddings"


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


headers = {
    "Content-Type": "application/json",
    "Authorization": generate_token("", 1000),
}

data = {"model": "embedding-2", "input": "测试文本，今天很开心。"}

response = requests.post(url, headers=headers, json=data)

print("Status Code", response.status_code)
print("JSON Response ", response.json())
