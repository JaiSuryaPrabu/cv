# importing necessary library 
import cv2
import numpy as np

image = cv2.imread("basics/greyscaling/earth.jpg") # loading the image 
rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB) # by default cv loads in BGR channel

# convert to greyscale
greyscaled_image = np.dot(rgb_image[...,:3],[0.299, 0.587, 0.114]).astype(np.uint8)

# show the image
cv2.imshow("Image",image)
cv2.imshow("Greyscaled Image",greyscaled_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# saving the greyscale image
cv2.imwrite("basics/greyscaling/greyscaled_image.jpg",greyscaled_image)