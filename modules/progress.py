import json

def get_progress():
    with open("progress.json","r",encoding="utf-8") as file:
        progress = json.load(file)
    return progress 
    