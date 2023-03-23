import random


def tournament(fitness, mating_pool_size, tournament_size):
    """Tournament selection without replacement"""

    selected_to_mate = []
    size = list(range(len(fitness)))

    # student code starts
    current_member = 0
    while current_member <= mating_pool_size:
        k = random.choices(size, k=tournament_size)  # pick k individuals randomly
        i = max(k)  # individual i is the best one
        selected_to_mate.append(i)  # add individual to mating pool
        current_member += 1
    # student code ends

    return selected_to_mate
