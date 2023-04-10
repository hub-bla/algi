import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('./measured_balance.csv')



plt.figure()

# plt.plot([x*10000 for x in range(1, 11)],data['Tworzenie drzewa AVL'], color='b')
# plt.errorbar([x*10000 for x in range(1, 11)],data['Tworzenie drzewa AVL'], data['std_AVL'],marker='o', color='b')
plt.plot([x*10000 for x in range(1, 11)], data['Balansowanie drzewa BST'], color='r')
plt.errorbar([x*10000 for x in range(1, 11)],data['Balansowanie drzewa BST'], data['std_BST'],marker='o', color='r')
plt.xlabel("n")
plt.ylabel("t [s]")
plt.title("Czas balansowania")
plt.legend(['BST'])
plt.grid()
plt.show()