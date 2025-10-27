from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pandas as pd
import numpy as np

class MLModel:
    def __init__(self):
        self.model = RandomForestClassifier()
        self.data = None

    def load_data(self, file_path):
        self.data = pd.read_csv(file_path)

    def preprocess_data(self):
        # Example preprocessing: fill missing values and encode categorical variables
        self.data.fillna(0, inplace=True)
        self.data = pd.get_dummies(self.data)

    def train(self, target_column):
        X = self.data.drop(columns=[target_column])
        y = self.data[target_column]
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        
        self.model.fit(X_train, y_train)
        predictions = self.model.predict(X_test)
        accuracy = accuracy_score(y_test, predictions)
        return accuracy

    def predict(self, input_data):
        input_df = pd.DataFrame([input_data])
        return self.model.predict(input_df)

    def save_model(self, filename):
        import joblib
        joblib.dump(self.model, filename)

    def load_model(self, filename):
        import joblib
        self.model = joblib.load(filename)