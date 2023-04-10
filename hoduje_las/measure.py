from functions_for_both import search_for_min, print_inorder, balance
from bst_random import create_random_bst
from avl import create_avl_from_arr
from time import process_time
import pandas as pd
import numpy as np
import random
import copy
#remember to sort arr before creating avl

#Wykonaj 3 wykresy (jeden wykres dla każdej z operacji: tworzenie struktury, wyszukanie minimum, wypisanie in-order) t=f(n) zależności czasu obliczeń t od liczby n elementów w drzewie. Na każdym wykresie przedstaw 2 krzywe – po jednej krzywej dla każdej struktury.

# Wykonaj wykres t=f(n) zależności czasu równoważenia t od liczby n elementów w losowym drzewie BST.


funcs_node = {"Znajdowanie minimum":search_for_min, "wypisanie inorder":print_inorder, "Równoważenie drzewa BST":balance}
funcs_arr = {"Tworzenie drzewa AVL":create_avl_from_arr, "Tworzenie drzewa BST":create_random_bst}

def inOrder(root):
     
    # Set current to root of binary tree
    current = root
    stack = [] # initialize stack
     
    while True:
         
        # Reach the left most Node of the current Node
        if current is not None:
             
            # Place pointer to a tree node on the stack
            # before traversing the node's left subtree
            stack.append(current)
         
            current = current.left
 
         
        # BackTrack from the empty subtree and visit the Node
        # at the top of the stack; however, if the stack is
        # empty you are done
        elif(stack):
            current = stack.pop()
            print(current.value, end=" ") # Python 3 printing
         
            # We have visited the node and its left
            # subtree. Now, it's right subtree's turn
            current = current.right
 
        else:
            break


k = [x*10000 for x in range(1, 11)]


def random_arr(n):
    return  [(random.randrange(n)) for x in range (n)]



def decreasing(n):
    l = []
    for i in range(n, 0, -1):
        l.append(i)
    return l

def measure_arr(func, dec_arr):
    arr = []
    for i in range(10):
        start_time = process_time()
        func(dec_arr)
        end_time = process_time()
        arr.append(end_time-start_time)
    return np.mean(arr), np.std(arr)

def measure(func, root):
    arr = []
    for i in range(10):
        tmp = copy.deepcopy(root)
        start_time = process_time()
        func(tmp)
        end_time = process_time()
        arr.append(end_time-start_time)
    return np.mean(arr), np.std(arr)

decreasing_arr = [decreasing(k[i]) for i in range(len(k))]
random_arrs = [random_arr(k[i]) for i in range(len(k))]
df_measured_times = pd.DataFrame()

for r_arr in random_arrs:
    root = funcs_arr["Tworzenie drzewa BST"](r_arr)
    t_BST, std_BST = measure(balance, root)
    temp_df = pd.DataFrame({"Balansowanie drzewa BST": [t_BST], "std_BST":[std_BST]})
    df_measured_times = pd.concat([df_measured_times, temp_df])
#arr arguments functions
# for  m_arr in decreasing_arr:
#     root = funcs_arr["Tworzenie drzewa BST"](m_arr)
#     t_BST, std_BST = measure(inOrder, root)
#     temp_arr = [*m_arr]
#     temp_arr.sort()
#     root2 = funcs_arr["Tworzenie drzewa AVL"](temp_arr)
#     t_AVL, std_AVL = measure_arr(inOrder, root2)
#     temp_df = pd.DataFrame({"Tworzenie drzewa AVL": [t_AVL], "Tworzenie drzewa BST": [t_BST], "std_BST":[std_BST], "std_AVL": [std_AVL]})
#     df_measured_times = pd.concat([df_measured_times, temp_df])
#     df_measured_times.reset_index(drop=True)

df_measured_times.to_csv('measured_balance.csv')






