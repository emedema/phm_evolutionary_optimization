"""
My collection of parent selection methods
"""

import random



def MPS(fitness, mating_pool_size):
    """Multi-pointer selection (MPS)"""

    selected_to_mate = []
    cumul_prop = []
    fit_sum = sum(fitness)
    cumul_prop.append(fitness[0]/fit_sum)
    for i in range (1, len(fitness)):
        cumul_prop.append(cumul_prop[i-1] + fitness[i]/fit_sum)
    rv = random.uniform(0,1/mating_pool_size)
    i=0
    while len(selected_to_mate) < mating_pool_size:
        while rv <= cumul_prop[i]:
            selected_to_mate.append(i)
            rv = rv +1/mating_pool_size
        i = i+1
    return selected_to_mate


def tournament(fitness, mating_pool_size, tournament_size):
    """Tournament selection without replacement"""

    selected_to_mate = []
    while len(selected_to_mate) < mating_pool_size:
        tour_index = random.sample(range(0,len(fitness)), tournament_size)
        best_fit = -1000
        best_index = 0
        for i in range (0, tournament_size):
            if fitness[tour_index[i]] > best_fit:
                best_fit = fitness[tour_index[i]]
                best_index = tour_index[i]
        selected_to_mate.append(best_index)
    return selected_to_mate

def random_uniform (population_size, mating_pool_size):
    """Random uniform selection"""

    selected_to_mate = random.sample(range(0,population_size), mating_pool_size)
    return selected_to_mate

