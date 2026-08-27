import random
import json

with open("progress.json", "r", encoding="utf-8") as file:
    progress = json.load(file)
    
with open("exercises.json", "r", encoding="utf-8") as file:
    exercises = json.load(file)

user = input("What's your level (noob/intermediary) ? ").lower().strip()
answer = input("Did you finished your exercice (yes/no) ? ").lower().strip()

if answer == "yes":
    progress["completed"] = True
    progress["current_exercise"] = random.choice(exercises[user])
    print("Your new exercise:")
    print(progress["current_exercise"])
    progress["completed"] = False
elif answer == "no":
    print("You still have an unfinished exercise:")
    print(progress["current_exercise"])
    progress["completed"] = False
else:
    print("Please choose between yes or no !!!!")
    
    
with open("progress.json", "w", encoding="utf-8") as file:
    json.dump(progress, file, indent=4)

    



