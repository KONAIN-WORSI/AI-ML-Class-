import cv2 as cv
import numpy as np

image  = cv.imread(r'pictures\Black and Orange Typography Never Give Up Stay Strong T-Shirt_20240626_115720_0000.png')
image_r = cv.resize(image, (800, 800))
image_g  = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

def draw_mask(event, x, y, flags, param):
    global drawing, mask

    if event == cv.EVENT_LBUTTONDOWN:
        drawing = True
    elif event == cv.EVENT_MOUSEMOVE:
        if drawing:
            cv.circle(mask, (x, y), 8, 255, -1)
            cv.circle(image_r, (x, y), 8, (0, 255, 0), -1)
        elif event == cv.EVENT_LBUTTONUP:
            drawing = False

drawing = False

mask = np.zeros(image_r.shape[:2], dtype = np.uint8)
cv.namedWindow('Paint to select object')
cv.setMouseCallback('Paint to select object', draw_mask)

while True:
    cv.imshow('Paint to select object', image_r)
    key = cv.waitKey(1) & 0xFF
    if key == 13:  # Enter key to finish drwaing
        break
    elif key == 27: # Esc key to exit without inpainting
        cv.destroyAllWindows()
        exit()

# Inpainting to remove the selected object
inpainted_image = cv.inpaint(image_r, mask, inpaintRadius = 3, flags = cv.INPAINT_TELEA)

cv.imshow('Removed object image', inpainted_image)
cv.waitKey(0)
cv.destroyAllWindows()






