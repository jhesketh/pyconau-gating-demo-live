#!/usr/bin/python


from collections import namedtuple

City = namedtuple('City', 'name state population')


def get_population_data():
    cities = [
        City('Hobart', 'TAS', 219200),
        City('Brisbane', 'QLD', 2274460),
        City('Sydney', 'NSW', 4627345),
    ]
    return cities


def largest_city(population_data):
    return sorted(population_data, key=lambda x: x.population, reverse=True)[0]


if __name__ == '__main__':
    print(largest_city(get_population_data()))
