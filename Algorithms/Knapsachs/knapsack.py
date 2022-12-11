def knapsack(items, M):
    sort = sorted(items, key = lambda x: x[0]/x[1], reverse = True)
    total_value = 0
    for weight, value in sort:
        if weight <= M:
            M -= weight
            total_value += value
        elif M > 0:
            total_value += value * (M / weight)
            break
    return total_value

print(knapsack([(15,5), (25,6), (10, 2), (100, 10)], 55))