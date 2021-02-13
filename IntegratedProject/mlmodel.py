import numpy as np
import pandas as pd
import pickle
from sklearn import metrics

dataset = pd.read_csv('abc.csv')

dataset.drop('NAME OF THE COMPANY', axis=1, inplace=True)

X = dataset.loc[:, ['LOCATION', 'INDUSTRY']].values
y = dataset.loc[:, 'INTEREST RATE'].values

# Encoding Categorical Data
from sklearn.preprocessing import LabelEncoder

labelEncoder = LabelEncoder()
X[:, 0] = labelEncoder.fit_transform(X[:, 0])
X[:, 1] = labelEncoder.fit_transform(X[:, 1])

# OneHotEncoder -> ColumnTransformer
# To avoid miscorelation between 0,1,2 we use dummy encoding
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder

ct = ColumnTransformer([('encoder', OneHotEncoder(), [0, 1])], remainder='passthrough')

X = ct.fit_transform(X)

# Using Decision Tree Regressor
from sklearn.tree import DecisionTreeRegressor

regressor = DecisionTreeRegressor(random_state=0)
regressor.fit(X, y)

train_df = pd.read_csv("abc.csv")
train_df['label'] = 'train'
train_df.drop('NAME OF THE COMPANY', axis=1, inplace=True)
train_df.drop('INTEREST RATE', axis=1, inplace=True)

# read the testing data from the user as let's say score_df
score_df = pd.read_csv("testing copy.csv")
score_df['label'] = 'score'

# Concat
concat_df = pd.concat([train_df, score_df])

# Create your dummies
features_df = pd.get_dummies(concat_df, columns=['LOCATION', 'INDUSTRY'], dummy_na=True)
features_df = features_df.drop('LOCATION_nan', axis=1)
features_df = features_df.drop('INDUSTRY_nan', axis=1)

# Split your data
train_df = features_df[features_df['label'] == 'train']
score_df = features_df[features_df['label'] == 'score']

# Drop your labels
train_df = train_df.drop('label', axis=1)
score_df = score_df.drop('label', axis=1)

y_pred = (regressor.predict(score_df)).astype(int)

pickle.dump(regressor, open('model.pkl', 'wb'))
