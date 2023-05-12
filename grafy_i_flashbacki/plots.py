import matplotlib.pyplot as plt
import pandas as pd

k_n_df = pd.read_csv('k_n.csv')
t_n_df = pd.read_csv('t_n.csv')


k_g_df = pd.read_csv('k_g.csv')
t_g_df = pd.read_csv('t_g.csv')

plt.figure()
plt.errorbar([x for x in range(100,1100,100)],t_n_df['t_n_mean'],t_n_df['t_n_std'],marker='o', color='r')
plt.errorbar([x for x in range(100,1100,100)],t_g_df['t_g_mean'],t_g_df['t_g_std'],marker='o', color='b')
plt.title("Czas sortowania topologicznego dla algorytmu tarjana")
plt.xlabel("n")
plt.ylabel("t")
plt.legend(["macierz sąsiedztwa", "macierz grafu"])
plt.show()



# plt.errorbar([x for x in range(100,1100,100)],k_n_df['k_n_mean'],k_n_df['k_n_std'],marker='o', color='r')
# plt.errorbar([x for x in range(100,1100,100)],t_n_df['t_n_mean'],t_n_df['t_n_std'],marker='o', color='b')
# plt.title("Czas sortowania topologicznego dla macierzy sąsiedztwa")
# plt.xlabel("n")
# plt.ylabel("t")
# plt.legend(["algorytm kahna", "algorytm tarjana"])