from math import exp
rate = float(input("Enter rate parameter (λ): "))
x = float(input("Enter value of x: "))
exponential_prob = rate * exp(-rate * x)
print("Exponential Probability:", exponential_prob)
