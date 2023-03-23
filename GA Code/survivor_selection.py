import itertools
import random


def mu_plus_lambda(current_pop, current_fitness, offspring, offspring_fitness):
    """mu+lambda selection"""

    # creating a dictionary to list the population and the fitness together
    # new lists for storing the concatenated lists in
    new_curr = []
    new_off = []
    for i in current_pop:
        temp = "".join(str(j) for j in i)
        new_curr.append(temp)

    for i in offspring:
        temp = "".join(str(j) for j in i)
        new_off.append(temp)

    # zipping the individuals and its fitness together for both current population and offspring
    temp_curr = dict(zip(new_curr, current_fitness))
    temp_off = dict(zip(new_off, offspring_fitness))

    # combining the dictionaries together
    temp_combo = {**temp_curr, **temp_off}

    # sorting the individuals based on their fitness, from high to low
    sorted_temp = dict(sorted(temp_combo.items(), key=lambda kv: kv[1], reverse=True))

    # taking the length of the initial current population to take the first highest ranking individuals
    curr_len = len(current_pop)
    slicedDict = dict(itertools.islice(sorted_temp.items(), 0, curr_len))

    # unraveling the string made from before to return it to a list of numbers
    temp_pop = list(slicedDict.keys())
    population = []
    for i in temp_pop:
        temp = []
        for j in i:
            temp.append(int(j))
        population.append(temp)

    # taking the list of values of the dictionary, i.e. the fitness of the individuals
    fitness = list(slicedDict.values())

    return population, fitness
