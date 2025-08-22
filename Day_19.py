import cv2 as cv
import numpy as np

img = cv.imread(r'pictures\building2.webp')
cv.imshow('Image', img)

grey = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Grey', grey)

# laplacian method
lap = cv.Laplacian(grey, cv.CV_64F) # second derivative -> + ve and - ve
lap = np.uint8(np.absolute(lap))
# cv.imshow('Laplacian', lap)

# sobel method
sobel_x = cv.Sobel(grey, cv.CV_64F, 1, 0)
sobel_y = cv.Sobel(grey, cv.CV_64F, 0, 1)

# cv.imshow('Sobel - x', sobel_x)
# cv.imshow('Sobel - y', sobel_y)

combine_sobel = cv.bitwise_or(sobel_x, sobel_y)
combine_sobel = np.uint8(np.absolute(combine_sobel))
# cv.imshow('Combine_sobel', combine_sobel)

# canny 
edges = cv.Canny(grey, threshold1 = 100, threshold2 = 300)
cv.imshow('Canny_Image', edges)


cv.waitKey(0)