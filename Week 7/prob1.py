import math
import random

import matplotlib.pyplot as plt
import numpy
from matplotlib import pyplot

from keras.layers import Dense
from keras.models import Sequential
from keras.optimizers import SGD

r = Sequential()
numpy.array

def setup_nn():
    r.add(Dense(1, activation='sigmoid', input_dim=1, init='uniform'))
    sgd = SGD(lr=0.05, decay=1e-6, momentum=0.9, nesterov=False)
    r.compile(loss='mean_squared_error', optimizer='sgd', metrics=['accuracy'])

def target_function(X):
    #a = random.uniform(0, 1)
    a = math.sin(X*3)
    return a*10


def trainX(samplesize):
    X = []
    Y = []
    for j in range(0, samplesize):
        xj = random.random()
        X.append(xj)
        Y.append(target_function(xj))
    r.fit(X, Y, batch_size=3, nb_epoch=100)
    return


def testX():
    X = [random.random()]
    Y = target_function(X[0])
    X = numpy.array(X)
    Ypred = r.predict(X, batch_size=3)
    return [X, Ypred[0][0]]


setup_nn()

trainX(1000)
X = []
Y = []
for i in range(0, 20):
    XY = testX()
    X.append(XY[0][0])
    Y.append(XY[1])
pyplot.plot(X, Y, 'o')


def plotfunction():
    for i in range(0, 20):
        x = i / 20
        X.append(x)
        Y.append(target_function(x))
    pyplot.plot(X, Y, '.')


plotfunction()
plt.show()