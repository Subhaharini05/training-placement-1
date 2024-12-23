x = list(map(float, input("Enter x values separated by spaces: ").split()))
y = list(map(float, input("Enter y values separated by spaces: ").split()))
n = len(x)
mean_x = sum(x) / n
mean_y = sum(y) / n
covariance = sum((x[i] - mean_x) * (y[i] - mean_y) for i in range(n)) / n
std_x = (sum((xi - mean_x) ** 2 for xi in x) / n) ** 0.5
std_y = (sum((yi - mean_y) ** 2 for yi in y) / n) ** 0.5
correlation = covariance / (std_x * std_y)
print("Correlation Coefficient:", correlation)
