def clean_data(data):
    """Cleans the input data by removing missing values and outliers."""
    cleaned_data = data.dropna()
    # Add outlier removal logic here
    return cleaned_data
