def greet(name):
  """Greets the person passed in as a parameter and returns the greeting."""
  message = f"Hello, {name}!"
  print(message)
  return message

if __name__ == "__main__":
  greet("World")
