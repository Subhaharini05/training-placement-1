data = sorted(list(map(float, input("Enter numbers separated by spaces: ").split())))
percentile = float(input("Enter the percentile (e.g., 50 for median): "))
k = int((percentile / 100) * len(data))
print("Percentile Value:", data[k])
