import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('./measured_inorder.csv')



plt.figure()

plt.plot(data['Tworzenie drzewa AVL'], color='b')
plt.errorbar(data.index,data['Tworzenie drzewa AVL'], data['std_AVL'],marker='o', color='b')
plt.plot(data['Tworzenie drzewa BST'], color='r')
plt.errorbar(data.index,data['Tworzenie drzewa BST'], data['std_BST'],marker='o', color='r')
plt.xlabel("n")
plt.ylabel("t [s]")
plt.title("Czas inorder")
plt.legend(['BST'])
plt.show()