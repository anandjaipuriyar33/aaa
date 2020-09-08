#load library
import pandas as pd
import numpy as np
from statistics import mode

#create data frame
dataframe = pd.read_csv("titanic-1.csv")


print(dataframe)

print(dataframe.shape)
print(dataframe.describe())

print(dataframe['Survived'].value_counts())
print(dataframe['SexCode'].value_counts())
print(dataframe['PClass'].value_counts())
print(dataframe['Sex'].value_counts())

print(dataframe['Sex'].unique())
print(dataframe['Sex'].nunique())
print(dataframe['PClass'].nunique())



print(dataframe.iloc[0:5,0:3])

print(dataframe.iloc[[0,3,5],[0,3]])

print(dataframe.iloc[[0,3,6,24], [0,2,4]])

print(dataframe.loc[:,'Survived':'SexCode'])

print()

dataframe= dataframe.set_index(dataframe['Name'])
print(dataframe.loc['17'])


dataframe['Sex']=dataframe['Sex'].replace("F", "female")
dataframe['Sex']=dataframe['Sex'].replace("M", "male")
print(dataframe['Sex'].value_counts())

print(dataframe['Sex'].value_counts())
print(dataframe['Sex'].replace(["female", "male"], ["Woman", "Man"]))
print(dataframe['Sex'].value_counts())
print(dataframe.drop('SexCode', axis=1))
dataframe=dataframe[dataframe['PClass'] != '*']

print('Maximum:', dataframe['Age'].max())
print('Minimum:', dataframe['Age'].min())
print('Mean:', dataframe['Age'].mean())
print('Sum:', dataframe['Age'].sum())
print('Count:', dataframe['Age'].count())


print(dataframe.isna().sum())

dataframe['Sex']=dataframe['Sex'].replace(np.nan, "Gender Unknown")

print(dataframe.isna().sum())

dataframe['Age']=dataframe['Age'].fillna(dataframe['Age'].mean())
dataframe['Sex']=dataframe['Sex'].fillna(mode(dataframe['Sex']))

print(dataframe.describe())

print(dataframe['Survived'].value_counts())
print(dataframe['SexCode'].value_counts())
print(dataframe['PClass'].value_counts())

print(dataframe)
print(dataframe.rename(columns))

#deleting a column axis =1,row axis=0

print(df.rename(columns={'PClass': 'Passenger Class'}).head(2))


print(dataframe.drop('SexCode', axis=1))

print(len(dataframe))
print(len(dataframe.drop_duplicates()))
print(len(dataframe.drop_duplicates(subset=['Sex'])))
print(len(dataframe.drop_duplicates(subset=['Sex'], keep='last')))
#permanently delete from data
#dataframe=dataframe.drop('SexCode', axis=1)

print(dataframe.groupby('PClass') .mean())
print(dataframe.groupby(['PClass','Survived'])['Name'].count())

print(dataframe.groupby(['Sex','Survived'])['Name'].count())

def uppercase(x):
    return(x.upper())

print(dataframe['Name'].apply(uppercase())[0:2])

for name in dataframe['Name'][0:2]:
    print(name.upper())

#1. reduntant entries in 'sex' column(eg: M and Male both are used)
#2. Redundant sexcode column
#3. 500 values of age was missing
#4. '*' value was there in pclass column by mistake.
#5. 5 entries in sex column are missing





