def dynamic_knapsack(capacity,profits, weights, n):
    table = [[0 for weight in range(capacity+1)] for i in range(n+1)]
    sum_weight = 0
    for i in range(n+1):
        for w in range(capacity+1):
            if i == 0  or w == 0:
                table[i][w] = 0
            elif weights[i-1] <=w:
                table[i][w] = max(
                    #check if sum of elements in previous cell 
                    # previous row and col=actual_weight_col-weight_of_item 
                    #is greater than the cell above actual_weight_col
                    profits[i-1]+table[i-1][w-weights[i-1]],
                    table[i-1][w]
                )
            else:
                table[i][w] = table[i-1][w]
        
    result = table[n][capacity]
   
    print(f'Result: {result}')


 

profits = [100, 60, 120]
weights = [30, 100, 20]
capacity = 50
n = len(profits)

