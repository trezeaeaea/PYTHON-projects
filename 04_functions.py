import random

noob_exercises = [
    "Print 'Hello, World!' to the console.",
    "Ask the user for their name and greet them.",
    "Check if a number is even or odd.",
    "Create a multiplication table for a given number.",
    "Calculate the sum of two numbers entered by the user.",
    "Find the largest of three numbers.",
    "Count from 1 to 100 using a loop.",
    "Calculate the factorial of a number.",
    "Print all even numbers between 1 and 50.",
    "Create a simple calculator (+, -, *, /)."
]

intermediary_exercises = [
    "Create a function that checks if a number is prime.",
    "Count the number of vowels in a string.",
    "Find the largest number in a list.",
    "Remove duplicate values from a list.",
    "Reverse a string without using slicing.",
    "Check if a string is a palindrome.",
    "Sort a list without using the built-in sort() function.",
    "Count the frequency of each word in a sentence.",
    "Generate the Fibonacci sequence up to N terms.",
    "Create a password generator with random letters, numbers, and symbols."
]
def get_random_exercise(level):
    if level == "noob":
        return random.choice(noob_exercises)
    elif level == "intermediary":
        return random.choice(intermediary_exercises)
    else:
        return "Unknown level. Please choose between noob and intermediary."
    
user = input("What's your level (noob/intermediary) ?").lower().strip()

exercise = get_random_exercise(user)

print("Today's exercise:"+ exercise)
