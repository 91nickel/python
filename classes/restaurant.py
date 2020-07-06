class Restaurant:
    def __init__(self, rest_name, cousine_type):
        self.rest_name = rest_name
        self.cousine_type = cousine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"Название - {self.rest_name}")
        print(f"Тип - {self.cousine_type}")

    def open_rest(self):
        print(f"Ресторан {self.rest_name} открыт")

    def set_number_served(self, count):
        print(f"Было: {self.number_served}")
        self.number_served = count
        print(f"Стало: {self.number_served}")

    def increment_number_served(self, count):
        print(f"Было: {self.number_served}")
        self.number_served += count
        print(f"Стало: {self.number_served}")





# mac = Restaurant("McDonalds", "fast food")
# burger = Restaurant("Burger King", "fast food")
# kfc = Restaurant("KFC", "fast food")
# mac.describe_restaurant()
# burger.describe_restaurant()
# kfc.describe_restaurant()

# print(mac.number_served)
# mac.number_served = 5
# print(mac.number_served)
# mac.set_number_served(10)
# mac.increment_number_served(15)

# br = IceCreamIceland("Baskin Robins", "Icecream")
# br.get_flavours()
