from os import listdir

# Получение списка файлов и папок из каталога
files = [f for f in listdir("/")]
print(files)

path = "/python/files/test.txt"
# Простое чтение файла
with open(path) as file_object:
    contents = file_object.read()
print(contents)

# Чтение построчно
content = ""
ar_content = []
with open(path) as file_object:
    for row in file_object:
        row = row.replace("1", " one ")
        content += row.strip()
        ar_content.append(row.strip())
print(content)
print(ar_content)
