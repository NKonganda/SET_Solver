import numpy as np
from keras.datasets import mnist  # MNIST dataset is included in Keras
import matplotlib.pyplot as plt  # MATLAB like plotting routines
import random  # for generating random numbers

# number of training epochs
NUM_EPOCHS = 10


# generate image data
def generateImageData(x, y):
    # count number of images that are zeros and ones
    count0 = 0
    count1 = 0

    for i in range(x.shape[0]):
        if (y[i] == 0):
            count0 += 1
        elif (y[i] == 1):
            count1 += 1

    # extract zeros and ones
    zeros = np.zeros([count0, 28, 28])
    ones = np.zeros([count1, 28, 28])

    count0 = 0
    count1 = 0
    for i in range(x.shape[0]):
        if (y[i] == 0):
            zeros[count0, :, :] = x[i, :, :]
            count0 += 1
        elif (y[i] == 1):
            ones[count1, :, :] = x[i, :, :]
            count1 += 1

    # generate data array
    DATA = np.zeros([count0 + count1, 28 * 28 + 2])

    # these are the 1's appended to the x vector to account for the bias
    DATA[0:count0, 0] = np.ones([count0, ])

    # place the 28x28 image data here
    DATA[0:count0, 1:28 * 28 + 1] = np.reshape(zeros, [count0, 28 * 28])

    # label images that are zeros with the class -1
    DATA[0:count0, 28 * 28 + 1] = -np.ones([count0, ])

    DATA[count0:count0 + count1, 0] = np.ones([count1, ])
    DATA[count0:count0 + count1, 1:28 * 28 + 1] = np.reshape(ones, [count1, 28 * 28])

    # label images that are zeros with the class +1
    DATA[count0:count0 + count1, 28 * 28 + 1] = np.ones([count1, ])

    return DATA


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def trainPerceptron(DATA, w):
    # second verse, same as the first...the training procedure should be very
    # similar to the one in the first programming problem
    print(DATA)
    for epoch in range(10):
        x = DATA[:, :-1]
        y = DATA[:, -1:]
        for i in range(len(y)):
            if y[i] == -1:
                y[i] = 0
        product = np.dot(x, w)
        prediction = sigmoid(product)
        error = y - prediction
        deriv = prediction * (1 - prediction)
        adj = np.dot(x.T, error * deriv)
        w += adj * 0.001

    return w


def main():
    # load image data from MNIST/keras
    (X_train, y_train), (X_test, y_test) = mnist.load_data()

    # create training and test/validation data
    DATA_train = generateImageData(X_train, y_train)
    DATA_test = generateImageData(X_test, y_test)

    # initial guess for weights
    w = np.random.normal(size=[28 * 28 + 1, 1])

    # run the perceptron algorithm
    w = trainPerceptron(DATA_train, w)

    # compute accuracy of the classifier on test data. remember, accuracy is
    #     number of correctly classified examples / number of examples * 100
    correct = 0
    for data in DATA_test:
        x = data[:-1]
        y = data[-1]
        if 1 - sigmoid(np.dot([x], w))[0][0] < 0.5:
            result = 1
        else:
            result = -1
        if y == result:
            correct += 1
    print(100 * correct / len(DATA_test))


if __name__ == "__main__":
    main()
