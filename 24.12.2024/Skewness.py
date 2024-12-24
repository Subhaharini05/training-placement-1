data = list(map(float, input("Enter numbers separated by spaces: ").split()))
n = len(data)
mean = sum(data) / n
std_dev = (sum((x - mean) ** 2 for x in data) / n) ** 0.5
skewness = (sum((x - mean) ** 3 for x in data) / n) / (std_dev ** 3)
print("Skewness:", skewness)
