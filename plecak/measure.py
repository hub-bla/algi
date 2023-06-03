# Wykonaj dla każdego algorytmu wykres t=f(n) zależności czasu obliczeń t od liczby n przedmiotów, przy stałej pojemności plecaka b.
# Wykonaj w skali logarytmicznej wykres t=f(n) zależności czasu obliczeń t od liczby n przedmiotów, przy stałej pojemności plecaka b. Na wykresie przedstaw 3 krzywe (jedna krzywa dla każdego algorytmu).
# Wykonaj dla każdego algorytmu wykres t=f(b) zależności czasu obliczeń t od pojemności plecaka b, przy stałej liczbie przedmiotów n.
# Wykonaj dla każdego algorytmu wykres t=f(n,b) zależności czasu obliczeń t od liczby n przedmiotów i pojemności plecaka b.
# Podaj jaka jest złożoność obliczeniowa zaproponowanych algorytmów oraz do jakich klas złożoności obliczeniowej należy 0-1 problem plecakowy (wersja optymalizacyjna i decyzyjna).
# Przedstaw obserwacje związane z działaniem wszystkich algorytmów. Czy można ustalić w jakich przypadkach algorytm zachłanny nie daje rozwiązania optymalnego?
from dynamic_knapsack import dynamic_knapsack
from bruteforce_knapsack import bruteforce_knapsack
from greedy_knapsack import greedy_knapsack
from generate_knapsack_problem import generate_knapsack_problem
import time
import numpy as np
import pandas as pd

k = [x for x in range(100, 1100, 100)]

functions = {'algorytm dynamiczny': dynamic_knapsack, 'algorytm zachłanny': greedy_knapsack}

def measure_time(f, capacity, profits, weights, n_elements):
    times = []
    for i in range(3):
        print(f"Round: {i}")
        start = time.time()
        f(capacity, profits, weights, n_elements)
        end = time.time()
        times.append(end-start)
    return np.mean(times), np.std(times)


mns = {
    'algorytm dynamiczny_mean':[],
    'algorytm zachłanny_mean': [],

}
stds = {
    'algorytm dynamiczny_std':[],
    'algorytm zachłanny_std': [],

}

capacity_arr = []
for n_el in k:
    capacity, profits, weights, n_elements = generate_knapsack_problem(n_el)
    capacity_arr.append(capacity)
    for f_name in functions.keys():
            print(f'Number of elements: {n_el}, Function: {f_name}')
            mn, std = measure_time(functions[f_name], capacity, profits, weights, n_elements)
            print(f'Mean: {mn}, Std: {std}')
            mns[f'{f_name}_mean'].append(mn)
            stds[f'{f_name}_std'].append(std)
            print(mns[f'{f_name}_mean'])

mns['capacity'] = capacity_arr
stds['capacity'] = capacity_arr
knapsack_mean_df = pd.DataFrame(mns)
knapsack_std_df = pd.DataFrame(stds)
knapsack_mean_df.to_csv("mean_without_brute_force.csv")
knapsack_std_df.to_csv("std_without_brute_force.csv")

