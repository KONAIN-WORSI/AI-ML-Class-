import cv2 as cv

img = cv.imread(r'pictures\building2.webp')

grey = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

gauss_blur = cv.GaussianBlur(grey, (5,5), 0)

# canny 
edges = cv.Canny(gauss_blur, threshold1 = 50, threshold2 = 200)
conture_canny, _ = cv.findContours(edges, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
count1 = len(conture_canny)
print(count1)


# thresold 
thres_val , thres_img = cv.threshold(gauss_blur , 160, 255, cv.THRESH_BINARY)
conture_thres, _ = cv.findContours(thres_img, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
count2 = len(conture_thres)
print(count2)

# draw the contures
img_canny  = grey.copy()
img_thres = grey.copy()

cv.drawContours(img_canny, conture_canny, -1, (0, 255, 0), 1)
cv.drawContours(img_thres, conture_thres, -1, (0, 0, 255), 1)

cv.imshow('Conture_canny', img_canny)
cv.imshow('Conture_thres', img_thres)

cv.waitKey(0)
cv.destroyAllWindows()