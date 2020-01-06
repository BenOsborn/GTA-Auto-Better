import numpy as np

def relu(x):
    return float(max(x,0))

def relud(x):
    if x <= 0:
        return float(0)
    else:
        return float(1)

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
        first_layer.append(relu(resultant))

    second_layer = []
    for i in range(16):
        resultant = float( np.dot(first_layer, weights2[i]) + bias2[0] )
        second_layer.append(relu(resultant))

    resultant = float( np.dot(second_layer, weights3) + bias3[0] )
    output = relu(resultant)

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
    first_layer_norelu = []
    for i in range(8):
        resultant = float( np.dot(arranged_pixels[i], weights1) + bias1[0] )
        first_layer.append(relu(resultant))
        first_layer_norelu.append(resultant)

    second_layer = []
    second_layer_norelu = []
    for i in range(16):
        resultant = float( np.dot(first_layer, weights2[i]) + bias2[0] )
        second_layer.append(relu(resultant))
        second_layer_norelu.append(resultant)

    resultant = float( np.dot(second_layer, weights3) + bias3[0] )
    output = relu(resultant)
    output_norelu = resultant

    return [arranged_pixels, first_layer, first_layer_norelu, second_layer, second_layer_norelu, output, output_norelu]

def training(image_pixels, weights1, bias1, weights2, bias2, weights3, bias3, learning_rate, correct):

    out = classification_for_training(image_pixels, weights1, bias1, weights2, bias2, weights3, bias3)

    weights3old = weights3
    bias3old = bias3
    weights2old = weights2
    bias2old = bias2
    weights1old = weights1
    bias1old = bias1

    for a in range(16):
        weights3[a] = weights3old[a] - -learning_rate*2*(correct - out[5])*relud(out[6])*out[3][a]
    bias3[0] = bias3old[0] - -learning_rate*2*(correct - out[5])*relud(out[6])

    for a in range(16):
            for b in range(8):
                weights2[a][b] = weights2old[a][b] - -learning_rate*2*(correct - out[5])*relud(out[6])*weights3old[a]*relud(out[4][a])*out[1][b]
            bias2[0] = bias2old[0] - -learning_rate*2*(correct - out[5])*relud(out[6])*weights3old[a]*relud(out[4][a])

    for a in range(16):
            for b in range(8):
                for c in range(625):
                    weights1[c] = weights1old[c] - -learning_rate*2*(correct - out[5])*relud(out[6])*weights3old[a]*relud(out[4][a])*weights2old[a][b]*relud(out[2][b])*out[0][b][c]
                bias1[0] = bias1old[0] - -learning_rate*2*(correct - out[5])*relud(out[6])*weights3old[a]*relud(out[4][a])*weights2old[a][b]*relud(out[2][b])
