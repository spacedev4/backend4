import requests
token = "8627476748:AAEcx5yCK3frZiuQHFoWjtbRMN88OohJTxE"
method = "sendDice"
while True:
    response = requests.post(
        url=f"https://api.telegram.org/bot{token}/{method}",
        data={'chat_id': 155880436, 'emoji': '🎰'}
    ).json()
    print(response)