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

functions = {'algorytm dynamiczny': dynamic_knapsack, 'algorytm zachłanny': greedy_knapsack, 'algorytm siłowy': bruteforce_knapsack}

def measure_time(f, create_knapsack, n_el):
    capacity, profits, weights, n_elements = create_knapsack(n_el)
    times = []
    for i in range(5):
        start = time.time()
        f(capacity, profits, weights, n_elements)
        end = time.time()
        times.append(end-start)
    return np.mean(times), np.std(times)


mns = {}
stds = {}


for f_name in functions.keys():
    for n_el in k:
        mn, std = measure_time(functions[f_name], generate_knapsack_problem, n_el)
        mns[f'{f_name}_mean'] = mn
        stds[f'{f_name}_std'] = std

knapsack_mean_df = pd.DataFrame(mns)
knapsack_std_df = pd.DataFrame(stds)

knapsack_mean_df.to_csv("mean.csv")
knapsack_std_df.to_csv("std.csv")

