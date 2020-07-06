sonya = {
    "age": 25,
    "name": "Sonya",
    "last_name": "Volchenko",
    "city": "moscow",
    "test": "Sonya",
}

for key, value in sonya.items():
    print(f"{key}->{value}")

for key in sonya:
    print(f"{key.title()}")

for key in sorted(sonya.keys()):
    print(f"{key.title()}")

print(sonya.items())
print(sonya.keys())
print(sonya.values())

print(set(sonya.values()))
print(set(sonya.values()))


