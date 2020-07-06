from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die


def getInteger(message, default=1):
    while True:
        print("Type q for exit")
        value = input(f"{message} (по умолчанию - {default}) ")
        if value.upper() == "Q":
            exit()
        if len(value.strip()) == 0:
            return default
        try:
            value = int(value)
            break
        except ValueError:
            print("Неверный формат ввода")
            continue

    return value


num_cubes = getInteger("Сколько кубиков будет всего: ", default=2)
num_drops = getInteger("Сколько раз бросаем: ", default=10000)
cubes = []
counter = 0
while len(cubes) < num_cubes:
    counter += 1
    sides = getInteger(f"Количество граней в кубике номер {counter}: ", default=6)
    cubes.append(Die(sides))


# Моделирование серии бросков с сохранением результата в списке
results = []
for roll_num in range(num_drops):
    result = 0
    for cube in cubes:
        result += cube.roll()
    results.append(result)

# Анализ результатов
frequencies = []
sum_sides = 0
for cube in cubes:
    sum_sides += cube.num_sides

for value in range(len(cubes), sum_sides + 1):
    frequencies.append(results.count(value))

# print(results)
# print(frequencies)

# Визуализация результатов
x_values = list(range(len(cubes), sum_sides + 1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {"title": "Result", "dtick": 1}
y_axis_config = {"title": "Frequency of Result"}
my_layout = Layout(
    title=f"Results of rolling {len(cubes)} {[side.num_sides for side in cubes]} dice 1000 times",
    xaxis=x_axis_config,
    yaxis=y_axis_config,
)
offline.plot({"data": data, "layout": my_layout}, filename="cubes_drop/d6_custom.html")
