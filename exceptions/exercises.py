def getValue(c):
    value = input(f"Введите число номер {c}: ")
    try:
        value = int(value)
    except ValueError:
        print("Неверный формат ввода")
        value = getValue(c)

    return value


c = 0
numbers = []
while c < 2:
    c += 1
    numbers.append(getValue(c))
print(sum(numbers))
