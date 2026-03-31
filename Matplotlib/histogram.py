import matplotlib.pyplot as plt

plt.style.use('fivethirtyeight')

ages = [18, 19, 20, 21, 21, 22, 22, 23, 24, 24,
        25, 26, 26, 27, 28, 29, 30, 30, 31, 32]

plt.hist(ages, bins = 8, color = 'lightgreen', edgecolor = 'black')

plt.xlabel('Ages')
plt.ylabel('No of Students')
plt.title('Ages of Students')
plt.tight_layout()
plt.show()