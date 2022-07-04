import requests
import random
import threading




message = input("Enter message to send: ")
channel_name = input("Enter channel name: ")

def get_username():

    json = {"operationName": "ChannelShell",
            "variables": {
                "login": channel_name
            },
            "extensions": {
                "persistedQuery": {
                    "version": 1,
                    "sha256Hash": "580ab410bcd0c1ad194224957ae2241e5d252b2c5173d8e0cce9d32d5bb14efe"
                }
            }
        }

    headers = {
        'Client-ID': 'kimne78kx3ncx6brgo4mv6wki5h1ko'
    }
    r = requests.post('https://gql.twitch.tv/gql', json=json, headers=headers)
    return r.json()['data']['userOrError']['id']


channel_ID = get_username()

def whisper():
    
    tokensf = open("tokens.txt")
    tokens = random.choice(tokensf.read().splitlines())
    tokensf.close()

    headers = {
        'Accept': '*/*',
        'Accept-Language': 'en-GB',
        'Authorization': f'OAuth {tokens}',
        'Client-Id': 'kimne78kx3ncx6brgo4mv6wki5h1ko',
        'Client-Session-Id': 'b5696dea608e796b',
        'Client-Version': 'babfaee6-9f6f-4bcf-b3c6-265823943d65',
        'Connection': 'keep-alive',
        'Content-Type': 'text/plain;charset=UTF-8',
        'Origin': 'https://dashboard.twitch.tv',
        'Referer': 'https://dashboard.twitch.tv/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
        'X-Device-Id': 'q7Sdnh3wMm8iM7xn5jYNz1V20bb8Z9qj',
        'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    data = '[{"operationName":"SendWhisper","variables":{"input":{"message":"'+message+'","nonce":"a2142037eb1bea987ab81bea84e63949","recipientUserID":"'+channel_ID+'"}},"extensions":{"persistedQuery":{"version":1,"sha256Hash":"3bbd599e7891aaf3ab6a4f5788fd008f21ad0d64f6c47ea6081979f87e406c08"}}}]'

    r = requests.post('https://gql.twitch.tv/gql', headers=headers, data=data)
    print(f"Sent 1 Whisper to {channel_name}")



def start():
    r = input("Enter amount of messages to spam: ")
    for i in range(int(r)):
        threading.Thread(target=whisper).start()

start()
