from collections import Counter
data = list(map(float, input("Enter numbers separated by spaces: ").split()))
freq = Counter(data)
mode = max(freq, key=freq.get)
print("Mode:", mode)
