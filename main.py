# Eddie Tran
# Main file for the program.

from sys import argv
from TSP import *
import Fitness
from Population import generatePopulation
from GeneticAlgorithm import geneticAlgorithm


if __name__ == '__main__':
    TSP = TSP(argv[1]) # Takes National TSP Collection files as arguments
    population = generatePopulation(TSP.cities) # Generate population
    tour = geneticAlgorithm(population, TSP.coordinates, Fitness.fitness) # Find tour using genetic algorithm
    print(Fitness.tourDistance(tour, TSP.coordinates)) # Print tour distance
    print(' '.join(str(i) for i in tour)) # Print tour
