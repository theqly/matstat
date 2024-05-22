from math import *
from scipy import stats

file = open("../../data/uniform_distribution.txt")
data = []
n = 30
e = 0.18

for line in file:
    numbers = [float(x) for x in line.strip().split()]
    data.extend(numbers)

assert (len(data) == n)

d_K = 0
i = 1
data.sort()
for x in data:
    local_max = 0
    if (x - ((i - 1) / n)) > (x - (i / n)):
        local_max = x - ((i - 1) / n)
    else:
        local_max = x - (i / n)
    if local_max > d_K: d_K = local_max

print(d_K)

d_K = d_K * sqrt(n)

print(d_K)
