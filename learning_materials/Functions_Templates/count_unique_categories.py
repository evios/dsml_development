def unique_categories(df):
    """
    Print only categorical columns Names and Number of unique values in corresponding column 
    """
    for col in df:
        if is_categorical_dtype(df[col]):
            print(col, sum(np.unique(df[col].cat.categories,return_counts=True)[1]))
