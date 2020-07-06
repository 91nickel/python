import json


def getName():
    while True:
        name = input("Введите имя, или 'exit' для выхода: ")
        if name == "exit":
            exit()
        if not name:
            name = getName()
            break
        else:
            break
    return name


def getFavouriteNumber():
    while True:
        number = input("Введите любимое число, или 'exit' для выхода: ")
        if number == "exit":
            exit()
        if not number:
            number = getFavouriteNumber()
            break
        else:
            try:
                number = int(number)
                break
            except ValueError:
                print("Необходимо ввести число")
                number = getFavouriteNumber()
                break
    return number


def readFile():
    with open(filename) as f:
        try:
            content = json.load(f)
        except json.decoder.JSONDecodeError:
            return False
        else:
            return content


def saveJson(content):
    with open(filename, "w") as f:
        json.dump(content, f)
        print("Сохранение данных прошло успешно")


def process():
    name = getName()
    data = readFile()
    if data == False:
        data = {}
    try:
        data[name]
    except KeyError:
        number = getFavouriteNumber()
    else:
        print(f"Ваше любимое число - {data[name]}")
        if input("Хотите ввести новое? (Y/N) ").upper() == "Y":
            number = getFavouriteNumber()
        else:
            number = None

    if number:
        data[name] = number
        saveJson(data)


filename = "/python/json/user_number.json"
while True:
    process()
