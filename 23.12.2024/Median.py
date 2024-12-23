data = sorted(list(map(float, input("Enter numbers separated by spaces: ").split())))
n = len(data)
median = (data[n // 2] if n % 2 != 0 else (data[n // 2 - 1] + data[n // 2]) / 2)
print("Median:", median)
