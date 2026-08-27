niveau = input("What's your level (noob/intermidiary) ?")
nb_exercices = int(input("How many exercices have you finished ?"))

if nb_exercices <5:
    print("We're will going to start slowly")
elif nb_exercices <=10:
    print("You're on the good way")
else:
    print("You're a monster!!!!!")
    

