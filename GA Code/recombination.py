# uniform crossover

# assign "heads" to one parent, "tails" to the other
# flip a coin for each gene of the first child
# make an inverse copy of the gene for the second child
# inheritance is independent of position

import random


def uniformXover(parent1, parent2):
    offspring1 = ""
    for i in range(len(parent1)):
        coinflip = random.randint(0, 1)
        if coinflip == 0:
            #print("choose parent 1", parent1[i])
            offspring1 = offspring1 + parent1[i]
        else:
            #print("choose parent 2", parent2[i])
            offspring1 = offspring1 + parent2[i]

    offspring2 = ""
    for i in offspring1:
        if i == '0':
            offspring2 = offspring2 + '1'
        else:
            offspring2 = offspring2 + '0'

    #print(offspring1)
    #print(offspring2)
    return offspring1, offspring2


#uniformXover('0000010110101110010110111010', '1000101010010011001000101101')
