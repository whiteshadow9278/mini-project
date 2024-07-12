import pandas as pd
df=pd.read_csv("titanic.csv")
df.head()

df.isna().sum()

df['Age'].fillna(df['Age'].mean(),inplace=True)

df['Embarked']=df['Embarked'].aspect('category')
df['Embarked']=df['Embarked'].cat.codes
df['Embarked'].finallna(df['Embarked'].mode(),inplace=true)
df.drop(['Cabin'],axis=1)
df.drop(df[(df['Name']=="Braund,Mr.Owen Harris")].index,inplace=True)
df.drop(df[(df['PassengerId']==5)].index,inplace=True)
