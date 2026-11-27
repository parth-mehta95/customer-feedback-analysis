def calculate_average(numbers):
  """Calculates the average of a list of numbers."""
  if not numbers:
    return 0  # Return 0 for an empty list
  total = 0
  for number in numbers:
    total += number
  average = total / len(numbers)
  return average

# Example usage
my_numbers = [10, 20, 30, 40, 50]
result = calculate_average(my_numbers)
print(f"The average is: {result}")

my_numbers = []
result = calculate_average(my_numbers)
print(f"The average is: {result}")
