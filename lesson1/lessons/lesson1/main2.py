import requests
token = "8627476748:AAEcx5yCK3frZiuQHFoWjtbRMN88OohJTxE"
method = "sendPhoto"
response = requests.post(
    url=f"https://api.telegram.org/bot{token}/{method}",
    data={'chat_id': 155880436, 'photo': "https://www.vecteezy.com/photo/54659403-a-vibrant-and-colorful-minecraft-landscape-adorned-with-adorable-bunnies-and-beautiful-flowers"}
).json()
print(response)