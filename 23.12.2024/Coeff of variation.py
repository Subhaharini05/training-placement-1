data = list(map(float, input("Enter numbers separated by spaces: ").split()))
mean = sum(data) / len(data)
std_dev = (sum((x - mean) ** 2 for x in data) / len(data)) ** 0.5
cv = (std_dev / mean) * 100
print("Coefficient of Variation:", cv, "%")
