def calculate_average(numbers):
  if not numbers:
    return 0
  return sum(numbers) / len(numbers)

# Example usage
data = [1, 2, 3, 4, 5]
average = calculate_average(data)
print(f"The average is: {average}")
