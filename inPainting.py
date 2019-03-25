import numpy as np
from matplotlib import pyplot as plt
from skimage import io, morphology, exposure, color
import cv2

def remove_mask(img,mask):
    """
    Extracts the nonzero pixels in the mask and sets the
    corresponding pixels in the original image as 0
    """
    x = np.where(mask>0.9)
    for i in range(len(x[0])):
        img[x[0][i]][x[1][i]]=0
        mask[x[0][i]][x[1][i]]=1

def isEmpty(mask):
    #Returns the number of pixels yet to be filled in our image
    return (0 == len(np.nonzero(mask)[0]))

def inPainting(img, mask):
    #The function removes the part of image where mask = 1.0
    remove_mask(img,mask)
    mask = np.floor(mask)
    # io.imshow(mask)
    # plt.show()
    # Confidence array conf(p)
    conf = 1 - np.float64(mask)
    p = np.zeros(conf.shape)

    i = 0
    while not isEmpty(mask):
        #Loop keeps running till there are pixels to be filled





    return
