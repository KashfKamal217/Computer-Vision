import cv2
image = cv2.imread('Images/sample_image.jpg')
cv2.imshow('Loaded Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
