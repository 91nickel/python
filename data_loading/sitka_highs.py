import csv
from matplotlib import pyplot as plt
from datetime import datetime

filename = "/python/data_loading/sitka_weather_2018_simple.csv"
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    print(header_row)

    # Чтение максимальных температур
    dates, hights = [], []

    print("start")
    for row in reader:
        hights.append(int(row[5]))
        dates.append(datetime.strptime(row[2], "%Y-%m-%d"))
    # print(hights)

    # Нанесение данных на диаграмму
    plt.style.use("seaborn")
    fig, ax = plt.subplots()
    ax.plot(dates, hights, c="red")

    plt.title("Daily high temperatures, July 2018", fontsize=24)
    plt.xlabel("", fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel("Temperature (F)", fontsize=16)
    plt.tick_params(axis="both", which="major", labelsize=16)

    plt.show()
