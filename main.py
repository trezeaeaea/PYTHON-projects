from modules.remote import load_exercises
from modules.progress import get_progress
from modules.exercises import take_exercises

progress = get_progress()
exercises = load_exercises()
exercise = take_exercises(exercises, progress)

print(type[exercises])
print(type[progress])
print(type[exercise])

