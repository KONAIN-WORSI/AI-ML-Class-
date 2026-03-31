import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('fivethirtyeight')

data = pd.read_csv('likes_dataset.csv')

views_count = data['view_count']
likes = data['likes']
ratio = data['ratio']

plt.scatter(views_count, likes, c = ratio, cmap = 'RdYlBu_r', edgecolors = 'black', linewidths = 0.7, alpha = 0.7)

cbar = plt.colorbar()
cbar.set_label('Like / Dislike Ratio')

plt.xscale('log')
plt.yscale('log')

plt.title('Trending Youtube videos')

plt.xlabel('Total View Count')
plt.ylabel('Total Likes')

plt.tight_layout()
plt.show()
