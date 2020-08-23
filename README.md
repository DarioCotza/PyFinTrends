### PyFinTrends
A tiny program for visualize financial assets prices with Google Trends data for a given symbol and keyword, over a 5 year span

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

