from math import exp, factorial
mean = float(input("Enter mean: "))
k = int(input("Enter number of occurrences: "))
poisson_prob = (mean ** k * exp(-mean)) / factorial(k)
print("Poisson Probability:", poisson_prob)
