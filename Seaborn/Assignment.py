import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv(r'Seaborn/nepali_students_dataset.csv')

plt.figure(figsize = (8,4))
sns.histplot(df['CGPA'], bins = 10, kde = True)
plt.title('Histogram of CGPA of nepali students')
plt.show()

def z_score():
    mn = df.mean()
    sd = df.std()

    lower = mn - 3 * sd
    upper = mn + 3 * sd

    return df[(df['CGPA' >= lower]) & (df['CGPA'] <= upper)]

df = (
    df.pipe(z_score, 'CGPA')
)

print(df)

