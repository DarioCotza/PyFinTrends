from pytrends.request import TrendReq

def Trends(kw_list):
    pytrends = TrendReq(hl='en-US', tz=360)
    pytrends.build_payload(kw_list, cat=0, timeframe='today 5-y', geo='', gprop='')
    trend_values = pytrends.interest_over_time()[kw_list[0]]
    
    #normalization
    search_max = trend_values.max()
    search_min = trend_values.min()
    search_range = search_max-search_min
    normalized_df = [(el-search_min)/search_range*100 for el in trend_values]
    return normalized_df

    