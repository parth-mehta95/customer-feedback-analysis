def process_data(data):
    # Improved function with performance enhancements
    result = [x * 2 for x in data]
    # Add a check for invalid data
    if any(x < 0 for x in data):
        raise ValueError("Negative data values are not allowed")
    return result
