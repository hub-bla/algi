def dynamic_knapsack(capacity,profits, weights, n):
    table = [[0 for weight in range(capacity+1)] for i in range(n+1)]
    
    for i in range(n+1):
        for w in range(capacity+1):
            if i == 0  or w == 0:
                table[i][w] = 0
            elif weights[i-1] <=w:
                table[i][w] = max(
                    profits[i-1]+table[i-1][capacity-weights[i-1]],
                    table[i-1][w]
                )
            else:
                table[i][w] = table[i-1][w]
        
    result = table[n][capacity]
    print(f'Result: {result}')


    dcr = capacity
    picked = [0] * n
    for i in range(n, 0, -1):
        if result<=0:
            break
        if result == table[i-1][dcr]:
            continue

        else:
            print(f'Weight: {weights[i-1]}, Profit: {profits[i-1]}')

            result = result - profits[i-1]
            dcr = dcr - weights[i-1]
            picked[i-1] = 1
    print(f'Picked: {picked}')

profits = [120, 100, 60]
weights = [30, 20, 100]
capacity = 50
n = len(profits)


dynamic_knapsack(capacity, profits, weights, n)