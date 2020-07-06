def city_country(city, country):
    return f"{city.title()}, {country.title()}"


def city_country_people(city, country, people=""):
    if people:
        people = f"- population: {people}"
    return (f"{city.title()}, {country.title()} {people}").strip()
