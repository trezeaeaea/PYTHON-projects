age = input("What's your age:")
price1 = 0
price2 = 0
price3 = 7
price4= 12
if age < "18":
    print("You are a minor.")
    price1 = price3
elif age > "18":
    print("You are an adult.")
    price2 = price4
popcorn = input("Do you want popcorn? (yes/no):")
if age < "18" and popcorn == "yes":
    price1 += 5 
elif age > "18" and popcorn == "yes":
     price2 += 5
else:
    print("No popcorn added.")
print(age)
print("Price for minors:", price1)
print("Price for adults:", price2)