# -------------------------------------------------------------------------
# AUTHOR: Tommy James
# FILENAME: perceptron.py
# SPECIFICATION: Complete the Python program (perceptron.py) that will read the file optdigits.tra to build a
# Single Layer Perceptron and a Multi-Layer Perceptron classifiers. You will compare their performances
# and test which combination of two hyperparameters (learning rate and shuffle) leads you to the best
# prediction performance for each classifier. To test the accuracy of those distinct models, you will use
# the file optdigits.tes. You should update and print the accuracy of each classifier, together with the
# hyperparameters when it is getting higher.
# FOR: CS 4210- Assignment #4
# TIME SPENT: how long it took you to complete the assignment
# -----------------------------------------------------------*/

# IMPORTANT NOTE: YOU HAVE TO WORK WITH THE PYTHON LIBRARIES numpy AND pandas to complete this code.

# importing some Python libraries
from sklearn.metrics import accuracy_score
from sklearn.linear_model import Perceptron
# pip install scikit-learn==0.18.rc2 if needed
from sklearn.neural_network import MLPClassifier
import numpy as np
import pandas as pd

n = [0.0001, 0.0005, 0.001, 0.005, 0.01, 0.05, 0.1, 0.5, 1.0]
r = [True, False]

# reading the data by using Pandas library
df = pd.read_csv('optdigits.tra', sep=',', header=None)

# getting the first 64 fields to form the feature data for training
X_training = np.array(df.values)[:, :64]
# getting the last field to form the class label for training
y_training = np.array(df.values)[:, -1]

# reading the data by using Pandas library
df = pd.read_csv('optdigits.tes', sep=',', header=None)

# getting the first 64 fields to form the feature data for test
X_test = np.array(df.values)[:, :64]
# getting the last field to form the class label for test
y_test = np.array(df.values)[:, -1]

max_acc = 0

for i in range(len(n)):  # iterates over n

    for j in range(len(r)):  # iterates over r

        # iterates over both algorithms
        # -->add your Python code here

        # iterates over the algorithms

        # Create a Neural Network classifier
        # if Perceptron then
        #   clf = Perceptron()    #use those hyperparameters: eta0 = learning rate, shuffle = shuffle the training data, max_iter=1000
        # else:
        #   clf = MLPClassifier() #use those hyperparameters: activation='logistic', learning_rate_init = learning rate,
        #                          hidden_layer_sizes = number of neurons in the ith hidden layer - use 1 hidden layer with 25 neurons,
        #                          shuffle = shuffle the training data, max_iter=1000
        # -->add your Pyhton code here
        if Perceptron:
            clf = Perceptron(eta0=n[i], shuffle=r[j], max_iter=1000)
        else:
            clf = MLPClassifier(activation='logistic', learning_rate_init=n[i],
                                hidden_layer_sizes=25, shuffle=r[j], max_iter=1000)

        # Fit the Neural Network to the training data
        clf.fit(X_training, y_training)

        # make the classifier prediction for each test sample and start computing its accuracy
        # hint: to iterate over two collections simultaneously with zip() Example:
        # for (x_testSample, y_testSample) in zip(X_test, y_test):
        # to make a prediction do: clf.predict([x_testSample])
        # --> add your Python code here
        acc = 0

        for (x_testSample, y_testSample) in zip(X_test, y_test):
            clf.predict([x_testSample])
            y_pred = clf.predict([x_testSample])
            acc = acc + accuracy_score([[y_testSample]], y_pred)
            # print(f'{y_pred}\t{y_testSample}\t{acc}')

        # check if the calculated accuracy is higher than the previously one calculated for each classifier. If so, update the highest accuracy
        # and print it together with the network hyperparameters
        # Example: "Highest Perceptron accuracy so far: 0.88, Parameters: learning rate=0.01, shuffle=True"
        # Example: "Highest MLP accuracy so far: 0.90, Parameters: learning rate=0.02, shuffle=False"
        # --> add your Python code here
        accuracy = round((acc / len(X_test)), 2)

        if accuracy > max_acc:
            max_acc = accuracy

        print(
            f'Highest Perceptron accuracy so far: {max_acc}, Parameters: learning rate = {n[i]}, Shuffle = {r[j]}')
