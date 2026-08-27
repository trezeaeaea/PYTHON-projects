import requests
import random
import json

exercise_url = "https://raw.githubusercontent.com/trezeaeaea/PYTHON-projects/refs/heads/main/exercises.json"

response = requests.get(exercise_url)

print(response.status_code)

exercises = response.json()
