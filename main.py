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

while True:
    print("1. View current exercise")
    print("2. Mark exercise as completed")
    print("3. View progress")
    print("4. Quit")
    
    #user = int(input("Please chooose a number (1/2/3/4) :"))
    try:
        user = int(input("Please chooose a number (1/2/3/4) :"))
    except ValueError:
        print("Please enter a valid number")
        continue
        
   
    if user == 1:
        print("The current exercise is", progress["current_exercise"])
    
    elif user == 2:
        
        progress["history"].append(progress["current_exercise"])
        progress["completed_exercises"] += 1
        exercise = take_exercises(exercises, progress)
        save_progress(progress)
        print("The new exercise is", exercise)
    elif user == 3:
        
        print("Level :", progress["level"])
        print("Completed exercises", progress["completed_exercises"])
        print("Current exercise", progress["current_exercise"])    
        #print("History exercise", progress["history"])
        for indice, valeur in enumerate(progress["history"]):
            print(indice + 1, valeur)
    elif user == 4:
        new_level = input("Choose a new level :",)
        progress["level"] = new_level
        if new_level in exercises:
            while True:
                progress["level"].append(new_level)
                exercise = take_exercises(exercises, progress)
                save_progress(progress)
                print("level change to", new_level)
                break
        elif:
            print("Invalid level.")
    elif user == 5:
        print("Goodbye")
        break
    else:
        print("Please choos a number please !!!!")
        
progress = get_progress()
print(progress)
print(progress.keys())
    
    

    
    
        

    

    
    
