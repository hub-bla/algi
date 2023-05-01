import pandas as pd
import numpy as np
import math
def same_merge(x):
    for i in x.index:
        if x.iloc[i] > 0:
            return 1
    return 0
def load_neigh(file_name:str, directed=False)->list:
    file = open(file_name, 'r')
    lines = file.readlines()
    num_nodes, num_edges = map(int, lines[0].split(' '))
    neigh = [[0 for i in range(num_nodes)]for j in range(num_nodes)]
    lines = lines[1:]
    for line in lines:
        i_node1, i_node2 = map(int, line.split(' '))
        if directed is  True:

            neigh[i_node1][i_node2] = 1
            neigh[i_node2][i_node1] = -1

        else:
            neigh[i_node1][i_node2] = 1
            neigh[i_node2][i_node1] = 1

    return neigh    

def incident_matrix(file_name:str, directed=False)->list:
    file = open(file_name, 'r')
    lines = file.readlines()
    num_nodes, num_edges = map(int, lines[0].split(' '))
    lines = lines[1:]
    incident = [[0 for i in range(num_edges)]for j in range(num_nodes)]
    for edge_num, line in enumerate(lines):
        i_node1, i_node2 = map(int, line.split(' '))
        if directed:

            incident[i_node1][edge_num] = -1
        else:
            incident[i_node1][edge_num] = 1 
        incident[i_node2][edge_num] = 1
    return incident
# lista następników

def edge_matrix(file_name:str):
    file = open(file_name, 'r')
    lines = file.readlines()
    num_nodes, num_edges = map(int, lines[0].split(' '))
    lines = lines[1:]
    edge_matrix= []
    for i, line in enumerate(lines):
        i_node1, i_node2 = map(int, line.split(' '))
        if ((i_node2, i_node1) not in edge_matrix):
            edge_matrix.append((i_node1, i_node2))

    return edge_matrix


def nexts_dict(file_name:str):
    edges = edge_matrix(file_name)
    file = open(file_name, 'r')
    lines = file.readlines()
    num_nodes, num_edges = map(int, lines[0].split(' '))
    nexts = dict()

    lines = lines[1:]
    for i in range(num_nodes):
        nexts[i] = []
    for edge in lines:
        node, nxt = map(int, edge.split(' '))
        nexts[node].append(nxt)
        nexts[node].sort()
    return nexts


def previous_dict(file_name:str)->list:
    file = open(file_name, 'r')
    lines = file.readlines()
    num_nodes, num_edges = map(int, lines[0].split(' '))
    previous = dict()
    lines = lines[1:]
    for i in range(num_nodes):
        previous[i] = []
    for edge in lines:
        prev, node = map(int, edge.split(' '))
        if node not in previous.keys():
            previous[node] = []
            previous[node].append(prev)
        else:
            previous[node].append(prev)
        previous[node].sort()
    return previous
def incident_dict(file_name:str)->list:
    previous = previous_dict(file_name)
    nexts = nexts_dict(file_name)
    incident = dict()
    for node in previous.keys():
        incident[node] =[]
        [incident[node].append(value) for value in previous[node]]
        [incident[node].append(value) for value in nexts[node]]
        incident[node] = list(set(incident[node]))
    return incident

def no_incident(file_name:str)->list:
    file = open(file_name, 'r')
    lines = file.readlines()
    num_nodes, num_edges = map(int, lines[0].split(' '))
    incident_dic = incident_dict(file_name)
    no_incident_dict = dict()
    for node in incident_dic.keys():
        no_incident_dict[node] = []
        [no_incident_dict[node].append(i)  for i in range(num_nodes) if i not in incident_dic[node]]
    return no_incident_dict



def graph_matrix(file_name:str)->list:
    file = open(file_name, 'r')
    lines = file.readlines()
    num_nodes, num_edges = map(int, lines[0].split(' '))
    no_incident_dict = no_incident(file_name)
    previous = previous_dict(file_name)
    nexts = nexts_dict(file_name)
    graph_matrix = np.empty((num_nodes, num_nodes+3))
    graph_matrix[:] = np.nan
    for node in no_incident_dict.keys():
        if nexts[node] != []:
            nxt = nexts[node][0]
            last_nxt = nexts[node][-1]
            graph_matrix[node][num_nodes] = nxt
            for i in nexts[node]:
                graph_matrix[node][i] = last_nxt
        if previous[node] !=[]:
            first_prv = previous[node][0]
            last_prv = previous[node][-1]
            graph_matrix[node][num_nodes+1] = first_prv
            for i in previous[node]:
                graph_matrix[node][i] = last_prv+num_nodes
        if no_incident_dict !=[]:
            first_no_inc = no_incident_dict[node][0]
            last_no_inc= no_incident_dict[node][-1]
            graph_matrix[node][num_nodes+2] = first_no_inc
            for i in no_incident_dict[node]:
                graph_matrix[node][i] = last_no_inc * (-1)

    return graph_matrix.astype('int32')

def traverse_dfs_neigh(neigh_matrix:np.array, node:int, visited:list):
    visited[node] = True
    print(node)
    for node2 in range(neigh_matrix[node].shape[0]):
        if visited[node2] is False and neigh_matrix[node][node2] == 1:
            traverse_dfs_neigh(neigh_matrix, node2, visited)
        

def dfs_neigh_matrix(neigh_df:pd.DataFrame):
    neigh_matrix = neigh_df.to_numpy()
    visited = [False for i in range(neigh_matrix.shape[0])]
    for node in range(neigh_matrix.shape[0]):
        if False not in visited:
            break
        traverse_dfs_neigh(neigh_matrix, node, visited)


def traverse_dfs_graph_m(graph_mtrx, node, visited):
    visited[node] = True
    print(node)
    for i in range(len(visited)):
        node2 = graph_mtrx[node][i]
        if np.isnan(node2) != True:
            if 0<= node2 and node2 < len(visited) and visited[i] is False:
            
                traverse_dfs_graph_m(graph_mtrx, i, visited)
       
        if False not in visited:
            break
def dfs_graph_matrix(graph_df:pd.DataFrame):
    graph_mtrx = graph_df.to_numpy()
    visited = [False for i in range(graph_mtrx.shape[0])]
    for node in range(graph_mtrx.shape[0]):
        if False not in visited:
            break
        if visited[node] is False:
            traverse_dfs_graph_m(graph_mtrx, node, visited)


def kahn_neigh(neigh_matrix):
    degrees = [0]*neigh_matrix.shape[0]
    for node1 in range(neigh_matrix.shape[0]):
        for node2 in neigh_matrix[node1]:
            if node2 == -1:
                degrees[node1] +=1
    

    queue = []
    for node in range(neigh_matrix.shape[0]):
        if degrees[node]==0:
            queue.append(node)

    count = 0

    topological_order=[]

    while queue:
        node = queue.pop(0)
        degrees[node]= None
        topological_order.append(node)
        for node2 in range(neigh_matrix[node].shape[0]):
            if neigh_matrix[node2][node] == -1:
                degrees[node2] -=1
            if degrees[node2]==0 and node!=node2:
                degrees[node2]= None
                queue.append(node2)
        count+=1
    if count != neigh_matrix.shape[0]:
        print("Cykle w grafie")
    else:
        print(topological_order)



def kahn_graph(graph_matrix):
    degrees = [0]*graph_matrix.shape[0]

    for node1 in range(graph_matrix.shape[0]):
        for node2 in range(graph_matrix[node1].shape[0]-3):
            if graph_matrix[node1][node2]>=graph_matrix.shape[0]:
                degrees[node1] +=1
    
    queue = []
    for node in range(graph_matrix.shape[0]):
        if degrees[node]==0:
            queue.append(node)

    count = 0
    topological_order=[]

    while queue:
        node = queue.pop(0)
        degrees[node]= None
        topological_order.append(node)
        for node2 in range(graph_matrix.shape[0]):
            if graph_matrix[node2][node]>=graph_matrix.shape[0]:
                degrees[node2] -=1
            if degrees[node2]==0 and node!=node2:
                degrees[node2]= None
                queue.append(node2)
        count+=1
    if count != graph_matrix.shape[0]:
        print("Cykle w grafie")
    else:
        print(topological_order)

neigh = load_neigh('przykładowy_graf.txt', directed=True)
graph_mtrx = graph_matrix('przykładowy_graf.txt')

neigh_df = pd.DataFrame(neigh)
neigh_df = neigh_df.replace({pd.NA: np.nan})
graph_matrix_df = pd.DataFrame(graph_mtrx).apply(lambda x: x.replace(to_replace=-2147483648, value =None) )
# dfs_graph_matrix(graph_matrix_df)
# kahn_neigh(neigh_df.to_numpy())
kahn_graph(graph_mtrx)
# print("Neigh:")
# print(neigh_df)
# print("Graph matrix:")
# print(graph_matrix_df)