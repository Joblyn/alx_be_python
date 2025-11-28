import unittest

class Student:
  def __init__(self, name, age) -> None:
    self.name = name
    self.age = age

class Product:
  def __init__(self, name, price, quantity) -> None:
    self.name = name
    self.price = price
    self.quantity = quantity
  
  def total_value(self):
    return self.price * self.quantity
  
# Exercise 1: Handling ZeroDivisionError

# Instructions:

# Write a program that takes two numbers as input from the user and divides the first number by the second number.
# Handle the ZeroDivisionError exception to inform the user if they attempt to divide by zero.

def divide_numbers():
  try:
    num1 = float(input("Enter the first number (numerator): "))
    num2 = float(input("Enter the second number (denominator): "))
    result = num1 / num2
    print(f"The result of {num1} divided by {num2} is: {result}")
  except ZeroDivisionError:
    print("Error: You cannot divide by zero. Please enter a non-zero denominator.")
  except ValueError:
    print("Error: Invalid input. Please enter numeric values.")
    
#     Exercise 2: File Handling with FileNotFoundError

# Instructions:

# Write a program that attempts to open and read data from a file specified by the user.
# Handle the FileNotFoundError exception to provide a meaningful message if the file does not exist.

def read_file():
  filename = input("Enter the filename to read: ")
  try:
    with open(filename, 'r') as file:
      content = file.read()
      print("File content:")
      print(content)
  except FileNotFoundError:
    print(f"Error: The file '{filename}' was not found. Please check the filename and try again.")
  except Exception as e:
    print(f"An unexpected error occurred: {e}")
    
# Exercise 3: Custom Exception

# Instructions:

# Create a custom exception class called ValueTooHighError that inherits from the Exception class.
# Write a program that takes a number as input and raises a ValueTooHighError exception if the number is greater than 100.

class ValueTooHighError(Exception):
  """Custom exception raised when a value is too high."""
  def __init__(self, value):
    self.value = value
    
  def __str__(self):
    return f"ValueTooHighError: The value {self.value} is too high. It must be 100 or less."
  
def check_value():
  try:
    value = float(input("Enter a number (should be 100 or less): "))
    if value > 100:
      raise ValueTooHighError(value)
    else:
      print(f"The value {value} is acceptable.")
  except ValueTooHighError as e:
    print(e)
  except ValueError:
    print("Error: Invalid input. Please enter a numeric value.")
    
def square_of_number(x):
  # intentional bug for testing:
  return x + x

class TestSquareOfNumber(unittest.TestCase):
  def test_square_of_number(self):
    self.assertEqual(square_of_number(3), 9)
  
  def test_square_of_number_negative(self):
    self.assertEqual(square_of_number(-4), 16)\
    
  # test valid input
  def test_square_of_number_zero(self):
    self.assertEqual(square_of_number(0), 0)
  
if __name__ == "__main__":
  unittest.main()