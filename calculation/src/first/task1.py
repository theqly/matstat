from math import *
from scipy import stats

file = open("../../data/normal_distribution.txt")
data = []
a = -2
sigma = 0.5
e = 0.01
n = 50
q = stats.norm.ppf(1 - (e/2))

for line in file:
    numbers = [float(x) for x in line.strip().split()]
    data.extend(numbers)

assert (len(data) == n)

x_average = 0

for x in data:
    x_average += x

x_average = x_average / n

print("x average: " + str(x_average))
print("left: " + str(x_average - (q * (sqrt(sigma) / sqrt(n)))))
print("right: " + str(x_average + (q * (sqrt(sigma) / sqrt(n)))))
