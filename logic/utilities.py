import math
import random

def generateRandomNumbers(count):
    skaitli = []
    intervals = [1000000, 5000000]
    lowerLimit = math.ceil(intervals[0]/216) # 1 000 000 / 216 = 4630
    upperLimit = math.floor(intervals[1]/216) # 5 000 000 / 216 = 23148
    while len(skaitli) < count:
        x = random.randint(lowerLimit, upperLimit)
        skaitli.append(216 * x)
    return sorted(skaitli)