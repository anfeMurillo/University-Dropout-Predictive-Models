import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
import pathlib as pl
import joblib as jl

path = pl.Path('./../../../data/processed/data_set.csv')

df = pd.read_csv(path)

df = df.fillna(0)

X = df.drop(['deserter','student_id'],axis=1)
y = df['deserter']

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.3,random_state=42)

model = DecisionTreeClassifier(random_state=42)

model.fit(X_train,y_train)

y_pred = model.predict(X_test)

path_save = pl.Path('../../../models/decision_tree.pkl')
jl.dump(model,path_save)