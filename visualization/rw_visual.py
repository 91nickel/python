import matplotlib.pyplot as plt
from random_walk import RandomWalk

while True:
    # Построение случайного блуждания
    rw = RandomWalk(50000)
    rw.fill_walk()

    # Нанесение точек на диаграмму
    plt.style.use("classic")
    fig, ax = plt.subplots(figsize=(15, 9))
    point_numbers = range(rw.num_points)
    ax.scatter(
        rw.x_values,
        rw.y_values,
        c=point_numbers,
        cmap=plt.cm.Blues,
        s=15,
        edgecolors="none",
    )

    # Выделение первой и последней точки
    ax.scatter(0, 0, c="green", edgecolors="none", s=100)
    ax.scatter(
        rw.x_values,
        rw.y_values,
        c=point_numbers,
        edgecolors="none",
        s=1,
        cmap=plt.cm.Blues,
    )

    # Удаление осей
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.show()

    keep_running = input("Make another walk? (y/n)")
    if keep_running != "y":
        break
