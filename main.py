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
  if operation_choice not in operations:
    print("Invalid choice. Please select a valid choice operation.")
    return
    
  operation = operations[operation_choice]
  score = 0

  for _ in range(10):
      question, correct_answer = generate_question(operation)
      user_answer = input(f"What is {question}? ")
      if validate_answer(user_answer, correct_answer):
        print("Correct!")
        score += 1
      else: 
        print(f"wrong! The correct Answer was: {correct_answer}.")
        
  print(f"Quiz completed. Your score is: {score}/10")

main()