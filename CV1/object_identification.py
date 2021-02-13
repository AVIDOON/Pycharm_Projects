from imageai.Detection import ObjectDetection
from IPython.display import Image
import  cv2 as cv
import os

execution_path = os.getcwd()

detector = ObjectDetection()
detector.setModelTypeAsRetinaNet()
detector.setModelPath( os.path.join(execution_path , "resnet50_coco_best_v2.0.1.h5"))
detector.loadModel()
custom_objects = detector.CustomObjects(person=True, car=False)
detections = detector.detectCustomObjectsFromImage(input_image=os.path.join(execution_path , "image2.jpeg"), output_image_path=os.path.join(execution_path , "image_new.jpeg"), custom_objects=custom_objects, minimum_percentage_probability=65)


for eachObject in detections:
   print(eachObject["name"] , " : " , eachObject["percentage_probability"] )
   print("--------------------------------")


new_image = cv.imread("image_new.jpeg",1)
cv.imshow("image",new_image)
if cv.waitKey(0) & 0xFF == ord('q'):
    cv.destroyAllWindows()