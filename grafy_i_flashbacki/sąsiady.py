import pandas as pd
import numpy as np
import random
import itertools
import math


def create_neighbours_matrix_directed_without_cycles(matrix_edge:int)->pd.DataFrame:
    '''SATURATION 50%'''
    neigh = [[0 for i in range(matrix_edge)]for j in range(matrix_edge)]
    n_of_edges = (matrix_edge*(matrix_edge-1))/2
    ones = int(n_of_edges//2)
    zeros = int(n_of_edges - n_of_edges//2)
    arr_of_ones = np.ones(shape=ones).astype('int32')
    arr_of_zeros = np.zeros(shape=zeros).astype('int32')

    zeros_and_ones =  np.concatenate((arr_of_ones, arr_of_zeros), axis=None) 

    np.random.shuffle(zeros_and_ones)
    for i in range(0, matrix_edge):
        for j in range(0, i):
            neigh[i][j] = zeros_and_ones[0]
            neigh[j][i] = neigh[i][j]*(-1)
            zeros_and_ones = zeros_and_ones[1:]



    return pd.DataFrame(neigh)

def create_neigh_with_specific_saturation(matrix_edge, sat, directed=False):
    neigh = [[0 for i in range(matrix_edge)]for j in range(matrix_edge)]
    n_of_edges = 0
    if (directed is True):
        n_of_edges = (matrix_edge*(matrix_edge-1))
    else:
        n_of_edges= (matrix_edge*(matrix_edge-1))/2
   
    ones = int(n_of_edges* sat) 
    zeros =int( n_of_edges - ones)
    arr_of_ones = np.ones(shape=ones).astype('int32')
    arr_of_zeros = np.zeros(shape=zeros).astype('int32')
    zeros_and_ones =  np.concatenate((arr_of_ones, arr_of_zeros), axis=None) 
    np.random.shuffle(zeros_and_ones)
    for i in range(0, matrix_edge):
        for j in range(0, i):
            if directed is True:
                direction = random.choice([-1,1])
                neigh[i][j] = zeros_and_ones[0] * direction
                neigh[j][i] = neigh[i][j] *(-1)
            else:
                neigh[i][j] = zeros_and_ones[0]
                neigh[j][i] = zeros_and_ones[0]
            zeros_and_ones = zeros_and_ones[1:]
    return pd.DataFrame(neigh)


def nexts_dict(n):
    neigh = create_neighbours_matrix_directed_without_cycles(n).to_numpy()
    nexts = dict()
    for i in range(neigh.shape[0]):
        nexts[i] = []
    for node in range(neigh.shape[0]):
        for node2 in range(neigh.shape[0]):
            if neigh[node][node2] == 1:
                nexts[node].append(node2)
    return nexts

def nexts_dict_generator(n, sat):
    neigh = create_neigh_with_specific_saturation(n, sat, directed=True)

    nexts = dict()
    for i in range(neigh.shape[0]):
        nexts[i] = []
    for node in range(neigh.shape[0]):
        for node2 in range(neigh.shape[0]):
            if neigh[node][node2] == 1:
                nexts[node].append(node2)
    return nexts


def previous_dict(n)->list:
    neigh = create_neighbours_matrix_directed_without_cycles(n).to_numpy()
    previous = dict()
    for i in range(neigh.shape[0]):
        previous[i] = []
    for node in range(neigh.shape[0]):
        for node2 in range(neigh.shape[0]):
            if neigh[node][node2] == -1:
                previous[node].append(node2)
            
        previous[node].sort()
    return previous

def incident_dict(n)->list:
     
    previous = previous_dict(n)
    nexts = nexts_dict(n)
    incident = dict()
    for node in previous.keys():
        incident[node] =[]
        [incident[node].append(value) for value in previous[node]]
        [incident[node].append(value) for value in nexts[node]]
        incident[node] = list(set(incident[node]))
    return incident


def no_incident(n)->list:
    
    incident_dic = incident_dict(n)
    no_incident_dict = dict()
    for node in incident_dic.keys():
        no_incident_dict[node] = []
        [no_incident_dict[node].append(i)  for i in range(n) if i not in incident_dic[node]]
    return no_incident_dict


def graph_matrix(n)->list:
    
    no_incident_dict = no_incident(n)
    previous = previous_dict(n)
    nexts = nexts_dict(n)
    graph_mtx = np.empty((n, n+3))
    graph_mtx[:] = np.nan
    for node in no_incident_dict.keys():
        if nexts[node] != []:
            nxt = nexts[node][0]
            last_nxt = nexts[node][-1]
            graph_mtx[node][n] = nxt
            for i in nexts[node]:
                graph_mtx[node][i] = last_nxt
        if previous[node] !=[]:
            first_prv = previous[node][0]
            last_prv = previous[node][-1]
            graph_mtx[node][n+1] = first_prv
            for i in previous[node]:
                graph_mtx[node][i] = last_prv+n
        if no_incident_dict !=[]:
            first_no_inc = no_incident_dict[node][0]
            last_no_inc= no_incident_dict[node][-1]
            graph_mtx[node][n+2] = first_no_inc
            for i in no_incident_dict[node]:
                graph_mtx[node][i] = (last_no_inc * (-1)) -1
    graph_mtx.astype('int32')
    return pd.DataFrame(graph_mtx).apply(lambda x: x.replace(to_replace=-2147483648, value =None) )
