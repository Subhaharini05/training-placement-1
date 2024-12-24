observed = list(map(float, input("Enter observed frequencies separated by spaces: ").split()))
expected = list(map(float, input("Enter expected frequencies separated by spaces: ").split()))
chi_square = sum((o - e) ** 2 / e for o, e in zip(observed, expected))
print("Chi-Square Statistic:", chi_square)
