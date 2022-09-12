import datetime
import os
import math
import requests
from dotenv import load_dotenv

#For acessing the AlphaVantage API

class Stocks:
    
    def __init__(self):
        load_dotenv()
        self.API_KEY = os.getenv("ALPHA_VANTAGE_API_KEY")
       
    def get_quote(self, ticker):
        ticker = ticker.upper()
        url = f'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={ticker}&apikey={self.API_KEY}'
        
        try:
            r = requests.get(url)
            data = r.json()
        except Exception:
            print("Exception when asking down quote:", str(Exception))
            return self.last_quote
        
        return data["Global Quote"]

    def get_price(self, ticker) -> str:
        quote = self.get_quote(ticker)        
        
        if quote:
            price = quote["05. price"]
            return f"Current price for {ticker} on {datetime.datetime.now().strftime('%c')} is ${float(price)}"
        else:
            return "You have input an invalid stock name, try again with the correct one."