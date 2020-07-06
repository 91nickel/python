import unittest
from city_functions import city_country
from city_functions import city_country_people


class CityFunctionsTestCase(unittest.TestCase):
    """Тесты для city_functions.py"""

    def test_city_country(self):
        """Работает ли связка Santiago Chile"""
        formatted_name = city_country("santiago", "chile")
        self.assertEqual(formatted_name, "Santiago, Chile")

    def test_city_country_people(self):
        """Работает ли связка Santiago Chile при обязательном параметре количества людей"""
        formatted_name = city_country_people("santiago", "chile")
        self.assertEqual(formatted_name, "Santiago, Chile")

    def test_city_country_people_full(self):
        """Работает ли связка Santiago Chile 5000000"""
        formatted_name = city_country_people("santiago", "chile", 5000000)
        self.assertEqual(formatted_name, "Santiago, Chile - population: 5000000")


if __name__ == "__main__":
    unittest.main()
