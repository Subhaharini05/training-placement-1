prior = float(input("Enter prior probability: "))
likelihood = float(input("Enter likelihood: "))
evidence = float(input("Enter evidence probability: "))
posterior = (likelihood * prior) / evidence
print("Posterior Probability:", posterior)
