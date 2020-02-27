import numpy
import random
import benchmarkFunction as b

# initialize
num_individuals = 10
num_of_genes = 2
num_parents_mating = 4
lower_limit = -32
upper_limit = 32

# Defining the population size.
pop_size = (num_individuals,num_of_genes) # The population will have sol_per_pop chromosome where each chromosome has num_weights genes.
#Creating the initial population.
new_population = numpy.random.uniform(low=lower_limit, high=upper_limit, size=pop_size)

def select_mating_pool(pop, fitness, num_parents):
    # Selecting the best individuals in the current generation as parents for producing the offspring of the next generation.
    parents = numpy.empty((num_parents, pop.shape[1]))
    for parent_num in range(num_parents):
        max_fitness_idx = numpy.where(fitness == numpy.max(fitness))
        max_fitness_idx = max_fitness_idx[0][0]
        parents[parent_num, :] = pop[max_fitness_idx, :]
        fitness[max_fitness_idx] = -99999999999
    return parents

def crossover(parents, offspring_size):
    offspring = numpy.empty(offspring_size)
    # The point at which crossover takes place between two parents. Usually it is at the center.
    crossover_point = numpy.uint8(offspring_size[1]/2)

    for k in range(offspring_size[0]):
        # Index of the first parent to mate.
        parent1_idx = k%parents.shape[0]
        # Index of the second parent to mate.
        parent2_idx = (k+1)%parents.shape[0]
        # The new offspring will have its first half of its genes taken from the first parent.
        offspring[k, 0:crossover_point] = parents[parent1_idx, 0:crossover_point]
        # The new offspring will have its second half of its genes taken from the second parent.
        offspring[k, crossover_point:] = parents[parent2_idx, crossover_point:]
    return offspring

def mutation(offspring_crossover):
    # Mutation changes a single gene in each offspring randomly.
    for idx in range(offspring_crossover.shape[0]):
        # The random value to be added to the gene.
        random_value = numpy.random.uniform(-1.0, 1.0, 1)
        check_limit = offspring_crossover[idx, 1] + random_value
        if(check_limit <= upper_limit and check_limit >= lower_limit):
            offspring_crossover[idx, 1] = offspring_crossover[idx, 1] + random_value
    return offspring_crossover

def fitness_similarity_check(best_result):
    result = False
    for n in range(len(best_result)):
        if best_result[n] == best_result[n-1]:
            result = True
    return result


num_generations = 10
stop_point=[]
for generation in range(num_generations):
    print("Generation : ", generation)
    # Measing the fitness of each chromosome in the population.
    fitness = b.ackley(new_population[:,0], new_population[:,1])
    # Selecting the best parents in the population for mating.
    parents = select_mating_pool(new_population, fitness, num_parents_mating)
    # Generating next generation using crossover.
    offspring_crossover = crossover(parents,offspring_size=(pop_size[0]-parents.shape[0], num_of_genes))
    # Adding some variations to the offsrping using mutation.
    offspring_mutation = mutation(offspring_crossover)
    # Creating the new population based on the parents and offspring.
    new_population[0:parents.shape[0], :] = parents
    new_population[parents.shape[0]:, :] = offspring_mutation
    # The best result in the current iteration.
    best_result = b.ackley(new_population[:,0], new_population[:,1])
    stop_point.append(numpy.max(best_result))
    print("Best result : ", numpy.max(best_result))
    # if fitness_similarity_check(stop_point)==True:
    #     break

print(stop_point)
# Getting the best solution after iterating finishing all generations.
#At first, the fitness is calculated for each solution in the final generation.
fitness = b.ackley(new_population[:,0], new_population[:,1])
# Then return the index of that solution corresponding to the best fitness.
best_match_idx = numpy.where(fitness == numpy.max(fitness))

print("Best solution : ", new_population[best_match_idx, :])
print("Best solution fitness : ", fitness[best_match_idx])
print("Best f(x) : ", b.ackley_global_minima(new_population[best_match_idx, 0],new_population[best_match_idx, 1]))