def normalize(values):
    v_max = values.max()
    v_min = values.min()
    v_range = v_max-v_min
    normalized_df = [(el-v_min)/v_range*100 for el in values]
    return normalized_df