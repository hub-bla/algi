from load_from_file import load_knapsack_problem
from dynamic_knapsack import dynamic_knapsack
from bruteforce_knapsack import bruteforce_knapsack
from greedy_knapsack import greedy_knapsack

capacity, profits, weights, n_elements = load_knapsack_problem("exemplary_knapsack.txt")
print()
print(f'Capacity: {capacity}, Profits: {profits}, Weights: {weights}, N_elements: {n_elements}')
print()

print("Dynamic:")
dynamic_knapsack(capacity, profits, weights, n_elements)
print()
print("Greedy:")
greedy_knapsack(capacity, profits, weights, n_elements)
print()

print("Brute force:")
bruteforce_knapsack(capacity, profits, weights, n_elements)