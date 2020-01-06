import numpy as np

def sigmoid(x):
    #return float(max(x,0))
    return float(1 / (1 + np.exp(-x)))

def sigmoidd(x):
    '''
    if x <= 0:
        return float(0)
    else:
        return float(1)
    '''
    return float(sigmoid(x)*(1 - sigmoid(x)))

def classification(image_pixels, weights1, bias1, weights2, bias2, weights3, bias3):

    arranged_pixels = []
    for h in range(2):
        for w in range(4):
            square = []
            for ph in range(25):
                for pw in range(25):
                    square.append(image_pixels[h*25 + ph][w*25 + pw])
            arranged_pixels.append(square)

    first_layer = []
    for i in range(8):
        resultant = float( np.dot(arranged_pixels[i], weights1) + bias1[0] )
        first_layer.append(sigmoid(resultant))

    second_layer = []
    for i in range(16):
        resultant = float( np.dot(first_layer, weights2[i]) + bias2[0] )
        second_layer.append(sigmoid(resultant))

    resultant = float( np.dot(second_layer, weights3) + bias3[0] )
    output = sigmoid(resultant)

    return output

def classification_for_training(image_pixels, weights1, bias1, weights2, bias2, weights3, bias3):

    arranged_pixels = []
    for h in range(2):
        for w in range(4):
            square = []
            for ph in range(25):
                for pw in range(25):
                    square.append(image_pixels[h*25 + ph][w*25 + pw])
            arranged_pixels.append(square)

    first_layer = []
    first_layer_nosigmoid = []
    for i in range(8):
        resultant = float( np.dot(arranged_pixels[i], weights1) + bias1[0] )
        first_layer.append(sigmoid(resultant))
        first_layer_nosigmoid.append(resultant)

    second_layer = []
    second_layer_nosigmoid = []
    for i in range(16):
        resultant = float( np.dot(first_layer, weights2[i]) + bias2[0] )
        second_layer.append(sigmoid(resultant))
        second_layer_nosigmoid.append(resultant)

    resultant = float( np.dot(second_layer, weights3) + bias3[0] )
    output = sigmoid(resultant)
    output_nosigmoid = resultant

    return [arranged_pixels, first_layer, first_layer_nosigmoid, second_layer, second_layer_nosigmoid, output, output_nosigmoid]

def training(image_pixels, weights1, bias1, weights2, bias2, weights3, bias3, learning_rate, correct):

    out = classification_for_training(image_pixels, weights1, bias1, weights2, bias2, weights3, bias3)

    for a in range(16):
        weights3[a] = weights3[a] - -learning_rate*2*(correct - out[5])*sigmoidd(out[6])*out[3][a]
    bias3[0] = bias3[0] - -learning_rate*2*(correct - out[5])*sigmoidd(out[6])

    out = classification_for_training(image_pixels, weights1, bias1, weights2, bias2, weights3, bias3)

    for a in range(16):
            for b in range(8):
                weights2[a][b] = weights2[a][b] - -learning_rate*2*(correct - out[5])*sigmoidd(out[6])*weights3[a]*sigmoidd(out[4][a])*out[1][b]
            bias2[0] = bias2[0] - -learning_rate*2*(correct - out[5])*sigmoidd(out[6])*weights3[a]*sigmoidd(out[4][a])

    out = classification_for_training(image_pixels, weights1, bias1, weights2, bias2, weights3, bias3)

    for a in range(16):
            for b in range(8):
                for c in range(625):
                    weights1[c] = weights1[c] - -learning_rate*2*(correct - out[5])*sigmoidd(out[6])*weights3[a]*sigmoidd(out[4][a])*weights2[a][b]*sigmoidd(out[2][b])*out[0][b][c]
                bias1[0] = bias1[0] - -learning_rate*2*(correct - out[5])*sigmoidd(out[6])*weights3[a]*sigmoidd(out[4][a])*weights2[a][b]*sigmoidd(out[2][b])
