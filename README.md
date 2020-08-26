# PyFinTrends
A tiny program for visualize financial market prices with Google Trends data for a given symbol and keyword

## Dependencies
- [Numpy](https://pypi.org/project/numpy/)
- [PyTrends](https://pypi.org/project/pytrends/)
- [yfinance](https://pypi.org/project/yfinance/)
- [Matplotlib](https://pypi.org/project/matplotlib/)
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
#### Shows the chart and saves the image to /img/BTC-USD/ as BTC-USD_Bitcoin price_5y.png
## Options
- -s, --symbol : set symbol  
- -k, --keywords : set GTrends keyword (default = "Company Name")
- -f, --savefile : save image
- -p, --period : '1d', '1mo', '3mo', '1y', '5y' (default = "5y")
- -n, --nation : set GTrends nation 'US', 'IT', 'SR'...., 'ZW (default = all)

## GUI
![tsla/tesla](https://github.com/Wonkysouce/img/blob/master/gui.PNG?raw=true "Example")


