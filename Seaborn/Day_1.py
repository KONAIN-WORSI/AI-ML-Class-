import seaborn as sns
import matplotlib.pyplot as plt

sns.set_style('darkgrid')
sns.set_context('notebook', font_scale = 1.0)

tips = sns.load_dataset("tips")

# Histogram with KDE combined
# plt.figure(figsize = (8,4))
# sns.histplot(tips['tip'], kde = True)
# plt.title('Histogram and KDE plot of Total Bill')
# plt.show()

# Scatter with hue and size
# plt.figure(figsize = (8,4))
# sns.scatterplot(data = tips, x = 'total_bill', y = 'tip', hue = 'day', size = 'size', sizes = (20,240))
# plt.title('Total_Bill VS Tip')
# plt.show()

# Box and swarm plot 
# plt.figure(figsize = (10, 5))
# sns.boxplot(data = tips, x = 'day', y = 'total_bill')
# sns.swarmplot(data = tips, x = 'day', y = 'total_bill', color = 'k', alpha = 0.7)
# plt.title('Box plot with swarm overlay')
# plt.show()