x = list(map(float, input("Enter x values separated by spaces: ").split()))
y = list(map(float, input("Enter y values separated by spaces: ").split()))
rank_x = {v: i + 1 for i, v in enumerate(sorted(set(x)))}
rank_y = {v: i + 1 for i, v in enumerate(sorted(set(y)))}
d = [(rank_x[x[i]] - rank_y[y[i]]) ** 2 for i in range(len(x))]
n = len(x)
spearman = 1 - (6 * sum(d)) / (n * (n ** 2 - 1))
print("Spearman's Rank Correlation:", spearman)
