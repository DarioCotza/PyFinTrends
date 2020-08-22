import sys, getopt
from matplotlib import pyplot as plt
import src.yahoo_data as yd
import src.trends as tr
import numpy as np


#default values
symbol = "BTC-USD"
keyword = ''
save = False
path = f'{symbol} {keyword}.png'


#args
all_arguments = sys.argv[1:]
s_options = 'hs:k:f'
l_options = ['help', 'symbol', 'keyword', 'filename']

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
        -f, --filename : save image ()



        Es. "python main.py -s TSLA -k 'Tesla' "

        Es. "python main.py -s BTC-USD -k 'Bitcoin' -f '/img/file_name.png' "

        ''')
    elif argument in ('-s', '--symbol'):
        symbol = value.upper()
    elif argument in ('-k', '--keyword'):
        keyword = value
    elif argument in ('-f', '--filename'):
        if value != '':
            path = value
        save = True

#yahoo data
y_data = yd.yahooData(symbol)
normalized_prices = y_data[0]
short_name = y_data[1]

#trends data
if keyword == '':
    keyword = short_name
trend = tr.Trends([keyword])



#plot
plt.title(short_name)
plt.plot(normalized_prices, label = f'{symbol} price')
plt.plot(np.arange(0, len(normalized_prices), len(normalized_prices)/len(trend)), trend, label=f'{keyword} searches')
plt.legend()

#save image
if save:
    plt.savefig(path)
plt.show()




    

    



