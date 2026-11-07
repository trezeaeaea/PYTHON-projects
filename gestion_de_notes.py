notes = []
user = int(input("How many grades :"))
for i in range(user):
    nombres_de_notes = int(input("Veuillez saisir une note :"))
    notes.append(nombres_de_notes)
sum(notes)
print(sum(notes)) 
moyenne_notes = sum(notes) / user
print(moyenne_notes)  
 
if moyenne_notes >=16:
    print("GG, you're the goat")
elif moyenne_notes >=14:
    print("Good game")
elif moyenne_notes >=10:
    print("Congratulation")
elif moyenne_notes < 10:
    print("Don't worry about this")


    

