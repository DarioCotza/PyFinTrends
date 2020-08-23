import yfinance as yf
import src.etc as etc

def yahoo_data(symbol, period):
    ticker = yf.Ticker(symbol)
    prices = ticker.history(period=period)
    prices = prices['Close']
    return [etc.normalize(prices), ticker.info['shortName']]

