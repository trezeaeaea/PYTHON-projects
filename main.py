from modules.remote import load_exercises
from modules.progress import get_progress, save_progress
from modules.exercises import take_exercises

progress = get_progress()
exercises = load_exercises()

user_request = input("Have you finished the exercise (yes/no) ? ").lower().strip()

if user_request == "yes":
    progress["history"].append(progress["current_exercise"])
    progress["completed_exercises"] += 1
    new_exercise = take_exercises(exercises, progress)
    print("The new exercise is:", new_exercise)
elif user_request == "no":
    print("The current exercise is:", progress["current_exercise"])
else:
    print("Please choose between yes or no.")
save_progress(progress)

while True:
    print()
    print("1. View current exercise")
    print("2. Mark exercise as completed")
    print("3. View progress")
    print("4. Change level")
    print("5. Quit")

    try:
        user = int(input("Please choose a number (1/2/3/4/5): "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    if user == 1:
        print("The current exercise is:", progress["current_exercise"])

    elif user == 2:
        progress["history"].append(progress["current_exercise"])
        progress["completed_exercises"] += 1
        exercise = take_exercises(exercises, progress)
        save_progress(progress)
        print("The new exercise is:", exercise)

    elif user == 3:
        print("Level:", progress["level"])
        print("Completed exercises:", progress["completed_exercises"])
        print("Current exercise:", progress["current_exercise"])
        print("History:")
        for indice, valeur in enumerate(progress["history"]):
            print(indice + 1, valeur)

    elif user == 4:
        new_level = input("Choose a new level (noob/intermediary): ").lower().strip()
        if new_level in exercises:
            progress["level"] = new_level
            exercise = take_exercises(exercises, progress)
            save_progress(progress)
            print("Level changed to", new_level)
            print("The new exercise is:", exercise)
        else:
            print("Invalid level.")

    elif user == 5:
        print("Goodbye!")
        break

    else:
        print("Please choose a number between 1 and 5.")
