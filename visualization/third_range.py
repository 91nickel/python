import matplotlib.pyplot as plt

numbers = [number for number in range(0, 10)]
cubes = [cube ** 3 for cube in range(0, 10)]
print(numbers)
print(cubes)
print(plt.cm)

plt.style.use("seaborn")
fig, ax = plt.subplots()
# ax.plot(numbers, cubes, linewidth=3)
ax.scatter(numbers[:5], cubes[:5], s=100, c=cubes[:5], cmap=plt.cm.plasma)
ax.scatter(numbers[5:], cubes[5:], s=50, c=cubes[:5], cmap=plt.cm.magma)

# Назначение заголовка диаграммы и меток осей
ax.set_title("Кубы первых 10 чисел", fontsize=24)
ax.set_xlabel("Исходные значения", fontsize=14)
ax.set_ylabel("Величина", fontsize=14)

# Назначение размера шрифта и делений на осях
ax.tick_params(axis="both", labelsize=14)

ax.axis([-1, 10, -100, 800])

plt.show()
plt.savefig("/python/visualization/diagramm.png", bbox_inches="tight")
