# from tensorflow import load_model, save_model
import os

# from datetime import datetime
from sklearn.tree import DecisionTreeClassifier
import pandas as pd
import numpy as np
from datetime import datetime
import joblib
from pandas import DataFrame


class Machine:
    def __init__(self, df):
        self.name = "DecisionTreeModel"
        print(f"DataFrame Columns: {df.columns}")
        target = df["Rarity"]
        features = df.drop(["Rarity"], axis=1)
        self.model = DecisionTreeClassifier()
        self.model = self.model.fit(features, target)
        self.initialized = datetime.now()

    def __call__(self, feature_basis):
        pred, *_ = self.model.predict(feature_basis)
        prob = self.model.predict_proba(feature_basis)
        return pred, prob.max(axis=1)[0]

    def save(self, filepath):
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        joblib.dump(self, filepath)

    @staticmethod
    def open(filepath):
        model = joblib.load(filepath)
        return model

    def info(self):
        return f"{self.name}, initialized on {self.initialized}"


# Second explenation paragraph:
# Using the average damange from each charicter is a reliable set of features to improve model accuracy. including the mean, standard deviation, and variance for each charciter increased total accuracy for all models tested (RandomForest, Decision Tree Classifier, and Binary Classifier). This is most likely becuase the damage statistics were claculated based on the dice role column of the data frame. Prior to adding these statitcs to the feature set for the model the pipeline was one hot encoding the diceroll setup, asigning a number when teh first one was encountered. By expandidng them from a categorical veriable into a numerical variable we provide the Decision Tree Mddel data that is more comprehensable. Compared to randomly assigned categories three numbers that procide real infomration to the model
