import requests

token = "8678981844:AAHjTGAA8eEC3zTuBxo7T0vazt6c_XAZ_j4"
method = "getMe"
response = requests.post(
    url=f"https://api.telegram.org/bot{token}/{method}",
)
print(response.json())