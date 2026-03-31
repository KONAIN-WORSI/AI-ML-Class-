import seaborn as sns
import matplotlib.pyplot as plt

sns.set_style('darkgrid')
sns.set_context('notebook', font_scale = 1.0)

tips = sns.load_dataset("tips")
flights = sns.load_dataset('flights')

# Point plot
plt.figure(figsize = (8,4))
# sns.pointplot(data = tips, x = 'day', y = 'total_bill', hue = 'sex', dodge = True, markers = ['x', 's'], capsize = 0.09)
# plt.title('Point plot of average of total bill bby day')
# plt.show()

# Correlation Heatmap
# coore = tips.corr(numeric_only = True)

# sns.heatmap(coore,annot = True,cmap = 'coolwarm', fmt = '.2f')
# plt.title('Correlation Heatmap of tips dataset')
# plt.show()

# Pivot heatmap
x = flights.pivot_table(index = 'year', columns = 'month', values = 'passengers')
sns.heatmap(x, annot = True, fmt = '.0f', cmap = 'coolwarm')
plt.title('Heat map of passenger by month and year')
plt.show()