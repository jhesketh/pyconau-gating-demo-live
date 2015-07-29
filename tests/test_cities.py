import testtools

import cities


class TestCities(testtools.TestCase):
    def test_largest(self):
        self.assertEqual(
            'Sydney', cities.largest_city(cities.get_population_data()).name)

    def test_largest_state(self):
        self.assertEqual(
            'NSW', cities.largest_state(cities.get_population_data()))
