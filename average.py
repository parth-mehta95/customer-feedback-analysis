def calculate_average(numbers):
  """Calculates the average of a list of numbers."""
  if not numbers:
    return 0
  total = 0
  for number in numbers:
    total += number
  average = total / len(numbers)
  return average

numbers = [10, 20, 30, 40, 50]
print(f"The average is: {calculate_average(numbers)}")
