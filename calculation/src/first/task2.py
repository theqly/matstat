from math import *
from scipy import stats

file = open("../../data/normal_distribution.txt")
data = []
a = -2
sigma = 0.5
e = 0.01
n = 50
q = stats.t.ppf(1 - (e/2), n - 1)

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

S = square_x_average - (x_average * x_average)
So = (n/(n-1))*S

print("So: " + str(So))
print("left: " + str(x_average - (q * (sqrt(So) / sqrt(n)))))
print("right: " + str(x_average + (q * (sqrt(So) / sqrt(n)))))
