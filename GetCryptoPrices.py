import requests
from datetime import datetime

CryptoAPI_L='https://api.coinmarketcap.com/v1/ticker/'


def getCryptoPrice (coin):
    response=requests.get(CryptoAPI_L+coin)
    responseJ=response.json()
    return float(responseJ[0]['price_usd'])

def main():
    getCryptoPrice('Ripple')
    getCryptoPrice('bitcoin')