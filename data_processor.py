# data_processor.py

def process_data(data):
  """Processes a list of numbers."""
  total = sum(data)
  count = len(data)
  # Alex's change: added a check for empty list
  if count == 0:
    return 0
  average = total / count
  return average


# Example usage
data = [1, 2, 3, 4, 5]
average = process_data(data)
print(f"The average is: {average}")
