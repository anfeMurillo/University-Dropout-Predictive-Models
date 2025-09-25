import joblib as j
import pathlib as p
import pandas as pd
import sys

def __main__ ():
    
    parameter = sys.argv[1]
    
    # Data path
    data_path = p.Path('../../../data/processed/data_set.csv')
    df = pd.read_csv(data_path)
    df = df.fillna(0)
    
    # Save student_id before dropping it
    student_ids = df['student_id'].copy()
    
    match (parameter):
        case 'decision_tree':
            model_path = p.Path('../../../models/decision_tree.pkl')
            result_path = p.Path('./predictions/result_decision_tree.csv')
            model = j.load(model_path)
            X = df.drop(['deserter','student_id'], axis=1)
            prediction = model.predict(X)
            new_df = pd.DataFrame({
                'student_id': student_ids,
                'prediction': prediction
            })
            new_df.to_csv(result_path, index=False)
        case 'logistic_regression':
            model_path = p.Path('../../../models/logistic_regression.pkl')
            result_path = p.Path('./predictions/result_logistic_regression.csv')
            model = j.load(model_path)
            X = df.drop(['deserter','student_id'], axis=1)
            prediction = model.predict(X)
            new_df = pd.DataFrame({
                'student_id': student_ids,
                'prediction': prediction
            })
            new_df.to_csv(result_path, index=False)
        case 'svm':
            model_path = p.Path('../../../models/svm.pkl')
            result_path = p.Path('./predictions/result_svm.csv')
            model = j.load(model_path)
            X = df.drop(['deserter','student_id'], axis=1)
            prediction = model.predict(X)
            new_df = pd.DataFrame({
                'student_id': student_ids,
                'prediction': prediction
            })
            new_df.to_csv(result_path, index=False)
        case 'knn':
            model_path = p.Path('../../../models/knn.pkl')
            result_path = p.Path('./predictions/result_knn.csv')
            model = j.load(model_path)
            X = df.drop(['deserter','student_id'], axis=1)
            prediction = model.predict(X)
            new_df = pd.DataFrame({
                'student_id': student_ids,
                'prediction': prediction
            })
            new_df.to_csv(result_path, index=False)
    
if __name__ == "__main__":
    __main__()