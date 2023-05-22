from load_from_file import load_knapsack_problem
from dynamic_knapsack import dynamic_knapsack
from bruteforce_knapsack import bruteforce_knapsack
from greedy_knapsack import greedy_knapsack

capacity, profits, weights, n_elements = load_knapsack_problem("exemplary_knapsack.txt")

print("Dynamic:")
dynamic_knapsack(capacity, profits, weights, n_elements)
print()
# capacity,profits, weights, n
print("Greedy:")
greedy_knapsack(capacity, profits, weights, n_elements)
print()

print("Brute force:")
bruteforce_knapsack(capacity, profits, weights, n_elements)