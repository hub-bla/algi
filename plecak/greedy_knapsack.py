import pandas as pd

def greedy_knapsack(capacity, profits, weights, n_elements):
    previous_ids = [x for x in range(n_elements)]
    acc_capacity = 0
    result= 0
    profits_n_weights = sorted(zip(profits, weights, previous_ids), reverse=True)
    added = []
    i = 0 
    while (i<n_elements):
        if (acc_capacity+profits_n_weights[i][1]) <= capacity:
            acc_capacity += profits_n_weights[i][1]
            result += profits_n_weights[i][0]
            added.append(profits_n_weights[i])
        
        i +=1
        
        

profits = [100, 60, 120]
weights = [30, 100, 20]
capacity = 50
n = len(profits)
