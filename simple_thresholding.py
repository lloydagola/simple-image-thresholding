import cv2

picture = cv2.cv2.imread("gradient.png")


cv2.cv2.imshow("Picture", picture)


if cv2.cv2.waitKey(0) & 0xFF == 27:
    cv2.cv2.destroyAllWindows()