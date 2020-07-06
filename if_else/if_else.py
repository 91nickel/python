alien_color = "green"
if alien_color == "green":
    print("+5 points\n")

if alien_color == "red":
    print("-10 points\n")

alien_color = "green"
if alien_color == "green":
    print("+5 points\n")
else:
    print("+10 points\n")

alien_color = "red"
if alien_color == "green":
    print("+5 points\n")
else:
    print("+10 points\n")

alien_color = "red"
if alien_color == "red":
    print("+5 points\n")
elif alien_color == "green":
    print("+10 points\n")
elif alien_color == "yellow":
    print("+15 point\n")

alien_color = "green"
if alien_color == "red":
    print("+5 points\n")
elif alien_color == "green":
    print("+10 points\n")
elif alien_color == "yellow":
    print("+15 point\n")

alien_color = "yellow"
if alien_color == "red":
    print("+5 points\n")
elif alien_color == "green":
    print("+10 points\n")
elif alien_color == "yellow":
    print("+15 point\n")

age = 15

if age < 2:
    print("Младенец")
elif age >= 2 and age < 4:
    print("Малыш")
elif age >= 4 and age < 13:
    print("Ребенок")
elif age >= 13 and age < 20:
    print("Подросток")
elif age >= 20 and age < 65:
    print("Взрослый")
elif age >= 65:
    print("Взрослый")

fruits = ["banana", "orange", "lemon", "grapefruit", "apple"]
fruits_a = ["pineapple", "orange", "tomato", "grapes", "mango"]

for fruit in fruits:
    if fruit in fruits_a:
        print(f"\nThe element {fruit} is in two lists")
    else:
        print(f"\nThe element {fruit} is only in list 'fruits'")
