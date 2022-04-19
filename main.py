# libraries
import Adaline
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


def build_data_partA(i):
    x = []
    y = []
    value = []
    random.seed(i)
    for i in range(1000):
        randX = random.randint(-10000, 10000)
        randY = random.randint(-10000, 10000)
        x.append(randX / 100)
        y.append(randY / 100)
        if y[i] > 1:
            value.append(1)
        else:
            value.append(-1)

    end = {'x': x, 'y': y, 'value': value}
    df = pd.DataFrame(data=end, columns=['x', 'y', 'value'])
    return df


def build_data_partB(i):
    x = []
    y = []
    value = []
    random.seed(i)
    for i in range(1000):
        randX = random.randint(-10000, 10000)
        randY = random.randint(-10000, 10000)
        x.append(randX / 100)
        y.append(randY / 100)
        if 4 <= (y[i]**2 + x[i]**2) <= 9:
            value.append(1)
        else:
            value.append(-1)

    end = {'x': x, 'y': y, 'value': value}
    df = pd.DataFrame(data=end, columns=['x', 'y', 'value'])
    return df


def plotting(test):
    print(test)
    f, ax = plt.subplots(1, 2)
    ax[0].set_title("value")
    ax[1].set_title("predict")

    for index, row in test.iterrows():
        if row['value'] == 1:
            ax[0].plot(row['x'], row['y'], markersize=2, marker="o", color="blue")
        else:
            ax[0].plot(row['x'], row['y'], markersize=2, marker="o", color="red")
        if row['predict'] == 1:
            ax[1].plot(row['x'], row['y'], markersize=2, marker="o", color="blue")
        else:
            ax[1].plot(row['x'], row['y'], markersize=2, marker="o", color="red")
    plt.show()

def main():
    part = input("Enter the relevant part (A or B): ")

    # part A
    if part == 'A':
        train = build_data_partA(1)
        test = build_data_partA(9)
        ada = Adaline.Adaline(0.0001, train)
        weight, bias = ada.fit()
        ada_pred = ada.predict(test, weight, bias)
        ada_score = ada.score(ada_pred, test)
        print(ada_score * 100)
        plotting(test)

    # part B
    elif part == 'B':
        train = build_data_partB(9)
        test = build_data_partB(1)
        ada = Adaline.Adaline(0.001, train)
        weight, bias = ada.fit()
        ada_pred = ada.predict(test, weight, bias)
        ada_score = ada.score(ada_pred, test)
        print(ada_score * 100)
        plotting(test)

    else:
        print("Not Valid")




if __name__ == '__main__':
    main()
