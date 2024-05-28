from scipy import stats

file = open("../../data/uniform_distribution.txt")
data = []
n = 30
e = 0.01
c = stats.chi2.ppf(1 - e, n - 1)
print(c)




