import Population as p


class Fitness:
    def __init__(self, chromosome, fitness):
        self.chromosome = chromosome
        self.fitness = fitness

    def __lt__(self, other):
        return self.fitness < other.fitness

    def __gt__(self, other):
        return self.fitness > other.fitness

    def __eq__(self, other):
        return self.fitness == other.fitness

    def __ne__(self, other):
        return self.fitness != other.fitness

    def __le__(self, other):
        return self.fitness <= other.fitness

    def __ge__(self, other):
        return self.fitness >= other.fitness

    def __str__(self):
        return str(self.chromosome) + " " + str(self.fitness)

    def __repr__(self):
        return str(self.chromosome) + " " + str(self.fitness)

    def __hash__(self):
        return hash(self.chromosome)

    def __iter__(self):
        return iter(self.chromosome)

    def __len__(self):
        return len(self.chromosome)

    def __getitem__(self, item):
        return self.chromosome[item]

    def __setitem__(self, key, value):
        self.chromosome[key] = value

    def __delitem__(self, key):
        del self.chromosome[key]

    def __add__(self, other):
        return self.chromosome + other.chromosome

    def Subject_Placement(self, other):
