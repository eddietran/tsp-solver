# Eddie Tran
# Implementation of a simple genetic algorithm using selection, crossover, and mutation.

import random

# Genetic algorithm mostly based on the pseudocode in the Russell & Norvig textbook.
def geneticAlgorithm(population, coordinates, fitness, generations=500):
    for i in range(generations):
        weights = weightedBy(population, coordinates, fitness)
        population2 = []
        for j in range(len(population)):
            parent1, parent2 = tuple(weightedRandomChoices(population, weights, 2))
            child = reproduce(parent1, parent2)
            mutate(child)
            population2.append(child)
        population = population2
    return bestFit(population, coordinates, fitness)

# Implementation of Non=Wrapping Order Crossover
def reproduce(parent1, parent2):
    a = random.randint(0, len(parent1)-1)
    b = random.randint(0, len(parent1)-1)
    queue = [element for element in parent1 if element not in parent2[a:b]]
    queue[a:a] = parent2[a:b]
    return queue

# Returns weights (fitness) associated with each individual in the population.
def weightedBy(population, coordinates, fitness):
    weights = {}
    for i in range(len(population)):
        weights[i] = fitness(population[i], coordinates)
    return weights

# Implementation of Stochastic Universal Sampling
def weightedRandomChoices(population, weights, eliteSize):
    totalFitness = sum(weights.values())
    elites = []
    probabilities = [fitness/totalFitness for fitness in weights.values()]
    selections = {i:0 for i in range(len(population))}

    for i in range(1, len(probabilities)):
        probabilities[i] = probabilities[i-1] + probabilities[i]

    value = random.uniform(0.0, 1.0/len(population))
    while value < 1.0:
        for i in range(len(population)):
            if value < probabilities[i]:
                selections[i] += 1
                break
        value += 1.0 / len(population)

    for i in range(eliteSize):
        bestFit = max(selections, key=selections.get)
        elites.append(population[bestFit])
        del selections[bestFit]
    return elites

# Implementation of mutation using swaps
def mutate(child):
    for current in range(len(child)):
        if random.random() < (1.0/len(child)):
            swap = random.randint(0, len(child)-1)
            child[current], child[swap] = child[swap], child[current]
    return child

# Returns the best fit individual in the population.
def bestFit(population, coordinates, fitness):
    weights = weightedBy(population, coordinates, fitness)
    bestFit = max(weights, key=weights.get)
    return population[bestFit]
