import requests
import os.path, json
import time
import re
import sys
import ccxt, time
import threading

def List():
    #la = requests.get("https://www.binance.com/bapi/composite/v1/public/cms/article/catalog/list/query?catalogId=48&pageNo=1&pageSize=15")
    #la = la.json()
    #List.la = la['data']['articles'][0]['title']
    List.la = ("Binance Will List manar patil(ADA)")
    
    a = List.la.split()    
    List.b = ['Binance','Will','List']    
    List.c = a[:3]    
    print(List.c)
    
def time():   
    threading.Timer(5.0, time).start()
    List()
time()


if (List.c)==(List.b):
    f = (re.search(r'\(([^)]+)\)', List.la).group(1))
else:
    print("not match")
    sys.exit()
        

exchange = ccxt.gateio({
'apiKey': '4ab66d7de8ca62ce8',
'secret': '9ada5a239acdffbb6c36541256e830114bf174a47657a32',
})

markets = exchange.fetch_markets()
balance = exchange.fetch_total_balance()
print(balance)


symbol = (f'{f}/USDT')
symbols = [symbol for symbol in [market['symbol'] for market in markets]]

if symbol in symbols:
    print(f"Good news!, {symbol} exists in Gate.io")       
else:
    print(f"Sorry, {symbol} does not exist in Gate.io")

      
global entryPrice
price = exchange.fetch_ticker(symbol)['last']
entryPrice = price
print(f'coin price: {price}')    


'''def buy(symbol):
    global entryPrice

    price = exchange.fetch_ticker(symbol)['last'] * 1.02
    entryPrice = price

    balance = exchange.fetch_total_balance()
    coin = symbol.split('/')[0]
    usdt_balance = balance['USDT']

    amount = (usdt_balance) / (price)

    exchange.create_limit_buy_order(symbol, amount=amount, price=price)

    message = f"You have {usdt_balance} USDT in your account. Buying {amount} {coin} for {price}"
    print(message)
buy(symbol)'''
    
    
'''def sell(symbol):
    price = exchange.fetch_ticker(symbol)['last'] * 1.15
    coin = symbol.split('/')[0]
    coin_balance = balance[coin]

    #exchange.create_limit_sell_order(symbol, amount=coin_balance, price=price)

    message = f"You have {coin_balance} {coin} in your account. Selling them for {price}"
    print(message)
sell(symbol)'''
  

  
