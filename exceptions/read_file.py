def openAndRead(file):
    try:
        with open(file) as f:
            print(f"Содержимое файла {file}")
            for row in f:
                print(row.strip())
    except FileNotFoundError:
        # print(f"Exception: file {file} not found!")
        pass


prefix = "/python/exceptions/"
files = ["cats.txt", "dogs.txt"]
for name in files:
    openAndRead(prefix + name)
