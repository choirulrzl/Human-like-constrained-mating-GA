import numpy
import random
import benchmarkFunction as b

num_generations = 10
num_individuals = 10
num_of_genes = 5
lower_limit = -4
upper_limit = 4
def initial_setup(population):
    for x in range(len(population[:,0])):
        # ganjil(1) male; genap(0) female
        if x%2==1:
            population[x:x+1,0] = 1.0
        else:
            population[x:x+1,0] = 0.0
        # initialize flag for DNA similarity
        population[x:x+1,1:3] = 0.0
    return population

# def normalize_parameter(population, x_min, x_max):
#     X = population[:,3:]
#     nom = (X-X.min(axis=0))*(x_max-x_min)
#     denom = X.max(axis=0) - X.min(axis=0)
#     denom[denom==0] = 1
#     population[:,3:] = x_min + nom/denom
#     return  population
# def roulette_select(population, fitnesses, number_of_individuals):
#     pop = normalize_parameter(population,0,1)
#     total_fitness = numpy.sum(fitnesses)
#     rel_fitness = [f/total_fitness for f in fitnesses]
#     # Generate probability intervals for each individual
#     probs = [sum(rel_fitness[:i+1]) for i in range(len(rel_fitness))]
#     # Draw new population
#     new_population = []

#     gender_check = True
#     for n in range(number_of_individuals):
#         r = random.random()
#         for (i, individual) in enumerate(pop):
#             if r <= probs[i] and individual[0] == 1.0 and gender_check == True:
#                 new_population.append(individual)
#                 gender_check = False
#                 break
#             elif r <= probs[i] and individual[0] == 0.0:
#                 new_population.append(individual)
#                 gender_check = True
#                 break    
#     return new_population


# Defining the population size.
population_size = (num_individuals,num_of_genes)
#Creating the initial population.
pop = numpy.random.uniform(low=lower_limit, high=upper_limit, size=population_size)
population = initial_setup(pop)
# parent_selection = roulette_select(population,fitness,num_individuals)
# fitness = b.ackley(population[:,3], population[:,-1])
# parent_selection = roulette_select(population,fitness,num_individuals)

print(population)
new_population = []
gender = False
for n in range(10):
    r = random.random()
    for (i, individual) in enumerate(population):
        # print("individual:",individual[0])
        # break
        if individual[0] == 1.0 and gender == False:
            new_population.append(individual)
            gender == True
            break
        elif individual[0] == 0 and gender == True:
            new_population.append(individual)
            gender == False
            break

print("new pop : ",new_population)
            