import time
import matplotlib.pyplot as plt
import sąsiady
from sąsiady import create_neigh_with_specific_saturation, nexts_dict_generator
from load_graph import kahn_graph, kahn_neigh, tarjan_graph, tarjan_neigh
import numpy as np
import pandas as pd
from cycles import hamilton_neigh, hamilton_nexts
k = [_ for _ in range(25, 35)]
saturations = [i/100 for i in range(40, 100, 10)]
print(saturations)
funcs = {"h_nxts": [hamilton_nexts,nexts_dict_generator]}



def measure(func, graph):
    measurements = []
    
    start = time.time()
    func(graph)
    end = time.time()
    measurements.append((end-start))
    return np.mean(measurements), np.std(measurements)



df = pd.DataFrame()
for func in funcs.keys():
    for saturation in saturations:
        print("Working...")
        measurements_mean = []
        measurements_std = []
        for g_size in k:
            print(f'Graph size:{g_size}, Saturation: {saturation}')
            graph = funcs[func][1](g_size, saturation)
            mean, std = measure(funcs[func][0], graph)
            measurements_mean.append(mean)
            measurements_std.append(std)
        
        df[f'{func}_{saturation}_mean'] = measurements_mean
        df[f'{func}_{saturation}_std'] = measurements_std


        df.to_csv('hamilton.csv')
