def make_shirt(size="L", text="I love Python"):
    print(f"Размер: {size}")
    print(f"Текст: {text}")


make_shirt("S", "Hello")
make_shirt(size="M", text="Hello 36")
make_shirt()


def describe_city(city, country="Russia"):
    print(f"{city} is in {country}")


describe_city("Moscow", "Russia")
describe_city("Moscow")
describe_city("Berlin")


def city_country(city, country):
    return f"{city}, {country}"


print(city_country("Москва", "Россия"))
print(city_country("Берлиин", "Германия"))
print(city_country("Лондон", "Великобритания"))


def make_album(name, album, tracks=None):
    res = {"name": name, "album": album, "track": tracks}
    if tracks:
        res["tracks"] = tracks
    return res


print(make_album("Имя 2", "Альбом 2"))
print(make_album("Имя 3", "Альбом 3", 3))


def make_album_while():
    print("Укажите 'exit' для выхода из программы")
    res = {}
    res["name"] = input_value("Введите имя исполнителя")
    res["album"] = input_value("Введите название альбома")
    tmp = input_value("Введите количество треков", False)
    if tmp:
        res["tracks"] = tmp
    return res


def input_value(message, required=True):
    res = input(f"{message}: ")
    if res == "exit":
        exit()
    if required:
        if res:
            return res
        else:
            res = input_value(message, required)
    return res


# print(make_album_while())

list_1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


def change_list(val):
    val[0] = 3
    val[1] = 3


change_list(list_1[:])
print(list_1)
