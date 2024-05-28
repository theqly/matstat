from math import *
from scipy import stats

file = open("../../data/uniform_distribution.txt")
data = []
n = 30
e = 0.01
c = stats.kstwobign.ppf(1 - e)
print(c)

for line in file:
    numbers = [float(x) for x in line.strip().split()]
    data.extend(numbers)

assert (len(data) == n)


max_difference = 0
point = 0
data.sort()
i = 1
point = 0

for x in data:
    local_max = 0
    local_i = 0
    if abs(x - ((i - 1) / n)) > abs(x - (i / n)):
        local_max = abs(x - ((i - 1) / n))
        local_i = i - 1
    else:
        local_max = abs(x - (i / n))
        local_i = i
    if local_max >= max_difference:
        max_difference = local_max
        point = local_i
    i += 1

#неправильно ищет точку, в которой достигается максимальное значение. хз в чем трабл
d_K = max_difference * sqrt(n)
print(data)
print("max difference: " + str(max_difference))
print("in point: " + str(data[point - 1]))
print("d_K: " + str(d_K))
print("i: " + str(point))
