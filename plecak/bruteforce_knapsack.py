import math
def print_result(capacity,fmax, picked, weights, profits, sum_weight):
    print(f'Result: {fmax}')
    for idx,item in enumerate(picked):
        if item == 1:
            print(f'Weight: {weights[idx]}, Profit: {profits[idx]}')
    
    print(f'Sum weight: {sum_weight}')
    print(f'Capacity: {capacity}')
    print(f'Picked: {picked}')
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
    print_result(capacity,fmax, picked, weights, profits, sum_weight)



profits = [100, 60, 120]
weights = [30, 100, 20]
capacity = 50
n = len(profits)
