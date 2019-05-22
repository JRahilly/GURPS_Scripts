# *** Imports *** #
import random as R


# *** Functions *** #
def rollDice(sides, number):
    total = 0
    for i in range(1, number + 1):
        total += R.randint(1, sides)
    return total

def randWeight(start, stop):
    return R.uniform(start, stop)
