#!/usr/bin/env python3

import urllib.request, json 
def get(url2):
    with urllib.request.urlopen(url2) as url:
            data = json.loads(url.read().decode())
            return data

bitcoin = get("https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD&e=Poloniex")
steem = get("https://min-api.cryptocompare.com/data/price?fsym=STEEM&tsyms=BTC&e=Poloniex")
eth = get("https://min-api.cryptocompare.com/data/price?fsym=ETH&tsyms=USD&e=Coinbase")
bp = float(bitcoin['USD'])
ep = float(eth['USD'])
sp = float(steem['BTC'])
print("STEEM" ,sp * bp)
