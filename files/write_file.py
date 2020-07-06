filename = "/python/files/guest.txt"
guests = []
content = ""
while True:
    name = input("Введите текст для сохранения в файле (break для остановки): ")
    if name == "break":
        break
    guests.append(name)
if guests:
    for row in guests:
        content += row + "\n"

    with open(filename, "a") as file_object:
        file_object.write(content)
        print("Запись произведена успешно")
else:
    print("Введенных данных нет")
