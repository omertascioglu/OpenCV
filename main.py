import cv2
print("Package imported")

image = cv2.imread("Resources/jaiyk.png")  # Read the image
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # Convert to grayscale

cv2.imshow("Grayscale Image", gray_image)  # Display the grayscale image
print(gray_image.shape)
cv2.waitKey(0)
cv2.destroyAllWindows()
