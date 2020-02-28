import numpy
import random
import benchmarkFunction as b

def normalize_parameter(population, x_min, x_max):
    X = population
    nom = (X-X.min(axis=0))*(x_max-x_min)
    denom = X.max(axis=0) - X.min(axis=0)
    denom[denom==0] = 1
    population = x_min + nom/denom
    return  population

def roulette_select(population, fitnesses, number_of_individuals):
    pop = normalize_parameter(population,0,1)
    total_fitness = numpy.sum(fitnesses)
    rel_fitness = [f/total_fitness for f in fitnesses]
    # Generate probability intervals for each individual
    probs = [sum(rel_fitness[:i+1]) for i in range(len(rel_fitness))]
    # Draw new population
    new_population = []
    for n in range(number_of_individuals):
        r = random.random()
        for (i, individual) in enumerate(pop):
            if r <= probs[i]:
                new_population.append(individual)
                break
    return new_population

def cxOnePoint(ind1,ind2):
    ind1[0],ind2[1] = ind2[0],ind1[1]
    return ind1,ind2

def crossover(parents, num_individuals,num_of_genes):
    offspring = numpy.empty([num_individuals,num_of_genes])
    for k in range(num_individuals//2):
        offspring[k],offspring[k+1] = cxOnePoint(parents[k],parents[k+1])
    return offspring

def mutation(offspring_crossover):
    # Mutation changes a single gene in each offspring randomly.
    for idx in range(offspring_crossover.shape[0]):
        # The random value to be added to the gene.
        random_value = numpy.random.uniform(-1.0, 1.0, 1)
        random_idx = random.randint(0,1)
        check_limit = offspring_crossover[idx, random_idx] + random_value
        if(check_limit <= upper_limit and check_limit >= lower_limit):
            offspring_crossover[idx, random_idx] = offspring_crossover[idx, random_idx] + random_value
    return offspring_crossover

# initialize hyperparameter
num_generations = 10
num_individuals = 5
num_of_genes = 2
lower_limit = -4
upper_limit = 4

# Defining the population size.
population_size = (num_individuals,num_of_genes)
#Creating the initial population.
population = numpy.random.uniform(low=lower_limit, high=upper_limit, size=population_size)

for generation in range(num_generations):
    print("Generation : ", generation)
    fitness = b.ackley(population[:,0], population[:,1])
    parent_selection = roulette_select(population,fitness,num_individuals)
    offspring_crossover = crossover(parent_selection,num_individuals,num_of_genes)
    offspring_mutation = mutation(offspring_crossover)
    best_result = numpy.max(b.ackley(population[:,0], population[:,1]))
    print("Best Result : ", best_result)

fitness = b.ackley(population[:,0], population[:,1])
best_match_idx = numpy.where(fitness == best_result)
print("Best solution : ", population[best_match_idx, :])
print("Best solution fitness : ", fitness[best_match_idx])
print("Best f(x) : ", b.ackley_global_minima(population[best_match_idx, 0],population[best_match_idx, 1]))
    
