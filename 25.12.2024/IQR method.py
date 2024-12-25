data = sorted(list(map(float, input("Enter numbers separated by spaces: ").split())))
n = len(data)
q1 = data[n // 4] if n % 4 == 0 else (data[n // 4] + data[n // 4 - 1]) / 2
q3 = data[3 * n // 4] if n % 4 == 0 else (data[3 * n // 4] + data[3 * n // 4 - 1]) / 2
iqr = q3 - q1
lower_bound = q1 - 1.5 * iqr
upper_bound = q3 + 1.5 * iqr
outliers = [x for x in data if x < lower_bound or x > upper_bound]
print("Outliers:", outliers)
