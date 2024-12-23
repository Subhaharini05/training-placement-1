data = list(map(float, input("Enter numbers separated by spaces: ").split()))
mean = sum(data) / len(data)
variance = sum((x - mean) ** 2 for x in data) / len(data)
std_dev = variance ** 0.5
print("Standard Deviation:", std_dev)
