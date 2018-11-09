import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import argparse
import numpy as np
import cv2
# Manually splitting the image because finding each individual petri 
#dish automatically is not possible or we could not. 

img = mpimg.imread('img/results_L3.jpg')
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
output = img1.copy()
gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
#Detecting the circle 
circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1.2, 100)
#check if it found  a circle 
for i in circles[0,:]:
    # draw the outer circle
    cv2.circle(gray,(i[0],i[1]),i[2],(0,255,0),2)
plt.imshow(gray)
circles = circles[0, 0] 
numimg1 = np.asarray(img1)
lx = numimg1.shape[0]
ly = numimg1.shape[1]
#mask = np.ones((lx, ly))
X, Y = np.ogrid[0:lx, 0:ly]
mask = (X - circles[1]) ** 2 + (Y - circles[0] ) ** 2 > (circles[2]-5)**2
# Masks
gray[mask] = 0
gray1 = (gray > 2.22*gray.mean()).astype(np.float)
#plt.plot(np.histogram(gray1, bins=60))
#plt.imshow(img1)
#plt.hist(gray1, bins=50)import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import argparse
import numpy as np
import cv2
#ap = argparse.ArgumentParser()
#ap.add_argument("-i", "--image", required = True, help = "img/results_L3.jpg")
#args = vars(ap.parse_args())
#image = cv2.imread(args["image"])
#output = image.copy()
img = mpimg.imread('img/results_L3.jpg')



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
output = img1.copy()
gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1.2, 100)
for i in circles[0,:]:
    # draw the outer circle
    cv2.circle(gray,(i[0],i[1]),i[2],(0,255,0),2)
plt.imshow(gray)
