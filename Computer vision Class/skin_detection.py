import cv2  # OpenCV library
import numpy as np  # For handling arrays

# -------- Step 1: Read the image --------
# Change the filename to the image you want to use
image_path = "pictures\IMG-20240506-WA0015.jpg"  # Example: "person.jpg"
image = cv2.imread(image_path)

# Check if the image loaded properly
if image is None:
    print("Error: Image not found! Please check the path.")
    exit()

# -------- Step 2: Convert to HSV color space --------
# HSV = Hue, Saturation, Value (good for color filtering)
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# -------- Step 3: Define skin color range --------
# These values work for most skin tones, but can be adjusted if needed.
lower_skin = np.array([10, 20, 100], dtype=np.uint8)   # Lower HSV boundary
upper_skin = np.array([20, 255, 255], dtype=np.uint8)  # Upper HSV boundary

# -------- Step 4: Create a mask for skin areas --------
mask = cv2.inRange(hsv_image, lower_skin, upper_skin)
# 'mask' will be white where skin is detected, black elsewhere.

# -------- Step 5: Apply mask to the original image --------
skin_detected = cv2.bitwise_and(image, image, mask=mask)

# -------- Step 6: Display the results --------
cv2.imshow("Original Image", image)           # Show the original image
cv2.imshow("Skin Mask", mask)                 # Show where skin is detected (white = skin)
cv2.imshow("Skin Detected", skin_detected)    # Show only skin areas

cv2.waitKey(0)  # Wait for a key press to close windows
cv2.destroyAllWindows()
