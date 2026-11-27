def clean_data(data):
    """Cleans the input data by removing missing values and converting data types."""
    data = data.dropna()
    # Add more cleaning steps here
    return data


def process_data(data):
    """Processes the input data with performance optimizations."""
    cleaned_data = data.dropna()
    return cleaned_data
