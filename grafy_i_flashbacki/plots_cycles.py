import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 1 plot for graph representation 
# 2 curves for algs on sat 50%
ham = pd.read_csv('hamilton.csv').drop('Unnamed: 0', axis=1)
new_ham =dict()
for col in list(ham.columns):
    if "std" not in col:
       new_ham[col] = ham[col]
new_ham = pd.DataFrame(new_ham)
ham_neigh = pd.read_csv('neigh_hamilton.csv')
ham_nexts = pd.read_csv('nexts_hamilton.csv')
euler = pd.read_csv('euler.csv').drop(['Unnamed: 0.1',"Unnamed: 0"], axis=1)

def first_plot(df_ham, df_eul, title):
    sat_50_ham = None
    sat_50_eul = None
    cols_ham = list(df_ham.columns)
    cols_eul = list(df_eul.columns)
    for i in range(len(cols_ham)):
        if "0.5" in cols_ham[i]:
            sat_50_ham = df_ham[cols_ham[i]]
            sat_50_eul = df_eul[cols_eul[i]]
            break

    plt.figure()
    plt.title(title)
    plt.plot([x for x in range(10, 20)],sat_50_ham)
    plt.plot([x for x in range(10, 20)], sat_50_eul)
    plt.legend(['macierz sąsiedztwa', 'lista następników'])
    plt.xlabel("n")
    plt.ylabel("t")
    plt.show()

# first_plot(new_ham.iloc[:, 9:], new_ham.iloc[:, :9], "Zajdowanie cyklu  przy nasyceniu 50%")
# print(ham_nexts.iloc[2,1:])
print(euler)
def second_plot(sats1, title):
   

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    n = [[x for x in range(10, 20)] for i in range(9)]
    t = sats1
    s = [[x/100 for x in range(0, 100,10)] for i in range(9)]
    n2 = np.append(0, np.array(n).flatten())
    s2 = np.append(0, np.array(s).flatten())
    t2 = np.append(0, np.array(t).flatten())

    N,S = np.meshgrid(n, s)
    print(len(n[0]), t.shape[0], len(s[0]))
    ax.plot_trisurf(n2, s2,t2, color='red')
    # print(len([x for x in range(10, 20)]), sats1.shape, len([[x/100 for x in range(0, 100,10)] for i in range(9)]))
    
    # ax.plot_trisurf([x for x in range(11, 20)], sats2, [x/100 for x in range(10, 100,10)])
    # ax.legend([surf], ['euler'])
    ax.set_xticklabels([x for x in range(10, 20)])
    ax.set_yticklabels([x/100 for x in range(0, 100,10)])
    ax.set_xlabel("n")
    ax.set_ylabel("s")
    ax.set_zlabel("t")
    ax.set_title(title)
    plt.show()
second_plot(new_ham.iloc[:,9:].to_numpy(), "Znajdowanie cyklu hamiltona w macierzy sąsiedztwa")