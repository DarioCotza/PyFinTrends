import yfinance as yf

def yahooData(symbol):
    ticker = yf.Ticker(symbol)
    prices = ticker.history(period='5y')

    #normalization
    price_max = prices['Close'].max()
    price_min = prices['Close'].min()
    price_range = price_max-price_min
    normalized_df = [(el-price_min)/price_range*100 for el in prices['Close']]
    
    return [normalized_df, ticker.info['shortName']]


