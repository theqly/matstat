from scipy import stats


def chi2_ro_standard_uniform(k, n, array):
    sum = 0
    for i in range(1, k + 1):
        vi = 0
        for j in array:
            #print("[" + str((i - 1) * (1 / k)) + "; " + str(i * (1 / k)) + "]")
            if (i - 1) * (1 / k) <= j < i * (1 / k):
                vi += 1
        #print(vi)
        sum += (vi - n * (1 / k)) ** 2 / (n * (1 / k))
    return sum


file = open("../../data/uniform_distribution.txt")
data = []
n = 30
e = 0.18
c = stats.chi2.ppf(1 - e, 5 - 1)
print(c)

for line in file:
    numbers = [float(x) for x in line.strip().split()]
    data.extend(numbers)

data.sort()
print(data)
assert (len(data) == n)

ro = chi2_ro_standard_uniform(5, n, data)

p_value = 1 - stats.chi2.cdf(ro, 5 - 1)

print("d_hi: " + str(ro))
print("p_value: " + str(p_value))
