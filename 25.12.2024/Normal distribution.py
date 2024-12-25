from math import exp, sqrt, pi
mean = float(input("Enter mean: "))
std_dev = float(input("Enter standard deviation: "))
x = float(input("Enter value of x: "))
normal_prob = (1 / (std_dev * sqrt(2 * pi))) * exp(-((x - mean) ** 2) / (2 * std_dev ** 2))
print("Normal Distribution Probability:", normal_prob)
