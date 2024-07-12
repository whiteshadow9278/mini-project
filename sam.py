import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('titanic.csv')

# Visualizing missing values
sns.heatmap(data.isna())
plt.show()

# Histogram of 'Sex'
g = sns.histplot(x='Sex', data=data)
plt.show()

# Countplot of 'Embarked' with 'Pclass'
g = sns.countplot(x='Embarked', hue='Pclass', data=data)
plt.show()

# Feature Engineering: Adding 'FamilySize'
def add_family(df):
    df['FamilySize'] = df['SibSp'] + df['Parch'] + 1
    return df

data = add_family(data)
data.head(10)

# Countplot of 'FamilySize' with 'Survived'
g = sns.countplot(x='FamilySize', hue='Survived', data=data)
plt.show()

# Categorical plot of 'Embarked' with 'Sex' and 'Survived'
g = sns.catplot(x="Embarked", hue="Sex", col="Survived", data=data, kind="count", height=4, aspect=.7)
plt.show()
