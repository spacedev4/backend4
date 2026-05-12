import requests
token = "8627476748:AAEcx5yCK3frZiuQHFoWjtbRMN88OohJTxE"
method = "sendAudio"
response = requests.post(
    url=f"https://api.telegram.org/bot{token}/{method}",
    data={'chat_id': 155880436, 'audio': "https://s3.ustatik.com/audio.com.audio/transcoding/93/61/1850079567336193-1850079567500939-1850079570554100.mp3?X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=F0E8U41NBMMW3Y027UTJ%2F20260508%2Feu-central-1%2Fs3%2Faws4_request&X-Amz-Date=20260508T060228Z&X-Amz-SignedHeaders=host&X-Amz-Expires=518400&X-Amz-Signature=ee2eddf475bb5901f80f1c29a6a211c37c8780776a6b873b34e224620cf3ad74"}
).json()
print(response)