import numpy as np
import cv2
from matplotlib import pyplot as plt
from skimage import io, morphology, exposure, color
from inPainting import *

def main():
    filePhoto = "img/photo.jpg"
    fileMask = "img/mask.jpg"
    #Reads the given image and converts it to grayscale
    img_grayscale = color.rgb2gray(io.imread(filePhoto))
    img_mask = color.rgb2gray(cv2.imread(fileMask))
    img = inPainting(img_grayscale,img_mask)

    return



if __name__ == '__main__':
    main()
