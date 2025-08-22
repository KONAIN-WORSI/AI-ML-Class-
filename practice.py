import cv2 as cv

# reading images

img = cv.imread(r'pictures\IMG_20230708_175738.jpg')

resized = cv.resize(img, (600,600)) # resizing the image to 600x600 pixels

# flipped = cv.flip(resized, 1) # flipping the image horizontally

# grey = cv.cvtColor(resized, cv.COLOR_BGR2GRAY)

# cv.rectangle(resized, (300,300), (500,500) , (80,67,233) , 3)

edges = cv.Canny(resized, threshold1 = 100 , threshold2 = 200)


cv.imshow('Edges', edges)
cv.waitKey(0) # wait for a key press

