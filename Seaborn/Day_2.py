import seaborn as sns
import matplotlib.pyplot as plt

sns.set_style('darkgrid')
sns.set_context('notebook', font_scale = 1.0)

tips = sns.load_dataset("tips")

# Violin plot
# plt.figure(figsize = (8,4))
# sns.violinplot(data = tips, x = 'day', y = 'tip', hue = 'sex')
# plt.title('Violin plot of total bill by day and sex')
# plt.show()

# Count plot
# plt.figure(figsize = (8,4))
# sns.countplot(data = tips, x = 'day', hue = 'sex')
# plt.title('Count plot of records of day and sex')
# plt.show()

# Facet grid plot
plt.figure(figsize = (8,4))
# g = sns.FacetGrid(tips, row = 'time', col = 'sex')
# g.map(sns.histplot,'total_bill', bins = 10)
# plt.show()

# Lmplot
sns.lmplot(data = tips, x = 'total_bill', y = 'tip', hue = 'sex')
plt.title('Lmplot of total bill and tips')
plt.show()