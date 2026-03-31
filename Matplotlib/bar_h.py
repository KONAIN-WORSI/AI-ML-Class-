import pandas as pd
from collections import Counter
import matplotlib.pyplot as plt

plt.style.use('fivethirtyeight')

data = pd.read_csv('Language_data.csv')
ids = data['Responder_id']
language_response = data['LanguagesWorkedWith']

language_counter = Counter()

for response in language_response:
    language_counter.update(response.split(';'))

most_repeated = language_counter.most_common(10)

language = []
popularity = []

for item in most_repeated:
    language.append(item[0])
    popularity.append(item[1])

language.reverse()
popularity.reverse()

plt.barh(language, popularity,)

plt.title('Top 10 Most Popular Language')
plt.xlabel('No of people who use')
plt.tight_layout()
plt.show()