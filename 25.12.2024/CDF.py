x = int(input("Enter value of x: "))
probabilities = list(map(float, input("Enter probabilities for each x separated by spaces: ").split()))
cdf = sum(probabilities[:x + 1]) if 0 <= x < len(probabilities) else 1
print("CDF at x =", x, ":", cdf)
