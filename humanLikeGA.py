import numpy
import random
import benchmarkFunction as b

# initialize
num_individuals = 10
num_of_genes = 5
num_parents_mating = 4 #harus genap
lower_limit = -4
upper_limit = 4

# Defining the population size.
pop_size = (num_individuals,num_of_genes) # The population will have sol_per_pop chromosome where each chromosome has num_weights genes.
#Creating the initial population.
new_population = numpy.random.uniform(low=lower_limit, high=upper_limit, size=pop_size)
print(new_population)
# print(new_population[0:1,3:4]) ini posisi buat gen pertama

def initial_setup(population):
    for x in range(len(population[:,0])):
        # ganjil(1) men; genap(0) women
        if x%2==1:
            population[x:x+1,0:1] = 1.0
        else:
            population[x:x+1,0:1] = 0.0
        population[x:x+1,1:3] = 0.0
    return population

# test = initial_setup(new_population)
# print(test)

def select_mating_pool(new_population, fitness, num_parents_mating):
    # Selecting the best individuals in the current generation as parents for producing the offspring of the next generation.
    parents = numpy.empty((num_parents_mating, new_population.shape[1]))
    for parent_num in range(num_parents_mating):
        max_fitness_idx = numpy.where(fitness == numpy.max(fitness))
        max_fitness_idx = max_fitness_idx[0][0]
        parents[parent_num, :] = new_population[max_fitness_idx, :]
        fitness[max_fitness_idx] = -99999999999
    return parents