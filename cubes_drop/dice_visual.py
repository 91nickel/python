from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

# Создание двух кубиков
die_1 = Die()
die_2 = Die()

# Моделирование серии бросков с сохранением результата в списке
results = []
for roll_num in range(1000):
    results.append(die_1.roll() + die_2.roll())

# Анализ результатов
frequencies = []
for value in range(2, die_1.num_sides + die_2.num_sides + 1):
    frequencies.append(results.count(value))

# print(results)
# print(frequencies)

# Визуализация результатов
x_values = list(range(2, die_1.num_sides + die_2.num_sides + 1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {"title": "Result", "dtick": 1}
y_axis_config = {"title": "Frequency of Result"}
my_layout = Layout(
    title="Results of rolling two D6 dice 1000 times",
    xaxis=x_axis_config,
    yaxis=y_axis_config,
)
offline.plot({"data": data, "layout": my_layout}, filename="cubes_drop/d6_d6.html")
