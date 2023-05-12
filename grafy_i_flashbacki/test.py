from load_graph import load_neigh, nexts_dict
from sąsiady import create_neighbours_matrix_directed_without_cycles, create_neigh_with_specific_saturation, nexts_dict_generator
import pandas as pd
import random


def isValid(v, i, neigh_matrix, track):
    if (neigh_matrix[track[i-1]][v] == 0):
        return False
    elif v  in track:
            return False
    return True

def cycle_finding(node, neigh_matrix, track):

    if (node == len(neigh_matrix)):
        if (neigh_matrix[track[node-1]][track[0]]==1):
            
            return True
        return False

    for node2 in range(len(neigh_matrix)):
        if isValid(node2, node, neigh_matrix, track):
            track[node] = node2
            if (cycle_finding(node+1, neigh_matrix, track) is True):
                return True
            track[node] = -1
    
    return False

def hamilton_neigh(neigh_matrix):
    track = [-1]*len(neigh_matrix)
    track[0] = 0
    if cycle_finding(neigh_matrix, track) is True:
        print(track)
    else:
        print("Graf nie zawiera cyklu")

def cycle_finding_in_nexts(node, nexts, track):
    track.append(node)
   
    for node2 in nexts.keys():
       
        if node2 in nexts[node] and node2 not in track: 

            if (cycle_finding_in_nexts(node2, nexts, track) is True):
                return True
    if len(track) == len(nexts.keys()):
        if 0 in nexts[node]:
            track.append(0)
            return True
        track.remove(node)
        return False
    track.remove(node)
    return False

def hamilton_nexts(nexts):

    track = []
    if cycle_finding_in_nexts(0, nexts, track):
        print(track)
    else:
        print("Graf nie zawiera cyklu")

def all_degrees_zero(degrees):
    for degree in degrees:
        if degree !=0:
            return False
    return True

def find_euler_neigh(node, neigh_matrix, degrees, track, edges):
    track.append(node)

    for node2 in range(len(neigh_matrix[node])):
        if neigh_matrix[node][node2] == 1 and ((node2, node) not in edges and (node, node2) not in edges) :
            edges.append((node, node2))
            
            degrees[node] -=1
            degrees[node2] -=1
            if find_euler_neigh(node2, neigh_matrix, degrees, track, edges):
                    return True
            degrees[node] +=1
            degrees[node2] +=1
            edges.remove((node,node2))
    if all_degrees_zero(degrees):
        return True
    
    return False
       
    
def euler_neigh(neigh_matrix):
    first_even = None
    degrees = [0] * len(neigh_matrix)
    for i in range(len(neigh_matrix)):
        for j in range(i,len(neigh_matrix)):
            degrees[i] += neigh_matrix[i][j]
            degrees[j] += neigh_matrix[j][i]
        if first_even is ModuleNotFoundError and degrees[i]%2==0:
            first_even = i
    edges = []
    track = []
    if first_even is None:
        first_even = random.choice(degrees)
    if find_euler_neigh(first_even, neigh_matrix, degrees, track, edges):
        print(track)
    else:
        print("Brak cyklu")


def check_condition(nexts):
    degrees_in =[0] * len(nexts.keys())
    degrees_out = [0] * len(nexts.keys())
    #degrees_out
    for node1 in range(len(nexts.keys())):
        degrees_out[node1]  = len(nexts[node1])
        #degrees_in
        for node2 in  range(len(nexts.keys())):
                for node3 in nexts[node2]:
                     if node3==node1:
                        degrees_in[node1] +=1
        if degrees_out[node1]!=degrees_in[node1]:
            return False
    return True
def find_euler_nexts(node, nexts, track):
    track.append(node)
    for node2 in nexts[node]:
            nexts[node].pop(0)
            find_euler_nexts(node2, nexts, track)
    
    
def euler_nexts(nexts):
    copy_of_nexts = nexts.copy()
    track = []
    if check_condition(copy_of_nexts):
        find_euler_nexts(0, copy_of_nexts, track)
        print(track)
    else:
        print("Brak cyklu")



neigh = load_neigh("euler.txt")
neigh2 = create_neigh_with_specific_saturation(20, 0.1)
nexts = nexts_dict("euler.txt")
nexts2 = nexts_dict_generator(30, 0.1)
euler_nexts(nexts)
euler_neigh(neigh)
# euler_nexts(nexts2)
# hamilton_nexts(nexts)
# print(pd.DataFrame(neigh))
# hamilton_neigh(neigh)
# for i in range(10,1000):
#     neigh2 = create_neigh_with_specific_saturation(i, 0.5)
#     nexts2 = nexts_dict_generator(i, 0.5)
#     euler_neigh(neigh2)
#     euler_nexts(nexts2)