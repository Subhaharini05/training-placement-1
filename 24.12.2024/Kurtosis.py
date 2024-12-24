data = list(map(float, input("Enter numbers separated by spaces: ").split()))
n = len(data)
mean = sum(data) / n
std_dev = (sum((x - mean) ** 2 for x in data) / n) ** 0.5
kurtosis = (sum((x - mean) ** 4 for x in data) / n) / (std_dev ** 4) - 3
print("Kurtosis:", kurtosis)
