# This program is made by Carl Bombales.

import random


# Sequence One: Number Generator
# Purpose: Generating a random integer between 1 and 20
# Author: Carl Bombales
# Date 7/11/2023
# version: 6.11.23
def generate_question(operation): 
  num1 = random.randint(1,20) # Generates a random number from 1 to 20.  
  num2 = random.randint(1,20) # Generates a random number from 1 to 20.
  if operation == "+":
    return f"{num1} + {num2}", num1 + num2 # Generates a random Addition Question.
  elif operation == "-":
    return f"{num1} - {num2}", num1 - num2 # Generates a random Subtraction Question.
  elif operation == "*":
    return f"{num1} * {num2}", num1 * num2 # Generates a random Multiplication Question.
  elif operation == "/":
    return f"{num1} / {num2}", num1 / num2 # Generates a random Division Question.

def validate_answer(user_answer, correct_answer):
  return float(user_answer) == correct_answer # Validates the user's answer.
# Sequence Two: Operation choice
# Purpose: Asks the user which operation would they like to answer
# Author: Carl Bombales 
# Date: 8/11/23
# Version: 6.11.23
  
def main(): # Main Program
  print("Math Quiz") # Introduction
  print("Choose an operation:") # Asks the user which operation they would like to answer
  print("1. Addition (+)")
  print("2. Subtraction (-)")
  print("3. Multiplication (*)")
  print("4. Division (/)")
  operation_choice = input("Enter the number of the operation: ") # Asks the user which operation they would like to answer

  operations = { # Valid operations
      "1": "+",
      "2": "-",
      "3": "*",
      "4": "/",
  }
  if operation_choice not in operations:
    print("Invalid choice. Please select a valid choice operation.") # Prints error message
    return main() # Returns to the main() function
# Sequence Three(): Answer and Score Generator
# Purpose: Generates the answer and score for the user
# Author: Carl Bombales
# Date: 8/11/2023
# Version 6.11.23
  operation = operations[operation_choice] # identifies the operation that the user chose.
  score = 0 # Score function    
  for _ in range(10): # Loops the question 10 times.
      try:
       question, correct_answer = generate_question(operation) # Generates the question and the correct answer.
       user_answer = float(input(f"What is {question}? ")) # Asks the user the question.
      except ValueError:
        print("Invalid Answer. Please enter a number")
        continue
      if validate_answer(user_answer, correct_answer): # Prints correct if the user got the question right.
        print("Correct!")
        score += 1 # Adds 1 to the score.
      else: 
        print(f"wrong! The correct Answer was: " \
              f"{correct_answer}.") # Prints wrong and shows the correct answer
        
  print(f"Quiz completed. Your score is: {score}/10") # The program prints the user's score once they completed 10 question and ends he program.

main() # Calls the main function.