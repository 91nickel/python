test_list = ["Trufel", "Zhura", "Nekit", "Gavrila"]
print(test_list[0:2])

new_list = test_list[:]

message = f"\nMy favourite frieds are {test_list[0:3]}"
print(message)
message = f"\nMy favourite frieds are {test_list[1:3]}"
print(message)
message = f"\nMy favourite frieds are {test_list[-3:]}"
print(message)

pizza = ["margarita", "hunter", "tropic", "chicken", "cheese"]
friends_pizzas = pizza[:]

pizza.append("dick")
friends_pizzas.append("cunt")

print(f"\nMy favourite pizzas are:")
for value in pizza:
    print(value)
print(f"\nMy friend favourite pizzas are:")
for value in friends_pizzas:
    print(value)
