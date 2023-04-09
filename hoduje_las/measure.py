from functions_for_both import search_for_min, print_inorder, balance
from bst_random import create_random_bst
from avl import create_avl_from_arr
from time import process_time
import pandas as pd
#remember to sort arr before creating avl

#Wykonaj 3 wykresy (jeden wykres dla każdej z operacji: tworzenie struktury, wyszukanie minimum, wypisanie in-order) t=f(n) zależności czasu obliczeń t od liczby n elementów w drzewie. Na każdym wykresie przedstaw 2 krzywe – po jednej krzywej dla każdej struktury.

# Wykonaj wykres t=f(n) zależności czasu równoważenia t od liczby n elementów w losowym drzewie BST.


funcs_node = {"Znajdowanie minimum":search_for_min, "wypisanie inorder":print_inorder, "Równoważenie drzewa BST":balance}
funcs_arr = {"Tworzenie drzewa AVL":create_avl_from_arr, "Tworzenie drzewa BST":create_random_bst}




k = [x*10000 for x in range(1, 11)]


def decreasing(n):
    l = []
    for i in range(n, 0, -1):
        l.append(i)
    return l

def measure_arr(func, arr):
    start_time = process_time()
    func(arr)
    end_time = process_time()
    return end_time-start_time


decreasing_arr = [decreasing(k[i]) for i in range(len(k))]
df_measured_times = pd.DataFrame()
#arr arguments functions
for  m_arr in decreasing_arr:
    t_BST = measure_arr(funcs_arr["Tworzenie drzewa BST"], m_arr)
    temp_arr = [*m_arr]
    temp_arr.sort()
    t_AVL = measure_arr(funcs_arr["Tworzenie drzewa AVL"], temp_arr)
    temp_df = pd.DataFrame({"Tworzenie drzewa AVL": [t_AVL], "Tworzenie drzewa BST": [t_BST]})
    df_measured_times = pd.concat([df_measured_times, temp_df])
    df_measured_times.reset_index(drop=True)

df_measured_times.to_csv('measured.csv')






