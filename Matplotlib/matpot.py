from matplotlib import pyplot as plt

plt.style.use('fivethirtyeight')

labels = ['Java Script', 'HTML/CSS', 'SQL', 'Python', 'Java']

slices = [59219, 55466, 47544, 36443, 32917]
explode = [0, 0, 0, 0.1, 0]


plt.pie(slices, labels= labels, explode = explode,shadow = True, startangle = 150, autopct ='%1.1f%%')

plt.title('Pie chart')
plt.tight_layout()
plt.show()