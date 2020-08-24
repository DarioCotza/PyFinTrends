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
        plt.savefig(path+filename, format='png', dpi=500)
        