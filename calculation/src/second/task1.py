from scipy import stats

file = open("../../data/normal_distribution.txt")
data = []
a = -2
sigma = 0.5
e = 0.01
n = 50
x_n = 20
y_n = 30
f = stats.f.ppf(1 - e, x_n - 1, y_n - 1)
print(f)

for line in file:
    numbers = [float(x) for x in line.strip().split()]
    data.extend(numbers)

assert (len(data) == n)

x_data = data[:20]
y_data = data[20:]

x_average = 0
x_average_square = 0

for x in x_data:
    x_average += x
    x_average_square += x*x

x_average = x_average / x_n
x_average_square = x_average_square / x_n

y_average = 0
y_average_square = 0

for y in y_data:
    y_average += y
    y_average_square += y*y

y_average = y_average / y_n
y_average_square = y_average_square / y_n

x_S_square = x_average_square - (x_average * x_average)
y_S_square = y_average_square - (y_average * y_average)

x_S0_square = (x_n/(x_n - 1)) / x_S_square
y_S0_square = (y_n/(y_n - 1)) / y_S_square

d_F = x_S0_square / y_S0_square

print("S0_square(x): " + str(x_S0_square) + "; " + "S0_square(y): " + str(y_S0_square))
print("d_F: " + str(d_F))


