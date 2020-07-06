from restaurant import Restaurant


mac = Restaurant("McDonalds", "fast food")
burger = Restaurant("Burger King", "fast food")
kfc = Restaurant("KFC", "fast food")
mac.describe_restaurant()
burger.describe_restaurant()
kfc.describe_restaurant()

print(mac.number_served)
mac.number_served = 5
print(mac.number_served)
mac.set_number_served(10)
mac.increment_number_served(15)
