from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score,recall_score,roc_auc_score,confusion_matrix,precision_score
import pandas as pd
from sklearn.model_selection import train_test_split


def load_training_data(path):
    return pd.read_csv(path)


def split_data(dataframe, target, test_split, random_state):
    X_train, X_test, y_train, y_test = train_test_split(dataframe.drop(target, axis=1), dataframe[target], test_size=test_split, random_state=random_state)
    return X_train, X_test, y_train, y_test


def train_model(X_train, y_train):
    model = ... # Define the model
    model.fit(X_train, y_train)
    return model

def save_model(model);
    pass

def evaluate_model(model, X_test, y_test):
    y_pred = model.predict(X_test)
    print(f'accuracy_score = {accuracy_score(y_test, y_pred)}')
    print(f'precision_score = {precision_score(y_test, y_pred)}')
    print(f'recall_score = {recall_score(y_test, y_pred)}')
    print(f'roc_auc_score = {roc_auc_score(y_test, y_pred)}')
    print(f'confusion_matrix = {confusion_matrix(y_test, y_pred)}')


def train_loop():
    df = load_training_data()
    X_train, X_test, y_train, y_test = split_data(df, 'flood', 0.2, 1)
    model = train_model(X_train, y_train)
    save_model(model)
    evaluate_model(model, X_test, y_test)

