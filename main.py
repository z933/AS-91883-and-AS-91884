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
# Date: 8/11/23
# Version: 6.11.23
  
def main(): # Main Program
  print("Math Quiz") # Introduction
  print("Choose an operation:") # The program prints these lines so the user can see which operation to choose.
  print("1. Addition (+)")
  print("2. Subtraction (-)")
  print("3. Multiplication (*)")
  print("4. Division (/)")
  operation_choice = input("Enter the number of the operation: ") # The program lets the user type which operation they want to chooose.

  operations = { # Valid operations
      "1": "+",
      "2": "-",
      "3": "*",
      "4": "/",
  }
  if operation_choice not in operations:
    print("Invalid choice. Please select a valid choice operation.") # If the user types anything other than the chosen operation the program will return this error messsage
    return 
# Sequence Three(): Answer and Score Generator
# Purpose: Generates the answer and score for the user
# Author: Carl Bombales
# Date: 8/11/2023
# Version 6.11.23
  operation = operations[operation_choice] # This variable is used to identify the operation that the user chose.
  score = 0 # Score function

  for _ in range(10): # Loops the question 10 times.
      question, correct_answer = generate_question(operation) # Generates the question and the correct answer.
      user_answer = input(f"What is {question}? ") # Asks the user the question.
      if validate_answer(user_answer, correct_answer): # Prints correct if the user got the question right.
        print("Correct!")
        score += 1 # Adds 1 to the score.
      else: 
        print(f"wrong! The correct Answer was: {correct_answer}.") # Prints an error message if the user answered the question wrong and shows the correct answer.
        
  print(f"Quiz completed. Your score is: {score}/10") # The program prints the user's score once they completed 10 question and ends he program.

main() # Calls the main function.