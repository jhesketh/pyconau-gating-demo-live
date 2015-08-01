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


def largest_state(population_data):
    state_population = {}
    for city in population_data:
        if city.state not in state_population:
            state_population[city.state] = city.population
        else:
            state_population[city.state] += city.population
    return sorted(state_population, key=state_population.get, reverse=True)[0]


if __name__ == '__main__':
    print(largest_city(get_population_data()))
    print(largest_state(get_population_data()))
