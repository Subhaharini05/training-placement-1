from math import sqrt
data = list(map(float, input("Enter numbers separated by spaces: ").split()))
confidence = float(input("Enter confidence level (e.g., 0.95): "))
mean = sum(data) / len(data)
std_dev = (sum((x - mean) ** 2 for x in data) / len(data)) ** 0.5
z = {0.95: 1.96, 0.99: 2.576}[confidence]
margin_error = z * (std_dev / sqrt(len(data)))
print("Confidence Interval:", (mean - margin_error, mean + margin_error))
