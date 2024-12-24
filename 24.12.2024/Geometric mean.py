from math import prod
data = list(map(float, input("Enter numbers separated by spaces: ").split()))
geometric_mean = prod(data) ** (1 / len(data))
print("Geometric Mean:", geometric_mean)
