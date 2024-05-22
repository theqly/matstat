from scipy import stats

file = open("../../data/normal_distribution.txt")
data = []
a = -2
sigma = 0.5
e = 0.01
n = 50

g1 = stats.chi2.ppf(e/2, n)
g2 = stats.chi2.ppf(1 - (e/2), n)
print(g1, g2)

for line in file:
    numbers = [float(x) for x in line.strip().split()]
    data.extend(numbers)

assert (len(data) == n)

S1_square = 0

for x in data:
    S1_square += (x - a) * (x - a)

S1_square = S1_square / n

print("S1_square: " + str(S1_square))
print("left: " + str((n * S1_square) / g2))
print("right: " + str((n * S1_square) / g1))




