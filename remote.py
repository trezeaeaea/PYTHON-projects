import requests
import json

exercise_url = "https://raw.githubusercontent.com/trezeaeaea/PYTHON-projects/refs/heads/main/exercises.json"

def load_exercises():
    try:
        response = requests.get(exercise_url)
        response.raise_for_status()
        exercises = response.json()
        print("Exercises loaded from GitHub.")
    except:
        with open("exercises.json","r",encoding="utf-8") as file:
                exercises = json.load(file)
        print("Internet unavailable. Local exercises loaded.")
    return exercises
    