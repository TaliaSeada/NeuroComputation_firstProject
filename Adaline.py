# libraries
import numpy as np
import pandas as pd
import random

# preprocessing
from sklearn.metrics import classification_report, f1_score
from sklearn.metrics import accuracy_score
from sklearn import metrics
from sklearn.metrics import confusion_matrix

# visualization
import matplotlib.pyplot as plt
import seaborn as sns

import warnings

warnings.filterwarnings('ignore')


class Adaline:
    def __init__(self, learning_rate, train):
        self.learning_rate = learning_rate
        self.train = train

    def _weight_genarate(self):
        weight = []
        for i in range(2):
            random.seed(i)
            rand = random.uniform(0, 0.01)
            rand = round(rand, 4)
            weight.append(rand)

        random.seed(4)
        bias = random.uniform(0, 1)
        bias = round(bias, 4)
        return weight, bias

    def fit(self):
        EPS = 0.000001
        weight, bias = self._weight_genarate()

        for index, row in self.train.iterrows():
            predicted = bias + row['x'] * weight[0] + row['y'] * weight[1]

            weight[0] = round((weight[0] + self.learning_rate * (row['value'] - predicted) * row['x']), 3)
            weight[1] = round((weight[1] + self.learning_rate * (row['value'] - predicted) * row['y']), 3)
            bias = round((bias + self.learning_rate * (row['value'] - predicted)), 3)

            # error calc
            error = (row['value'] - predicted) ** 2
            if error <= EPS or error == 0:
                break
        return weight, bias

    def predict(self, test, weight, bias):
        count = 0
        pred = []
        for index, row in test.iterrows():
            prediction = bias + (row['x'] * weight[0]) + (row['y'] * weight[1])
            if prediction > 0:
                prediction = 1
            else:
                prediction = -1
            pred.append(prediction)

            if prediction == row['value']:
                count += 1

        test['predict'] = pred
        return count

    def score(self, pred, test):
        acurr = pred / len(test)
        res = round(acurr, 4)
        return res
















