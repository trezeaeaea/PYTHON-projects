import json
import random

with open("progress.json","r",encoding="utf-8") as file:
    progress = json.load(file)
    
with open("exercises.json","r",encoding="utf-8") as file:
    exercises = json.load(file)
    
user_level = progress["level"]

user_question = input("Did you finished the exercise (yes/no)").lower().strip()

if user_question == "yes":
    exercise = random.choice(exercises[user_level])
    progress["current_exercise"] = exercise
    print("The new exercise is :", exercise)
elif user_question == "no":
    print("The exercise is the same")
    print(progress["current_exercise"])
else:
    print("Can you answer to the question please !!!!")
    
    
with open("progress.json","w",encoding="utf-8") as file:
    json.dump(progress, file, indent=4)