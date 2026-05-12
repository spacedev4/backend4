import requests
import json
token = "8627476748:AAEcx5yCK3frZiuQHFoWjtbRMN88OohJTxE"
method = "getUpdates"
response = requests.post(
    url=f"https://api.telegram.org/bot{token}/{method}"
).json()
print(json.dumps(response, indent=4, ensure_ascii=False))