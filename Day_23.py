import cv2 as cv 
import numpy as np

# img_1 = np.zeros((300,300), dtype = 'uint8')
# img_2 = np.zeros((300,300), dtype = 'uint8')

# # draw a white rectangle and a white circle 
# cv.rectangle(img_1, (50,50), (250,250), 255, -1) # -1 is for color filling inside the rectangle
# cv.circle(img_2, (150,150), 120 , 255, -1)

# cv.imshow('Rectangle', img_1)
# cv.imshow('Circle', img_2)


# # bit wise operation
# bit_and = cv.bitwise_and(img_1, img_2)
# cv.imshow('AND', bit_and)

# bit_or = cv.bitwise_or(img_1, img_2)
# cv.imshow('OR', bit_or)

# bit_xor = cv.bitwise_xor(img_1, img_2)
# cv.imshow('XOR', bit_xor)

# bit_not = cv.bitwise_not(img_2)
# cv.imshow('NOT', bit_not)

# Masking


# img_mask = np.zeros(resized.shape[:2], dtype = 'uint8')

# # create a mask
# cv.circle(img_mask, (200,200), 175, 255, -1)

# # apply the mask
# masked_img = cv.bitwise_and(resized , resized, mask = img_mask)

# # show
# cv.imshow('Original Image', resized)
# cv.imshow('Mask', img_mask)
# cv.imshow('Masked Image', masked_img)



img = cv.imread(r'pictures\IMG-20230721-WA0025.jpg')
resized = cv.resize(img, (400,400))

# spliting the color channel
B, G, R =  cv.split(resized)

# cv.imshow('Original Image', resized)
# cv.imshow('Grey for Blue', B)
# cv.imshow('Grey for Green', G)
# cv.imshow('Grey for Red', R)

# merged = cv.merge([B, G, R])
# cv.imshow('Merged image', merged)


zeros = np.zeros_like(B)
blue_visual = cv.merge([B, zeros, zeros])
green_visual = cv.merge([zeros, G, zeros])
red_visual = cv.merge([zeros, zeros, R])

cv.imshow('blue', blue_visual)
cv.imshow('Green', green_visual)
cv.imshow('Red', red_visual)



cv.waitKey(0)
cv.destroyAllWindows() 