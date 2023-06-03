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


    dcr = capacity
    picked = [0] * n
    sum_weight = 0 
    #first we pick penultimate row and we're looking if there's
    #a max profit
    #if not, we know that in last row the last element was added
    #
    for i in range(n, 0, -1):
        if result<=0:
            break
        if result == table[i-1][dcr]:
            continue
            
        else:

            print(f'Weight: {weights[i-1]}, Profit: {profits[i-1]}')

            result = result - profits[i-1]
            dcr = dcr - weights[i-1]
            sum_weight += weights[i-1]
            picked[i-1] = 1
    print(f'Sum weight: {sum_weight}')
    print(f'Capacity: {capacity}')
    print(f'Picked: {picked}')
profits = [1, 2, 5,6]
weights = [2, 3, 4, 5]
capacity = 8
n = len(profits)

