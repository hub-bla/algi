def load_knapsack_problem(file_name):
    f = open(file_name, "r")
    lines = f.readlines()
    n_elements, capacity = map(int, lines[0].split(' '))
    lines = lines[1:]
    profits = []
    weights = []
    for line in lines:
        weight, profit  = map(int, line.split(' '))
        profits.append(profit)
        weights.append(weight)

    return capacity, profits, weights, n_elements



