def build_profile(name, last_name, **kwargs):
    profile = {}
    profile["name"] = name
    profile["last_name"] = last_name
    for (key, val) in kwargs.items():
        profile[key] = val
    return profile


print(build_profile("Никита", "Кузнецов", age=32, weight=80))
