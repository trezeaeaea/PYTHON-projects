import json

def get_progress():
    with open("progress.json","r",encoding="utf-8") as file:
        progress = json.load(file)
    return progress 
    
def save_progress(progress):
    with open("progress.json","w",encoding="utf-8") as file:
        json.dump(progress, file, indent=4)
    