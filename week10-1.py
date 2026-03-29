#24331A05E2
#to import data from CSV to DataFrame and inspect data in DataFrame using head(), tail (), info() and describe() functions in pandas.
import pandas as pd
data = {
    'Name': ['Chandu', 'Abhi', 'Maggie', 'Charan'],
    'Age': [19, 20, 23, 18],
    'Marks': [90, 88, 92, 80],
    'Fav subject': ['Biology','mathematics','chemistry','physics']
}
df = pd.DataFrame(data)
print("\nFirst 2 rows:")
print(df.head(2))
print("\nlast row:")
print(df.tail(1))
print("Using info():\n")
print(df.info())
print("Using describe():")
print(df.describe())
