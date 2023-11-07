# This program is made by Carl Bombales.
import random
# Sequence One: Number Generator
# Purpose: Generating a random integer between 1 and 20
# Author: Carl
# Date 7/11/2023
# version: 6.11.23
def generate_question(operation): 
  num1 = random.randint(1,20) # Generates a random number from 1 to 20.  
  num2 = random.randint(1,20) # Generates a random number from 1 to 20.
  if operation == "+":
    return f"{num1} + {num2}", num1 + num2 # This function Generates a random Addition Question.
  elif operation == "-":
    return f"{num1} - {num2}", num1 - num2 # This function Generates a random Subtraction Question.
  elif operation == "*":
    return f"{num1} * {num2}", num1 * num2 # This function Generates a random Multiplication Question.
  elif operation == "/":
    return f"{num1} / {num2}", num1 / num2 # This function Generates a random Division Question.

def validate_answer(user_answer, correct_answer):
  return int(user_answer) == correct_answer # The variable correct_answer has all the answer from each operation.
# Sequence Two: Operation choice
# Purpose: Asks the user which operation would they like to answer
# Author: Carl Bombales 
# Data:
  
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