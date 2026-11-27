def process_data(data):
    # Validate input data before processing
    if any(x < 0 for x in data):
        raise ValueError("Negative data values are not allowed")
    # Improved function with performance enhancements
    result = [x * 2 for x in data]
    return result
