from modules.remote import load_exercises
from modules.progress import get_progress
from modules.exercises import take_exercises
from modules.progress import save_progress 
progress = get_progress()
exercises = load_exercises()

user_request = input("have you finished the exercise (yes/no)")

if user_request == "yes":
    old_exercise = progress["current_exercise"]
    progress["history"].append(old_exercise)
    progress["completed_exercises"] += 1
    new_exercise = take_exercises(exercises, progress)
    print("The new ecxercise is : ", new_exercise)
elif user_request == "no":
    print("The actually exercise is", progress["current_exercise"])
else:
    print("Choose between yes or no please !!!!")
save_progress(progress)
    
