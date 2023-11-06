# This program is made by Carl.
import random

def generate_question(operation):
  num1 = random.randint(1,20)
  num2 = random.randint(1,20)
  if operation == "+":
    return f"{num1} + {num2}", num1 + num2
  elif operation == "-":
    return f"{num1} - {num2}", num1 - num2
  elif operation == "*":
    return f"{num1} * {num2}", num1 * num2
  elif operation == "/":
    return f"{num1} / {num2}", num1 / num2

def validate_answer(user_answer, correct_answer):
  return int(user_answer) == correct_answer
  
def main(): 
  print("Math Quiz")
  print("Choose an operation:")
  print("1. Addition (+)")
  print("2. Subtraction (-)")
  print("3. Multiplication (*)")
  print("4. Division (/)")
  operation_choice = input("Enter the number of the operation: ")

  operations = {
      "1": "+",
      "2": "-",
      "3": "*",
      "4": "/",
  }
  if operation_choice not in operation:
    print("Invalid choice. Please select a valid choice operation.")
    return