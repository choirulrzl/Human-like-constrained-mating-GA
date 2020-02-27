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
# print(new_population)
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

test = initial_setup(new_population)

print(test)

def scale(population, x_min, x_max):
    X = population[:,3:]
    nom = (X-X.min(axis=0))*(x_max-x_min)
    denom = X.max(axis=0) - X.min(axis=0)
    denom[denom==0] = 1
    population[:,3:] = x_min + nom/denom
    return  population

 
x = scale(test,0,1)
print(x)

def roulette_select(population, fitnesses, number_of_population):
    pop = scale(population,0,1)
    total_fitness = float(sum(fitnesses))
    rel_fitness = [f/total_fitness for f in fitnesses]
    # Generate probability intervals for each individual
    probs = [sum(rel_fitness[:i+1]) for i in range(len(rel_fitness))]
    # Draw new population
    new_population = []
    for n in range(number_of_population):
        r = random()
        for (i, individual) in enumerate(pop):
            if r <= probs[i]:
                new_population.append(individual)
                break
    return new_population


# fitness = b.ackley(test[:,3:4], test[:,-1])
# print(fitness)

# parents_elits = select_mating_pool(test,fitness,num_parents_mating)
# print(parents_elits)