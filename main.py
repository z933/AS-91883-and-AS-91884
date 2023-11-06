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
  elif operation "/":
    return f"{num1} / {num2}", num1 / num2