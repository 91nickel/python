def make_sandwich(*toppings):
    print("Your sandwich:")
    for top in toppings:
        print(f"\t- {top}")


make_sandwich(
    "Две мясные котлеты гриль", "Специальный соус", "Сыр", "Огурцы", "Салат", "Лук"
)

