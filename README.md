# PyFinTrends
A tiny program for visualize financial market prices with Google Trends data for a given symbol and keyword

## Dependencies
- Numpy
- PyTrends
- yfinance
- Matplotlib
### Install

```
pip install numpy pytrends yfinance matplotlib
```
## Usage
```
python main.py -s "BTC-USD" -k "Bitcoin"
```
or 
```
python main.py --symbol "BTC-USD" --keyword "Bitcoin"
```

![BTC-USD/Bitcoin](https://github.com/Wonkysouce/img/blob/master/BTC-USD%20.png?raw=true "Example")
```
python main.py -s "BTC-USD" -k "Bitcoin price" -f
```
or 
```
python main.py --symbol "BTC-USD" --keyword "Bitcoin price" --savefile
```
Shows the chart and saves the image to /img as BTC-USD_Bitcoin price.png
## Options
- -s, --symbol : set symbol  
- -k, --keywords : set GTrends keyword (default = "Company Name")
- -f, --savefile : save image (default = "Symbol.png")
- -p, --period : '1d', '1mo', '3mo', '1y', '5y' (default = "5y")
- -n, --nation : set GTrends nation 'US', 'IT', 'SR'...., 'ZW (default = all)

