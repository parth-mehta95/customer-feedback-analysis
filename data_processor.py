# data_processor.py

def process_data(data):
  """Processes a list of numbers."""
  total = sum(data)
  count = len(data)
  # Alex's change: added a check for empty list
  if count == 0:
    return 0
