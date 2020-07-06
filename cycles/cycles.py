squares = [value ** 2 for value in range(1, 11)]
print(squares)
# squares = [[value for val in range(1, 3)] for value in range(1, 11)]
# print(squares)

numbers = [val for val in range(1, 21)]
print(numbers)
numbers = [val for val in range(1, 1000001)]
# print(numbers)
print(min(numbers))
print(max(numbers))
print(sum(numbers))

numbers = [val for val in range(1, 21, 2)]
print(numbers)

numbers = [val for val in range(3, 31, 3)]
for val in numbers:
    print(val)

numbers = [val ** 3 for val in range(1, 11)]
for val in numbers:
    print(val)
