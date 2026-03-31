import cv2 as cv
import numpy as np

image = cv.imread(r'pictures\IMG_20230916_154030_531.jpg')
image_r = cv.resize(image, (800,800))
image_g = cv.cvtColor(image_r, cv.COLOR_BGR2GRAY)


# Select ROI (Region of Interest) for object removal
def draw_mask(event, x, y, flags, param):
    global drawing, mask
    if event == cv.EVENT_LBUTTONDOWN:
        drawing = True
    elif event == cv.EVENT_MOUSEMOVE:
        if drawing:
            cv.circle(mask, (x, y), 10, 255, -1)
            cv.circle(image_r, (x, y), 10, (0, 0, 255), -1)
    elif event == cv.EVENT_LBUTTONUP:
        drawing = False

drawing = False
mask = np.zeros(image_r.shape[:2], dtype=np.uint8)
cv.namedWindow("Paint to Select Object")
cv.setMouseCallback("Paint to Select Object", draw_mask)


# Show the image and allow user to draw mask
while True:
    cv.imshow('Paint to Select Object', image_r)
    key = cv.waitKey(1) & 0xFF
    if key == 13:  # Enter key to finish drawing
        break
    elif key == 27:  # Esc key to exit without inpainting
        cv.destroyAllWindows()
        exit()

# Inpainting to remove the selected object
inpainted_image = cv.inpaint(image_r, mask, inpaintRadius=2, flags=cv.INPAINT_TELEA)


cv.imshow('Removed Object Image', inpainted_image)
cv.waitKey(0)
cv.destroyAllWindows()