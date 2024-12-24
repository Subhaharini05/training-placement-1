data = list(map(float, input("Enter numbers separated by spaces: ").split()))
harmonic_mean = len(data) / sum(1 / x for x in data)
print("Harmonic Mean:", harmonic_mean)
