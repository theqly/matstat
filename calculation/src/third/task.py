import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import uniform

file = open('../../data/uniform_distribution.txt')

data = []

for line in file:
    line_data = list(map(float, line.split()))
    data.extend(line_data)

data = np.array(data)

sorted_data = np.sort(data)

emper = np.arange(1, len(sorted_data) + 1) / len(sorted_data)

a, b = 0, 1

x = np.linspace(0, 1, 1000)
cdf = uniform.cdf(x, loc=a, scale=b)

plt.figure(figsize=(8, 6))
plt.step(sorted_data, emper, where='post', label='F emper')
plt.plot(x, cdf, label='F', linestyle='--')
plt.xlabel('x')
plt.ylabel('F(x)')
plt.legend()
plt.grid(True)
plt.show()
