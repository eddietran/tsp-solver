# Eddie Tran
# Used for generating populations for the TSP using random permutations.

from random import shuffle
from copy import deepcopy

# Generates a population of N random permutations.
def generatePopulation(cities, n=100):
    population = []
    for i in range(n):
        individual = deepcopy(cities)
        shuffle(individual)
        population.append(individual)
    return population
