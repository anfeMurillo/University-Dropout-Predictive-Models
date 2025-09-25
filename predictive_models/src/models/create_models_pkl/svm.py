import pandas as pd
from sklearn.svm import  SVC
from sklearn.model_selection import train_test_split
import pathlib as pl
from imblearn.over_sampling import SMOTE
import joblib as jl

path = pl.Path('./../../../data/processed/data_set.csv')

df = pd.read_csv(path)

df = df.fillna(0)

df_majority = df[df['deserter'] == 0]
df_minority = df[df['deserter'] == 1]

X = df.drop(['deserter','student_id'],axis=1)
y = df['deserter']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

smote = SMOTE(random_state=42)
X_train_smote, y_train_smote = smote.fit_resample(X_train, y_train)

model_smote = SVC(kernel='rbf', random_state=42)
model_smote.fit(X_train_smote, y_train_smote)

y_pred_smote = model_smote.predict(X_test)

path_save = pl.Path('../../../models/svm.pkl')
jl.dump(model_smote,path_save)