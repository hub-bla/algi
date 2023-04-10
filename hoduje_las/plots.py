import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('./measured_minimum.csv')




plt.figure()

plt.plot(data['Tworzenie drzewa AVL'])
plt.errorbar(data.index,data['Tworzenie drzewa AVL'], data['std_AVL'],marker='o')
plt.plot(data['Tworzenie drzewa BST'])
plt.errorbar(data.index,data['Tworzenie drzewa BST'], data['std BST'],marker='o')
plt.xlabel("n")
plt.ylabel("t")
plt.title("Czas tworzenia drzew")
plt.legend()
plt.show()