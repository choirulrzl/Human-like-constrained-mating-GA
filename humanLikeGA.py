import numpy
import random
import benchmarkFunction as b
import math as m

#setting up the DNA of population
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

def normalize_parameter(population, x_min, x_max):
    X = population[:,3:]
    nom = (X-X.min(axis=0))*(x_max-x_min)
    denom = X.max(axis=0) - X.min(axis=0)
    denom[denom==0] = 1
    population[:,3:] = x_min + nom/denom
    return  population

def roulette_select(population, fitnesses, number_of_individuals):
    pop = normalize_parameter(population,0,1)
    total_fitness = numpy.sum(fitnesses)
    rel_fitness = [f/total_fitness for f in fitnesses]
    # Generate probability intervals for each individual
    probs = [sum(rel_fitness[:i+1]) for i in range(len(rel_fitness))]
    # Draw new population
    new_population = []
    gender = False
    for n in range(number_of_individuals):
        r = random.random()
        for (i, individual) in enumerate(pop):
            if r <= probs[i] and individual[0]%2==1 and gender == False:
                new_population.append(individual)
                gender = True
                break
            elif r <= probs[i] and individual[0]%2==0 and gender == True:
                new_population.append(individual)
                gender = False
                break    
    return new_population

def cxOnePoint(ind1,ind2):
    ind1[3],ind2[3] = ind2[3],ind1[3]
    return ind1,ind2

def crossover(parents, num_individuals,num_of_genes):
    offspring = numpy.empty([num_individuals,num_of_genes])
    for k in range(num_individuals//2):
        if parents[k][0] != parents[k+1][0] and (parents[k][1] != parents[k+1][1] or parents[k][1],parents[k+1][1] == 0.0):
            offspring[k],offspring[k+1] = cxOnePoint(parents[k],parents[k+1])
            offspring[k][1] = k+1
            offspring[k+1][1] = k+1
    return offspring

def mutation(offspring_crossover):
    # Mutation changes a single gene in each offspring randomly.
    for idx in range(offspring_crossover.shape[0]):
        # The random value to be added to the gene.
        random_value = numpy.random.uniform(-1.0, 1.0, 1)
        random_idx = random.randint(3,4)
        check_limit = offspring_crossover[idx, random_idx] + random_value
        if(check_limit <= upper_limit and check_limit >= lower_limit):
            offspring_crossover[idx, random_idx] = offspring_crossover[idx, random_idx] + random_value
    return offspring_crossover

# initialize hyperparameter
num_generations = 10
num_individuals = 100
num_of_genes = 5
lower_limit = -32
upper_limit = 32

# Defining the population size.
population_size = (num_individuals,num_of_genes)
#Creating the initial population.
pop = numpy.random.uniform(low=lower_limit, high=upper_limit, size=population_size)
population = initial_setup(pop)
y=[]
for x in range(30):
    for generation in range(num_generations):
        print("Generation : ", generation)
        fitness = b.ackleyn3(population[:,3], population[:,-1])
        parent_selection = roulette_select(population,fitness,num_individuals)
        offspring_crossover = crossover(parent_selection,num_individuals,num_of_genes)
        offspring_mutation = mutation(offspring_crossover)
        best_result = numpy.max(b.ackleyn3(population[:,3], population[:,-1]))
        # print("Best Result : ", best_result)

    fitness = b.ackleyn3(population[:,3], population[:,-1])
    best_match_idx = numpy.where(fitness == numpy.max(fitness))
    print("Best solution : ", population[best_match_idx, :])
    print("Best solution fitness : ", fitness[best_match_idx])
    # print("Best f(x) : ", b.ackleyn3_global_minima(population[best_match_idx, 0],population[best_match_idx, 1]))
    y.append(population[best_match_idx, :])
    
z=numpy.average(y)
print(z)