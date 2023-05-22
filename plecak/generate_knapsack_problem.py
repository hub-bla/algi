import random


def generate_knapsack_problem(n_elements):
    capacity = n_elements * 10
    profits = [0] * n_elements
    weights = [0] * n_elements
    for idx in range(n_elements):
        profits[idx] = random.randint(1, 10)
        weights[idx] = random.randint(1, 10)

    return capacity, profits, weights, n_elements