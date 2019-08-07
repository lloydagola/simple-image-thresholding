import cv2

picture = cv2.cv2.imread("gradient.png")

#compares each pixel of the input image to 127, 
#if it's less than 127, it's assigned 0
#if it's more than 127, it's assigned 255
_, binary_threshold = cv2.cv2.threshold(picture, 127, 255, cv2.cv2.THRESH_BINARY)
_, binary_threshold_inverse = cv2.cv2.threshold(picture, 127, 255, cv2.cv2.THRESH_BINARY_INV)
_, binary_threshold_trunc = cv2.cv2.threshold(picture, 127, 255, cv2.cv2.THRESH_TRUNC)
_, binary_threshold_to_zero = cv2.cv2.threshold(picture, 127, 255, cv2.cv2.THRESH_TOZERO)
_, binary_threshold_to_zero_inverse = cv2.cv2.threshold(picture, 127, 255, cv2.cv2.THRESH_TOZERO_INV)


cv2.cv2.imshow("Picture", picture)
cv2.cv2.imshow("binary_threshold", binary_threshold)
cv2.cv2.imshow("binary_threshold_inverse", binary_threshold_inverse)
cv2.cv2.imshow("binary_threshold_trunc", binary_threshold_trunc)
cv2.cv2.imshow("binary_threshold_to_zero", binary_threshold_to_zero)
cv2.cv2.imshow("binary_threshold_to_zero_inverse", binary_threshold_to_zero_inverse)


if cv2.cv2.waitKey(0) & 0xFF == 27:
    cv2.cv2.destroyAllWindows()