import numpy as np
import matplotlib.pyplot as plt
import cv2

def parametrize(image):
    # Reads an image. Takes file path as input and outputs a numpy array containing the image, in greyscale.
    img = cv2.imread(image, cv2.IMREAD_GRAYSCALE)

    # Threshold image to identify the shape
    _, thresh = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)

    # Find the contours in the image
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    contour = max(contours, key=lambda x: len(x))

    contour = contour[:, 0, :]
    x = contour[:, 0]
    y = contour[:, 1]

    x = x - np.mean(x)
    y = - (y - np.mean(y))

    return x, y

# x, y = parametrize("F_outline.jpg")
# plt.plot(x, y)
# plt.show()