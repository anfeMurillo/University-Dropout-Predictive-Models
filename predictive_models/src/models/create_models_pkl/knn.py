import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
import pathlib as pl
import joblib as jl

path = pl.Path('./../../../data/processed/data_set.csv')

df = pd.read_csv(path)

df = df.fillna(0)

df_majority = df[df['deserter'] == 0]
df_minority = df[df['deserter'] == 1]

df_majority_reduced = df_majority.sample(n=len(df_minority), random_state=42)

df_balanced = pd.concat([df_majority_reduced,df_minority])

# Mix the rows

df_balanced = df_balanced.sample(frac=1, random_state=42).reset_index(drop=True)

X = df_balanced.drop(['deserter','student_id'],axis=1)
y = df_balanced['deserter']

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=42)

model = KNeighborsClassifier(n_neighbors=5)

model.fit(X_train,y_train)

y_pred = model.predict(X_test)

path_save = pl.Path('../../../models/knn.pkl')
jl.dump(model,path_save)