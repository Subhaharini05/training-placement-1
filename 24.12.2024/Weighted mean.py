values = list(map(float, input("Enter values separated by spaces: ").split()))
weights = list(map(float, input("Enter corresponding weights separated by spaces: ").split()))
weighted_mean = sum(values[i] * weights[i] for i in range(len(values))) / sum(weights)
print("Weighted Mean:", weighted_mean)
