import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import cv2

img = mpimg.imread('img/gray.jpg')
img1 = img[500:705, 75:300]
img2 = img[500:705, 300:512]
img3 = img[500:705, 512:720]
img4 = img[495:700, 722:921]
img5 = img[295:500, 80:300]
img6 = img[295:500, 295:512]
img7 = img[295:500, 512:709]
img8 = img[295:495, 712:911]
img9 = img[55:250, 575:775]
img10 = img[60:255, 580:780]
