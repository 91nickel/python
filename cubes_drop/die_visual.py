from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

# Создание кубика
die = Die()

# Моделирование серии бросков с сохранением результата в списке
results = []
for roll_num in range(1000):
    results.append(die.roll())

# Анализ результатов
frequencies = []
for value in range(1, die.num_sides + 1):
    frequencies.append(results.count(value))

# print(results)
# print(frequencies)

# Визуализация результатов
x_values = list(range(1, die.num_sides + 1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {"title": "Result"}
y_axis_config = {"title": "Frequency of Result"}
my_layout = Layout(
    title="Results of rolling one D6 1000 times",
    xaxis=x_axis_config,
    yaxis=y_axis_config,
)
offline.plot({"data": data, "layout": my_layout}, filename="cubes_drop/d6.html")
