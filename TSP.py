# Eddie Tran
# Representation of the Travelling Salesperson Problem

class TSP:

    __slots__ = ['cities', 'coordinates']

    def __init__(self, filename):
        self.cities = []
        self.coordinates = {}
        # Parse files from the National TSP Collection
        with open(filename) as f:
            for line in f:
                words = line.split()
                if words[0].isdigit():
                    self.cities.append(int(words[0]))
                    self.coordinates[int(words[0])] = (float(words[1]), float(words[2]))
