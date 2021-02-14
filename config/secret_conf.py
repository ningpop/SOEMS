import json

def get_secret_key():
    with open("secret.json", "r") as secret:
        key = json.load(secret)
    return key["secret_key"]