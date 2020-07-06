def make_car(model, body, **kwargs):
    car = {}
    car["model"] = model
    car["type"] = body
    for (key, val) in kwargs.items():
        car[key] = val
    return car


print(make_car("subaru", "outback", color="blue", tow_package=True))
