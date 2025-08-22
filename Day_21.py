import cv2 as cv
import numpy as np

img = cv.imread(r'pictures\IMG-20240506-WA0015.jpg')

# resizing 
resized = cv.resize(img, (600, 600), interpolation = cv.INTER_AREA) # kam dimension ma inter-area or iner-linear badi ma inter-cubic
# cv.imshow('Resized', resized)


# flipping
flip = cv.flip(resized, -1) # 1 for horizontal flip 0 for vertical flip and for both -1
# cv.imshow('Original Image', resized)
# cv.imshow('vertical Image', flip)

# cropping
# cropped = resized[100:400,300:600]
# cv.imshow('Cropped Image', cropped)

# translation
# def translate(img, x, y):
#     trans_mat = np.float64([[1, 0 , x], [0, 1, y]])
#     dimension = (img.shape[1], img.shape[0])
#     return cv.warpAffine(img , trans_mat , dimension)

# translated = translate(img , 80, 100)
# cv.imshow('Original Image', img)
# cv.imshow('Translated Image', translated)


# rotation
def rotate(img, angle , rotpoint = None):
    (height , width) = img.shape[:2] # accessing the whole picture through slicing

    if rotpoint is None:
        rotpoint = (width // 2, height // 2)

    rot_mat = cv.getRotationMatrix2D(rotpoint , angle, 1.0)
    dimension = (width, height)
    return cv.warpAffine(img, rot_mat , dimension)

rotated = rotate(img , -45, (200,100) )
cv.imshow('Original Image', img)
cv.imshow('Rotated Image', rotated)

    




cv.waitKey(0)