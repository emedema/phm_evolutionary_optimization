# binary string
# 28-bit long
import random


def initial(pop_size, chrom_len):
    popList = []
    i = 0
    while i < pop_size:
        bitList = []
        while len(bitList) < chrom_len:
            bit = random.randint(0, 1)
            bitList.append(bit)
            bitString = ''.join(map(str, bitList))
            #bitString = int(bitString)
        popList.append(bitString)
        i += 1
    print(popList)
    return popList


#initial(20, 28)
