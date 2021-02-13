import cv2 as cv

#read image
original_image = cv.imread('images-5.jpeg')

#convert to gray format
gray_scale_image = cv.cvtColor(original_image,cv.COLOR_BGR2GRAY)

#CascadeClassifier pass path of the file commonly in this directory
face_cascade = cv.CascadeClassifier("/Users/avinashraj/PycharmProjects/CV1/haarcascade_frontalface_alt.xml")

#detect faces
detected_faces = face_cascade.detectMultiScale(gray_scale_image)

#make a green mark/box around face
for (column, row, width, height) in detected_faces:
    cv.rectangle(
        original_image,
        (column, row),
        (column + width, row + height),
        (0, 255, 0),
        2
    )

#show image
cv.imshow('Image', original_image)

#exit only on pressing q
if cv.waitKey(0) & 0xFF == ord('q'):
    cv.destroyAllWindows()
