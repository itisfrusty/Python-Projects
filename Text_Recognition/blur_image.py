import cv2
import numpy as np
from scipy.ndimage import convolve

# read image
image = cv2.imread('test2.jpg')
window_name = 'Blur image'

# resize image
scale_percent = 70 # percent of original size
width = int(image.shape[1] * scale_percent / 100)
height = int(image.shape[0] * scale_percent / 100)
dim = (width, height)
resized = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)

ksize = (10,10)
blured = cv2.blur(resized, ksize) 

# Sharpening karnel
sharpening_filter = np.array([[-1,-1,-1],
                              [-1,9,-1],
                              [-1,-1,-1]])
sharpende_image = cv2.filter2D(blured,-1,sharpening_filter)
new_window_name = "Deblured image"
cv2.imwrite('blured.jpg', blured)
cv2.imwrite('sharpened.jpg',sharpende_image)

# Displaying the image 
cv2.imshow(window_name, blured) 
cv2.imshow(new_window_name,sharpende_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
