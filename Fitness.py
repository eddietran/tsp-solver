# Eddie Tran
# Used for calculating fitness and tour distance for the TSP.

from math import dist

# Returns Euclidean distance between two points rounded to the nearest integer
def distance(x1, y1, x2, y2):
    return round(dist((x1, y1), (x2, y2)))

# Calculates tour distance (tour cost)
def tourDistance(tour, coordinates):
    if len(tour) == 1:
        return coordinates[tour[0]]
        
    totalDistance = 0
    for i in range(1, len(tour)):
        p = coordinates[tour[i]]
        q = coordinates[tour[i-1]]
        totalDistance += distance(p[0], p[1], q[0], q[1])
    return totalDistance

# Returns fitness of a tour. Fitness increases as tourDistance decreases.
def fitness(tour, coordinates):
    return 1.0 / tourDistance(tour, coordinates)
