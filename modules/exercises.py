import random


def take_exercises(exercises, progress):
    exercise = random.choice(exercises[progress["level"]])
    while exercise == progress["current_exercise"]:
        exercise = random.choice(exercises[progress["level"]])
    progress["current_exercise"] = exercise
    return exercise
