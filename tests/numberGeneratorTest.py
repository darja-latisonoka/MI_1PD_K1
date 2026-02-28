import random
import time
import math

# sobrideja funkcija
def func1(n):
    skaitli = []
    while len(skaitli) < n:
        x = random.randint(1000000, 5000000)
        if x % 216 == 0:
            skaitli.append(x)
    return skaitli

# labaka funkcija, atraka un mazak random ko izveidoja Valdis
def func2(n):
    skaitli = []
    intervals = [1000000, 5000000]
    lowerLimit = math.ceil(intervals[0]/216) # 1 000 000 / 216 = 4630
    upperLimit = math.floor(intervals[1]/216) # 5 000 000 / 216 = 23148
    while len(skaitli) < n:
        x = random.randint(lowerLimit, upperLimit)
        skaitli.append(216 * x)
    return skaitli

# sito deva AI
def func3(n, low=1_000_000, high=5_000_000):
    start = ((low + 215) // 216) * 216      # first valid multiple >= low
    stop = (high // 216) * 216 + 216        # exclusive upper bound for randrange
    return [random.randrange(start, stop, 216) for _ in range(n)]

start1 = time.perf_counter_ns()
func1(5)
end1 = time.perf_counter_ns()
print("first function took:", end1-start1, "nano seconds")

start2 = time.perf_counter_ns()
func2(5)
end2 = time.perf_counter_ns()
print("second function took:", end2-start2, "nano seconds")

start3 = time.perf_counter_ns()
func3(5)
end3 = time.perf_counter_ns()
print("third function took:", end3-start3, "nano seconds")

print("second function is", (end1-start1) / (end2-start2), "times faster than first")
print("third function is", (end1-start1) / (end3-start3), "times faster than first")