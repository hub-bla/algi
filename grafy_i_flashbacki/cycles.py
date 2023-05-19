from load_graph import load_neigh, nexts_dict
from sąsiady import create_neighbours_matrix_directed_without_cycles, create_neigh_with_specific_saturation, nexts_dict_generator
import pandas as pd
from load_graph import tarjan_neigh
import random

random.seed(1)

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
    if cycle_finding(0, neigh_matrix, track) is True:
        track.append(0)
        print(track)
    else:
        print("Graf nie zawiera cyklu")


def isValid_nexts(v, i, nexts, track):
    node = track[i-1]
    if ((node !=-1)and( v not in nexts[node])):
        return False
    elif v  in track:
            return False
    return True

def cycle_finding_in_nexts(node, nexts, track):
    if (node == len(nexts)):
        if (track[0] in nexts[track[node-1]]):
            
            return True
        return False

    for node2 in nexts.keys():
       if isValid_nexts(node2, node,nexts,track): 
            track[node] = node2
            if (cycle_finding_in_nexts(node+1, nexts, track) is True):
                return True
            track[node] = -1
    
    return False

def hamilton_nexts(nexts):

    track = [-1] * len(nexts.keys())
    if cycle_finding_in_nexts(0, nexts, track):
        track.append(0)
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
    euler  = True
    degrees = [0] * len(neigh_matrix)
    for i in range(len(neigh_matrix)):
        for j in range(i,len(neigh_matrix)):
            degrees[i] += neigh_matrix[i][j]
            degrees[j] += neigh_matrix[j][i]
        if degrees[i]%2!=0:
            euler = False
            
    edges = []
    track = []
    
    if euler and find_euler_neigh(len(neigh_matrix)-1, neigh_matrix, degrees, track, edges):
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

def find_euler_nexts(node, nexts, track, stack):
    w = node
    stack.append(w)
    while len(nexts[w]) != 0:
        w = nexts[w].pop(0)
        stack.append(w)
        if node==w:
            break

    w = stack.pop(-1)
    while True:
        if len(nexts[w]) == 0:
            track.append(w)
        else:
            find_euler_nexts(w, nexts, track, stack)
        w = stack.pop(-1)
        if w==node:
            break
    track.append(node)
  
       
    
    
def euler_nexts(nexts):
    copy_of_nexts = nexts.copy()
    stack = []
    track = []
    if check_condition(copy_of_nexts):
        find_euler_nexts(len(nexts.keys())-1, copy_of_nexts, track, stack)
        print(track)
    else:
        print("Brak cyklu")
    
    
neigh_h = load_neigh("directed_hamilton.txt")
nexts_h = nexts_dict("directed_hamilton.txt")
neigh_e = load_neigh("undirected_euler.txt")
nexts_e = nexts_dict("directed_euler.txt")


print("EULER SASIEDZTWA")
euler_neigh(neigh_e)
print("EULER NASTEPNIKI")
euler_nexts(nexts_e)

print("HAMILTON SASIEDZTWA")
hamilton_neigh(neigh_h)
print("HAMILTON NASTEPNIKI ")
hamilton_nexts(nexts_h)

#