# bit flip with probability pm independently for each bit
import random
import copy

def bitFlip(individual):
    #return mutant
    probability = 0.3 #need to set
    #individual = int(individual)
    #print(individual)
    mutantInit = copy.copy(individual)
    mutantList = [i for i in mutantInit]
    #print(mutantList)
    for i in range(len(individual)):
        if random.random() < probability:
            if individual[i] == '0':
                mutantList[i] = '1'
            else:
                mutantList[i] = '0'
    #print(mutantList)
    mutant = ''.join(map(str, mutantList))
    #print(mutant)
    return mutant

#bitFlip("0000111010100111010000111001")

