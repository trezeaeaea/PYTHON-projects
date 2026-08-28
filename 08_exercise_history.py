import random
import json


with open("progress.json","r",encoding="utf-8") as file:
    progress = json.load(file)
    
with open("exercises.json","r",encoding="utf-8") as file:
    exercises = json.load(file)
    
user_level = progress["level"]

question = input("Have you finished the exercise ? (yes/no)").lower().strip()

if question == "yes":
    old_exercise = progress["current_exercise"]
    progress["history"].append(old_exercise)
    progress["completed_exercises"] += 1
    new_exercise = random.choice(exercises[user_level])
    while new_exercise == old_exercise:
        new_exercise = random.choice(exercises[user_level])
        continue
    progress["current_exercise"] = new_exercise
    print("The new exercise is :", new_exercise)
elif question == "no":
    print("You've an unfinished exercise")
    print(progress["current_exercise"])
else:
    print("Please choose between no and yes !!!!")
    
with open("progress.json","w",encoding="utf-8") as file:
    json.dump(progress, file, indent=4)