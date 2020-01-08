import numpy as np
import math

def sigmoid(x):
    return float( 1 / (1 + math.exp(-x)) )
def sigmoidd(x):
    return float( (1 / (1 + math.exp(-x)))*(1 - (1 / (1 + math.exp(-x)))) )

weights1 = np.random.uniform(size=3)
bias1 = np.random.uniform(size=1)
weights2 = np.random.uniform(size=1)
bias2 = np.random.uniform(size=1)

def classify_training(inputs, weights1, bias1, weights2, bias2):

    hidden1_net = np.dot(inputs, weights1) + bias1[0]
    hidden1 = sigmoid( hidden1_net )

    output_net = hidden1*weights2[0] + bias2[0]
    output = sigmoid( output_net )

    return [hidden1_net, hidden1, output_net, output]

def classify(inputs, weights1, bias1, weights2, bias2):

    hidden1 = sigmoid( np.dot(inputs, weights1) + bias1[0] )

    output = sigmoid( hidden1*weights2[0] + bias2[0] )

    return output

def train(inputs, actual, weights1, bias1, weights2, bias2):

    out = classify_training(inputs, weights1, bias1, weights2, bias2)

    weights1old = weights1
    bias1old = bias1
    weights2old = weights2
    bias2old = bias2

    weights2[0] = weights2old[0] - -0.5*(actual-out[3])*sigmoidd(out[2])*out[1]
    bias2[0] = bias2old[0] - -0.5*(actual-out[3])*sigmoidd(out[2])

    for a in range(3):
        weights1[a] = weights1old[a] - -0.5*(actual-out[3])*sigmoidd(out[2])*weights2old[0]*sigmoidd(out[0])*inputs[a]
    bias1[0] = bias1old[0] - -0.5*(actual-out[3])*sigmoidd(out[2])*weights2old[0]*sigmoidd(out[0])

for _ in range(10000):
    train([0, 1, 1], 1, weights1, bias1, weights2, bias2)
    train([1, 0, 0], 0, weights1, bias1, weights2, bias2)
    train([1, 1, 0], 1, weights1, bias1, weights2, bias2)
    train([0, 1, 0], 0, weights1, bias1, weights2, bias2)
    train([0, 0, 1], 0, weights1, bias1, weights2, bias2)
    train([1, 1, 1], 1, weights1, bias1, weights2, bias2)

print(classify([1, 1, 1], weights1, bias1, weights2, bias2))
