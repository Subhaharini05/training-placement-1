x = int(input("Enter value of x: "))
probabilities = list(map(float, input("Enter probabilities for each x separated by spaces: ").split()))
pmf = probabilities[x] if 0 <= x < len(probabilities) else 0
print("PMF at x =", x, ":", pmf)
