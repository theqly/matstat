from scipy import stats

file = open("../../data/normal_distribution.txt")
data = []
a = -2
sigma = 0.5
e = 0.01
n = 50

g1 = stats.chi2.ppf(e/2, n - 1)
g2 = stats.chi2.ppf(1 - (e/2), n - 1)
print(g1, g2)

for line in file:
    numbers = [float(x) for x in line.strip().split()]
    data.extend(numbers)

assert (len(data) == n)

x_average = 0

for x in data:
    x_average += x

x_average = x_average / n

S0_square = 0

for x in data:
    S0_square += (x - x_average) * (x - x_average)

S0_square = S0_square / (n - 1)

print("S0_square: " + str(S0_square))
print("left: " + str(((n - 1) * S0_square) / g2))
print("right: " + str(((n - 1) * S0_square) / g1))




