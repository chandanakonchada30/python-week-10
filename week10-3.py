#24331A05E2
#to perform dataframe modification and data cleaning in pandas.
import pandas as pd
data = {
    'Name': ['Chandu', 'Abhi', 'Maggie', 'Charan'],
    'Age': [19, 20, 23, 18],
    'Marks': [90, 88, 92, 80],
    'Fav subject': ['Biology','mathematics','chemistry','physics']
}
df = pd.DataFrame(data)
df['Age'] = df['Age'].fillna(df['Age'].mean())
df['Marks'] = df['Marks'].fillna(0)
df['Grade'] = ['B', 'A', 'C', 'B']
df.loc[df['Marks'] > 85, 'Grade'] = 'A'
print(df)