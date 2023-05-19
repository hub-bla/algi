import time
import matplotlib.pyplot as plt
import sąsiady
from sąsiady import create_neigh_with_specific_saturation, nexts_dict_generator
from load_graph import kahn_graph, kahn_neigh, tarjan_graph, tarjan_neigh
import numpy as np
import pandas as pd
from cycles import hamilton_neigh, hamilton_nexts, euler_neigh, euler_nexts
k = [_ for _ in range(10, 20)]
saturations = [i/100 for i in range(10, 100, 10)]
print(saturations)
funcs = {"h_nxts": [hamilton_nexts,nexts_dict_generator], "h_neigh": [hamilton_neigh,create_neigh_with_specific_saturation]}



def measure(func, generator, g_size, saturation):
    measurements = []
    for i in range(5):
        print(f'Graph size:{g_size}, Saturation: {saturation}')
        graph = generator(g_size, saturation)
        start = time.time()
        func(graph)
        end = time.time()
        measurements.append((end-start))
    return np.mean(measurements), np.std(measurements)



df = pd.DataFrame()
funcs_ke = funcs.keys()
for func in funcs.keys():
    for saturation in saturations:
        print("Working...")
        measurements_mean = []
        measurements_std = []
        for g_size in k:
            
            
            mean, std = measure(funcs[func][0], funcs[func][1], g_size, saturation)
            measurements_mean.append(mean)
            measurements_std.append(std)
        
        df[f'{func}_{saturation}_mean'] = measurements_mean
        df[f'{func}_{saturation}_std'] = measurements_std


        df.to_csv('hamilton.csv')
