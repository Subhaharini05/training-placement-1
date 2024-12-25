data = sorted(list(map(float, input("Enter numbers separated by spaces: ").split())))
n = len(data)
cumulative = [sum(data[:i + 1]) for i in range(n)]
gini = 1 - 2 * sum((i + 1) * data[i] for i in range(n)) / (n * sum(data))
print("Gini Coefficient:", gini)
