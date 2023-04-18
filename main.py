from httpx import post
from time import sleep
from yaml import safe_load
from random import choice, randint

config = safe_load(open("config.yml"))

def get_headers(tokens):
    headers = {
    "accept": "*/*",
    "accept-language": "en-US,th;q=0.9",
    "authorization": tokens,
    "cache-control": "no-cache",
    "content-type": "application/json",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Not?A_Brand\";v=\"8\", \"Chromium\";v=\"108\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "x-debug-options": "bugReporterEnabled",
    "x-discord-locale": "en-US",
    "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJwdGIiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC4xMDI2Iiwib3NfdmVyc2lvbiI6IjEwLjAuMTkwNDUiLCJvc19hcmNoIjoieDY0Iiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiY2xpZW50X2J1aWxkX251bWJlciI6MTkwMDMxLCJuYXRpdmVfYnVpbGRfbnVtYmVyIjozMTY3NSwiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbCwiZGVzaWduX2lkIjowfQ=="}
    return headers

def get_json(messages):
    return {"content": messages, "nonce":"", "tts": False, "flags":0}

def get_messages():
    messages = open('messages.txt', 'r+',encoding="utf-8").read().splitlines()
    return choice(messages)

def send_msg(tokens, channels_id, messages):
    _hi = post(F"https://ptb.discord.com/api/v9/channels/{channels_id}/messages",headers=get_headers(tokens), json=get_json(messages))
    if _hi.status_code in [200, 201, 204]:
        print(F"send {messages} | {_hi.json()['id']} | sleep {randint(3,10)}")
        sleep(randint(3,6))
    else:
        print(F"error {_hi.text}")

if (__name__ == '__main__'):        
    while True:
        send_msg(config["account"]["tokens"], config["channels"]["channels_id"], get_messages())

