import requests
token = "8627476748:AAEcx5yCK3frZiuQHFoWjtbRMN88OohJTxE"
method = "sendDocument"
response = requests.post(
    url=f"https://api.telegram.org/bot{token}/{method}",
    data={'chat_id': 155880436, 'document': "https://cdn.modrinth.com/data/yfDziwn1/versions/ableb7r5/SodiumTranslations.zip?mr_download_reason=standalone&mr_game_version=26.1&mr_loader=minecraft"}
)