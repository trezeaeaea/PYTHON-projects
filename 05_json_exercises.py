import random 
import json 

with open("exercises.json", "r", encoding="utf-8") as file:
    exercises = json.load(file)
    
    
def get_random_exercise(level):
    if level in exercises:
        return random.choice(exercises[level])
    else:
        return "Unknown level. Please choose noob or intermediary."

user_level = input("What's your level (noob/intermediary) ?").lower().strip()

exercise = get_random_exercise(user_level)

print("Today's exercise:", exercise)
        