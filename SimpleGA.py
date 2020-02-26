import numpy
from numpy.random import randint
import random
from random import random as rand
from random import gauss, randrange

# initialize
def individual(number_of_genes,upper_limit,lower_limit):
    return [round(rand()*(upper_limit-lower_limit)+lower_limit,1) for x in range(number_of_genes)]

def population(number_of_individuals, number_of_genes, upper_limit,lower_limit):
    return [individual(number_of_genes,upper_limit,lower_limit)for x in range(number_of_individuals)]

def fitnes(equation_inputs,population):
    return numpy.sum(population*equation_inputs,axis=1)

number_of_genes = 4
upper_limit = 4
lower_limit = -4
number_of_individual = 5
# harusnya paling fit -3.-4+2.4
equation_inputs = [0,0,-3,2]

# x=population(number_of_individual,number_of_genes,upper_limit,lower_limit)
# print(x)


