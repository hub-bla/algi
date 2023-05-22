import pandas as pd

def print_result(capacity, result, weights, profits, profits_n_weights, acc_capacity, added):
    df_added = pd.DataFrame(added)
    gathered_profits = df_added[0].to_numpy()
    picked = [0] * len(profits)
    print(f'Result: {result}')
    for i, profit in enumerate(profits):
        if profit in gathered_profits:
            print(f'Weight: {weights[i]}, Profit: {profits[i]}')
            picked[i] = 1
    
    print(f'Sum weight: {acc_capacity}')
    print(f'Capacity: {capacity}')
    print(f'Picked: {picked}')

def greedy_knapsack(capacity, profits, weights, n_elements):
    previous_ids = [x for x in range(n_elements)]
    acc_capacity = 0
    result= 0
    profits_n_weights = sorted(zip(profits, weights, previous_ids), reverse=True)
    added = []
    i = 0 
    while True:
        acc_capacity += profits_n_weights[i][1]
        result += profits_n_weights[i][0]
        added.append(profits_n_weights[i])
        if acc_capacity > capacity or i>n:
            acc_capacity -= profits_n_weights[i][1]
            result -= profits_n_weights[i][0]
            added.remove(profits_n_weights[i])
            break
        i +=1
    
    print_result(capacity, result, weights, profits, profits_n_weights, acc_capacity, added)

profits = [100, 60, 120]
weights = [30, 100, 20]
capacity = 50
n = len(profits)
