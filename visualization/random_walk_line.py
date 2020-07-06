import matplotlib.pyplot as plt
from random_walk import RandomWalk

while True:
    # Построение случайного блуждания
    rw = RandomWalk(5000)
    rw.fill_walk()

    # Нанесение точек на диаграмму
    plt.style.use("classic")

    fig, ax = plt.subplots(figsize=(15, 9))
    point_numbers = range(rw.num_points)

    ax.plot(rw.x_values, rw.y_values, linewidth=3)

    # Удаление осей
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.show()

    keep_running = input("Make another walk? (y/n)")
    if keep_running != "y":
        break
