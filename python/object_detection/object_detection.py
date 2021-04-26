import cv2
import matplotlib.pyplot as plt
import cvlib as cv
from cvlib.object_detection import draw_bbox

img = cv2.imread('fruit.jpeg')

bbox, label, conf = cv.detect_common_objects(img)

output_image = draw_bbox(img, bbox, label, conf)

RGB_img = cv2.cvtColor(output_image, cv2.COLOR_BGR2RGB)

plt.imshow(RGB_img)
plt.show()


