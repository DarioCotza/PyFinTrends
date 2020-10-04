def normalize(values):
    v_max = values.max()
    v_min = values.min()
    v_range = v_max-v_min
    normalized_df = [(el-v_min)/v_range*100 for el in values]
    return normalized_df


def saveimg(os, plt, save, symbol, keyword, period):
    path = f'./img/{symbol}/'
    if os.path.exists(path):
        plt.savefig(f'{path}{symbol}_{keyword}_{period}.png', format='png', dpi=500)
    else:
        os.mkdir(path)
        plt.savefig(f'{path}{symbol}_{keyword}_{period}.png', format='png', dpi=500)


def linear_regression(np, x,  y):
    #number of points
    n = len(y)
    n_1 = 1/(len(y)-1)
    #mean of x and y vector
    m_x, m_y = np.mean(x), np.mean(y)
    #calculating standard deviation of x and y
    S_x = np.sqrt(1/n*np.sum(np.power(x-m_x, 2)))
    S_y = np.sqrt(1/n*np.sum(np.power(y-m_y, 2)))
    #calculating the correlation coefficient
    r = n_1*np.sum(((x-m_x)/S_x) * ((y-m_y)/S_y))
    #slope 
    slope = r*(S_y/S_x)
    #y-intercept
    a = m_y - slope*m_x
    #plot 
    y = a + slope*x
    print(r)
    return [y, r]