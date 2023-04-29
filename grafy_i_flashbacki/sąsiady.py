import pandas as pd
import numpy as np

def create_neighbours_matrix_directed_without_cycles(matrix_edge:int)->pd.DataFrame:
    '''SATURATION 50%'''
    neighbours = pd.DataFrame(columns=[x for x in range(matrix_edge)])
    n_of_edges = (matrix_edge*(matrix_edge-1))/2
    n_imp = [1 for x in range(matrix_edge-1)]
    ones = int((n_of_edges//2)- len(n_imp))
    zeros = int(n_of_edges - n_of_edges//2)
    arr_of_ones = np.ones(shape=ones).astype('int32')
    arr_of_zeros = np.zeros(shape=zeros).astype('int32')

    zeros_and_ones =  np.concatenate((arr_of_ones, arr_of_zeros), axis=None) 

    np.random.shuffle(zeros_and_ones)
    print(zeros_and_ones)
    for i in range(0, matrix_edge):
        row = np.zeros(shape=matrix_edge).astype('int32')
        is_added = False
        for j in range(i+1, matrix_edge):
            if is_added is not True:
                row[j] = n_imp[0]
                n_imp = n_imp[1:]
                is_added = True
            else:
                row[j] = zeros_and_ones[0]
                zeros_and_ones = zeros_and_ones[1:]

        neighbours.loc[str(i)] = pd.Series(row)


    return neighbours


graph = create_neighbours_matrix_directed_without_cycles(10)

print(graph)

