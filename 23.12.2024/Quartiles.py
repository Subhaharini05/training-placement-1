data = sorted(list(map(float, input("Enter numbers separated by spaces: ").split())))
n = len(data)
q1 = data[n // 4] if n % 4 == 0 else (data[n // 4] + data[n // 4 - 1]) / 2
q2 = data[n // 2] if n % 2 != 0 else (data[n // 2] + data[n // 2 - 1]) / 2
q3 = data[3 * n // 4] if n % 4 == 0 else (data[3 * n // 4] + data[3 * n // 4 - 1]) / 2
print("Quartiles: Q1 =", q1, ", Q2 =", q2, ", Q3 =", q3)
