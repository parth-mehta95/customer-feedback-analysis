def calculate_average(numbers):
  if not numbers:
    return 0
  return sum(numbers) / len(numbers)

def calculate_median(numbers):
  sorted_numbers = sorted(numbers)
  n = len(sorted_numbers)
  if n % 2 == 0:
    # Even number of elements
    mid1 = sorted_numbers[n // 2 - 1]
    mid2 = sorted_numbers[n // 2]
    median = (mid1 + mid2) / 2
  else:
    # Odd number of elements
    median = sorted_numbers[n // 2]
  return median

# Example usage
data = [1, 2, 3, 4, 5]
average = calculate_average(data)
median = calculate_median(data)
print(f"The average is: {average}")
print(f"The median is: {median}")
