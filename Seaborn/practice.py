import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

sns.set_style("whitegrid") # plt.style.use(--) -> Matplotlib
sns.set_context("notebook", font_scale = 1.0)

tips = sns.load_dataset("tips")
flights = sns.load_dataset("flights")
iris = sns.load_dataset("iris")

#---------------------------------------------------
#1 -> Histogram + KDE(Kernal Density Estimate) Plot
#---------------------------------------------------
# plt.figure(figsize = (8,3))
# sns.histplot(tips["total_bill"], kde = True)
# plt.title("Histogram + KDE from tips -> total bill")
# plt.show()

#---------------------------------------------------
#2 -> Scatter Plot with hue and size
#---------------------------------------------------
# plt.figure(figsize = (8,3))
# sns.scatterplot(data = tips, x = "total_bill", y = "tip", hue = "day", size = "size", sizes = (20, 200))
# plt.title("Tip VS Total_Bill")
# plt.show()

#---------------------------
# 3 -> Box + Swarm combined
#---------------------------
plt.figure(figsize = (10,5))
# sns.boxplot(data = tips, x = "day", y = "total_bill")
# sns.swarmplot(data = tips, x = "day", y = "total_bill", alpha = 0.6)
# plt.title("Boxplot with swarm overlay")
# plt.show()

#----------------------------------------------
# 4 -> Regression per smoker status (lmplot)
#----------------------------------------------
# sns.lmplot(data = tips, x = 'total_bill', y = 'tip', hue = 'smoker', height = 4, aspect = 2)
# plt.title('Linear Regression by Smoker status')
# plt.show()

#-----------------------------------------------
# 5 -> Correlation Heatmap
#------------------------------------------------
# corre = tips.select_dtypes(include = [np.number]).corr()
# sns.heatmap(corre, annot = True, cmap = 'coolwarm')
# plt.title('Correlation Heatmap')
# plt.show()

#-------------------------------------------------
# 6 -> FacetGrid Scatter plot by (lunch/Dinner)
#-------------------------------------------------
# g = sns.FacetGrid(tips, col = 'time', height = 4)
# g.map(sns.scatterplot, 'total_bill', 'tip')
# g.add_legend()
# plt.show() 


#-------------------------------------------------
# 7 -> Voilin plot
#-------------------------------------------------
# sns.violinplot(tips, x = 'day', y = 'total_bill', hue = 'sex', split = True)
# plt.title('Voilin plot of Total Bill by Day and Gender')
# plt.show()


#-------------------------------------------------
# 8 -> Pair plot
#-------------------------------------------------
# sns.pairplot(iris, hue = 'species', diag_kind = 'hist')
# plt.suptitle('Pairplot of Iris Dataset', y = 1.02)
# plt.show()

#-------------------------------------------------
# 9 -> Count Plot (frequency of categories)
#-------------------------------------------------
# sns.countplot(data = tips, x = 'day', hue = 'sex')
# plt.title('Count of records by day and sex')
# plt.show()

#-------------------------------------------------
# 10 -> Point plot (mean with confidence interval)
#-------------------------------------------------
sns.pointplot(data = tips, x = 'day', y = 'tip', hue = 'sex', dodge = True, markers = ['o', 's'], capsize = 0.1)
plt.title('Point plot (mean tip by day and sex)')
plt.show()

#-------------------------------------------------
# 11 -> Jiont plot (scatter + marginals)
#-------------------------------------------------
# sns.jointplot(data = tips, x = 'total_bill', y = 'tip', kind = 'reg', height = 6)
# plt.suptitle('Joint plot of total bill vs tip' , y = 1.02)
# plt.show()

#-------------------------------------------------
# 12 -> Strip plot (all point with jitter)
#-------------------------------------------------
# sns.stripplot(data = tips, x = 'day', y = 'tip', hue = 'sex', dodge = True, jitter = True, alpha = 0.7)
# plt.title('Strip plot of tips by day and sex')
# plt.show()

#-------------------------------------------------------
# 13 -> Residual plot (residuals from linear regression)
#--------------------------------------------------------
# plt.figure(figsize = (7,4))
# sns.residplot(data = tips, x = 'total_bill', y = 'tip', lowess = True)
# plt.title('Residual plot : tip ~ total bill')
# plt.show()

#----------------------------------------------------------
# 14 -> Heat map of pivoted data (time series like flights)
#----------------------------------------------------------
# fp = flights.pivot(index = 'month', columns = 'year', values = 'passengers')
# sns.heatmap(fp, annot = True, fmt = 'd', cmap = 'YlGnBu')
# plt.title('Heatmap of passenger by month and year')
# plt.show()