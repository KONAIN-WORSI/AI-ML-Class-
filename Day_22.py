import numpy as np
import cv2 as cv

img = cv.imread(r'pictures\building2.webp')

grey = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('grey', grey)

# simple thresold
thresold , thres_img = cv.threshold(grey, 135, 255, cv.THRESH_BINARY)
thresold , thres_img_inv = cv.threshold(grey, 135, 255, cv.THRESH_BINARY_INV)
# cv.imshow('Simple Thresold Image Regular', thres_img)
# cv.imshow('Simple Thresold Image Inverse', thres_img_inv)

# adaptive thresold
adp_thres_img_gauss = cv.adaptiveThreshold(grey, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 10)
# cv.imshow('Adaptive thresold gauss', adp_thres_img_gauss)

adp_thres_img_mean = cv.adaptiveThreshold(grey, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 10)
# cv.imshow('Adaptive thresold mean', adp_thres_img_mean)

# color spaces
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
hls = cv.cvtColor(img, cv.COLOR_BGR2HLS)
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
ycrcb = cv.cvtColor(img, cv.COLOR_BGR2YCR_CB)
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)

# cv.imshow('HSV', hsv)
# cv.imshow('HLS', hls)
# cv.imshow('LAB', lab)
# cv.imshow('YCRCB', ycrcb)
# cv.imshow('RGB', rgb)



cv.waitKey(0)