import time
import matplotlib.pyplot as plt
import sąsiady
from load_graph import kahn_graph, kahn_neigh, tarjan_graph, tarjan_neigh
import numpy as np
import pandas as pd
k = [_ for _ in range(100, 1100,100)]

neigh_graphs = [(sąsiady.create_neighbours_matrix_directed_without_cycles(n)).to_numpy() for n in k]
graph_graphs = [(sąsiady.graph_matrix(n)).to_numpy() for n in k]

funcs = {"k_g": kahn_graph, "k_n": kahn_neigh, "t_g":tarjan_graph, "t_n":tarjan_neigh}



def measure(func, graph):
    measurements = []
    for i in range(10):
        start = time.time()
        func(graph)
        end = time.time()
        measurements.append((end-start))
    return np.mean(measurements), np.std(measurements)


k_n = {"k_n_mean": [], "k_n_std":[]}
k_g = {"k_g_mean": [], "k_g_std":[]}
t_g = {"t_g_mean": [], "t_g_std":[]}
t_n = {"t_n_mean": [], "t_n_std":[]}

for i in range(len(neigh_graphs)):
    n_mean, n_std = measure(funcs["k_n"], neigh_graphs[i])
    g_mean, g_std = measure(funcs["k_g"], graph_graphs[i])

    k_n["k_n_mean"].append(n_mean)
    k_n["k_n_std"].append(n_std)

    k_g["k_g_mean"].append(g_mean)
    k_g["k_g_std"].append(g_std)

k_n_df = pd.DataFrame(data=k_n)
k_n_df.to_csv('k_n.csv')

k_g_df = pd.DataFrame(data=k_g)
k_g_df.to_csv('k_g.csv')

for i in range(len(neigh_graphs)):
    n_mean, n_std = measure(funcs["t_n"], neigh_graphs[i])
    g_mean, g_std = measure(funcs["t_g"], graph_graphs[i])

    t_n["t_n_mean"].append(n_mean)
    t_n["t_n_std"].append(n_std)

    t_g["t_g_mean"].append(g_mean)
    t_g["t_g_std"].append(g_std)

t_n_df = pd.DataFrame(data=t_n)
t_n_df.to_csv('t_n.csv')

t_g_df = pd.DataFrame(data=t_g)
t_g_df.to_csv('t_g.csv')