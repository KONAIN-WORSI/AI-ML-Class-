import cv2 as cv

# reading images
img = cv.imread(r'pictures\IMG-20240506-WA0015.jpg')

resized = cv.resize(img, (700, 900))

# average blurring the image
avg_blur = cv.blur(resized, (5,5))

# Median blurring
median_blur = cv.medianBlur(resized, 5) # -> this only takes odd values

# Gussain blur
guss_blur = cv.GaussianBlur(resized, (5,5) , 0)
# cv.imshow('Guassian Blur', guss_blur)

# Bilateral blur
Bilat_blur = cv.bilateralFilter(resized, 5 , 20 , 20)
cv.imshow('Bilateral Blur', Bilat_blur)


cv.imshow('Resized Image', resized)

# cv.imshow('Average blur', avg_blur)
# cv.imshow('Median Blur', median_blur)
cv.waitKey(0)