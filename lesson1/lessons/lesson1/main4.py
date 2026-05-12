import requests
token = "8627476748:AAEcx5yCK3frZiuQHFoWjtbRMN88OohJTxE"
method = "sendVideo"
response = requests.post(
    url=f"https://api.telegram.org/bot{token}/{method}",
    data={'chat_id': 155880436, 'video': "https://video-preview.s3.yandex.net/sk3eYAIAAAA.mp4", "width": 640, "height": 480}
)
print(response)