import numpy as np
import cv2
import os
import math
input_image_path = "Test_Images/test4.jpg"
card_cascade = cv2.CascadeClassifier('Cascades/set_card_cascade_v3.xml')
dir = "Temp_Images"
img = cv2.imread(input_image_path)

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cards = card_cascade.detectMultiScale(gray_img, scaleFactor=1.04, minNeighbors=4, minSize=(30, 30))

if not os.path.exists('Temp_Images'):
    os.makedirs('Temp_Images')

# def face_distance_to_conf(face_distance, face_match_threshold=0.6):
#     if face_distance > face_match_threshold:
#         range = (1.0 - face_match_threshold)
#         linear_val = (1.0 - face_distance) / (range * 2.0)
#         return linear_val
#     else:
#         range = face_match_threshold
#         linear_val = 1.0 - (face_distance / (range * 2.0))
#         return linear_val + ((1.0 - linear_val) * math.pow((linear_val - 0.5) * 2, 0.2))

for f in os.listdir(dir):
    os.remove(os.path.join(dir, f))

for (x, y, w, h) in cards:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(img, 'card', (x+w, y+h), font, 0.5, (255, 0, 0), 2, cv2.LINE_AA)
    roi_color = img[y:y + h, x:x + w]
    print("[INFO] Object found. Saving locally.")
    cv2.imwrite("Temp_Images/" + str(x) + '-' + str(y) + '_' + str(w) + '-' + str(h) + '.jpg', roi_color)

cv2.imshow('test', img)
cv2.waitKey(0)



cv2.destroyAllWindows()
