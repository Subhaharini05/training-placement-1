data = list(map(float, input("Enter numbers separated by spaces: ").split()))
bins = int(input("Enter the number of bins: "))
min_value, max_value = min(data), max(data)
interval = (max_value - min_value) / bins
frequency = [0] * bins
for value in data:
    index = int((value - min_value) / interval)
    index = min(index, bins - 1)
    frequency[index] += 1
print("Frequency Distribution:", frequency)
