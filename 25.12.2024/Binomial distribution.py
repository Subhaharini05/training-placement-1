from math import comb
n = int(input("Enter number of trials: "))
p = float(input("Enter probability of success: "))
k = int(input("Enter number of successes: "))
binomial_prob = comb(n, k) * (p ** k) * ((1 - p) ** (n - k))
print("Binomial Probability:", binomial_prob)
