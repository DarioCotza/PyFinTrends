import yfinance as yf
import src.etc as etc

def yahooData(symbol, period):
    ticker = yf.Ticker(symbol)
    prices = ticker.history(period=period)
    prices = prices['Close']


    return [etc.Normalize(prices), ticker.info['shortName']]


