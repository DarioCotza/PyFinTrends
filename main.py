import sys, getopt
from matplotlib import pyplot as plt
import src.yahoo_data as yd
import src.trends as tr
import numpy as np


#default values
symbol = "BTC-USD"
period = '5y'
nation = ''
save = False


#args
all_arguments = sys.argv[1:]
s_options = 'hs:k:fp:n:'
l_options = ['help', 'symbol', 'keyword', 'savefile', 'period', 'nation']


try:
    arguments, values = getopt.getopt(all_arguments, s_options, l_options)
except getopt.error as err:
    print(str(err))
    sys.exit(2)


for argument, value in arguments:
    if argument in ('-h', '--help'):
        print('''
        -h, --help : show this message
        -s, --symbol : set symbol  
        -k, --keywords : set GTrends keyword (default = "Company Name")
        -f, --savefile : save image (default = "'symbol' + 'keyword.png")
        -p, --period : '1d', '1mo', '3mo', '1y', '5y' (default = "5y")
        -n, --nation : set GTrends nation 'US', 'IT', 'SR'...., 'ZW (default = all)



        Es. "python main.py -s TSLA -k 'Tesla' " : plot data

        Es. "python main.py -s BTC-USD -k 'Bitcoin' -f " : create /img/BTC-USD_Bitcoin.png

        ''')
    elif argument in ('-s', '--symbol'):
        symbol = value.upper()
    elif argument in ('-k', '--keyword'):
        keyword = value
    elif argument in ('-f', '--savefile'):
        path = f'./img/{symbol}_{keyword}.png'
        save = True
    elif argument in ('-p', '--period'):
        if value in tr.timeframes:
            period = value
        else:
            print('period should be one of these values: \n'+ str([key for key in tr.timeframes]))
            sys.exit(2)
    elif argument in ('-n', '--nation'):
        if value in tr.nations:
            nation = value.upper()
        else:
            print('nation should be one of these values \n'+ str([key for key in tr.nations]))
            sys.exit(2)


#yahoo data
y_data = yd.yahoo_data(symbol, period)
normalized_prices = y_data[0]
short_name = y_data[1]


#trends data
if keyword == None:
    keyword = short_name
trend = tr.trends([keyword], period, nation)


#plot
plt.title(short_name)
plt.plot(normalized_prices, label = f'{symbol} price')
x = np.arange(0, len(normalized_prices), len(normalized_prices)/len(trend))
try:
    plt.plot(x, trend, label=f'{keyword} searches')
except ValueError:
    diff = len(x)-len(trend)
    for i in range(diff):
        x = np.delete(i, -1)
    plt.plot(x, trend, label=f'{keyword} searches')
plt.legend()
plt.fill_between(x, trend, color = 'lawngreen', alpha = .1)
plt.fill_between(np.arange(0, len(normalized_prices), 1) ,normalized_prices, color = 'white')


#save image
if save: 
    plt.savefig(path)  
    

plt.show()




    

    



