import cv2

picture = cv2.cv2.imread("gradient.png")

#compares each pixel of the input image to 127, 
#if it's less than 127, it's assigned 0
#if it's more than 127, it's assigned 255
_, threshold_result = cv2.cv2.threshold(picture, 127, 255, cv2.cv2.THRESH_BINARY)

cv2.cv2.imshow("Picture", picture)
cv2.cv2.imshow("Threshold Result", threshold_result)

if cv2.cv2.waitKey(0) & 0xFF == 27:
    cv2.cv2.destroyAllWindows()