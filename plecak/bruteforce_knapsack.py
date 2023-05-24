import math

def bruteforce_knapsack(capacity, profits, weights, n_elements):
    fmax = 0
    picked = None
    sum_weight = 0
    for x in range(1, int(math.pow(2, n_elements)-1)):
        result = [0] *n_elements
        x = [*bin(x).replace('0b', '')]
        acc_weight = 0
        acc_profit = 0
        for i, b in enumerate(reversed(x)):
            if b == '1':
                acc_weight += weights[i]
                acc_profit += profits[i]
                result[i] = 1
                 
        if acc_weight <= capacity and acc_profit > fmax:
            fmax = acc_profit
            picked = [*result]
            sum_weight = acc_weight



profits = [100, 60, 120]
weights = [30, 100, 20]
capacity = 50
n = len(profits)
