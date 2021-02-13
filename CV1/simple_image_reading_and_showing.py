import cv2 as cv

new_image = cv.imread("image_new.png",0)
cv.imshow("image",new_image)
if cv.waitKey(0) & 0xFF == ord('q'):
    cv.destroyAllWindows()