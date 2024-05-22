from math import *
from scipy import stats

file = open("../../data/normal_distribution.txt")
data = []
a = -2
sigma = 0.5
e = 0.01
n = 50

c = stats.t.ppf(1 - (e/2), n - 1)
print(c)

for line in file:
    numbers = [float(x) for x in line.strip().split()]
    data.extend(numbers)

assert (len(data) == n)

x_average = 0
square_x_average = 0

for x in data:
    x_average += x
    square_x_average += (x*x)

x_average = x_average / n
square_x_average = square_x_average / n

S_square = square_x_average - (x_average * x_average)
S0_square = (n/(n-1))*S_square

print("So: " + str(S0_square))
print("left: " + str(x_average - (c * (sqrt(S0_square) / sqrt(n)))))
print("right: " + str(x_average + (c * (sqrt(S0_square) / sqrt(n)))))
