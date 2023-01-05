from keras.models import load_model
from PIL import Image, ImageOps
import numpy as np
import os

# Load the model
model = load_model('keras_model.h5')

# load labels
f = open("labels.txt")
labels = f.readlines()

# read temp image names
dir = "Temp_Images"
image_names = os.listdir(dir)
print(len(image_names))
print(image_names)

# create directory for labeled cards

if not os.path.exists('Labeled_Images'):
    os.makedirs('Labeled_Images')
dir2 = 'Labeled_Images'
for f in os.listdir(dir2):
    os.remove(os.path.join(dir2, f))
# Create the array of the right shape to feed into the keras model
# The 'length' or number of images you can put into the array is
# determined by the first position in the shape tuple, in this case 1.
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

size = (224, 224)

for i in range(len(image_names)):
    # Replace this with the path to your image
    image = Image.open("Temp_Images/" + image_names[i])
    # resize the image to a 224x224 with the same strategy as in TM2:
    # resizing the image to be at least 224x224 and then cropping from the center
    image = ImageOps.fit(image, size, Image.ANTIALIAS)

    # turn the image into a numpy array
    image_array = np.asarray(image)
    # Normalize the image
    normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
    # Load the image into the array
    data[0] = normalized_image_array

    # run the inference
    prediction = model.predict(data)
    # print(type(prediction))
    # print(prediction)

    result = np.where(prediction == np.amax(prediction))
    # print('Tuple of arrays returned : ', result)
    # print('List of coordinates of maximum value in Numpy array : ')
    # zip the 2 arrays to get the exact coordinates
    # listOfCoordinates = list(zip(result[0], result[1]))
    # # traverse over the list of coordinates
    # for cord in listOfCoordinates:
    #     print(cord)
    # print second coordinate (number in labels.txt)
    print(result[1])
    output = int(result[1])
    # print(type(output))
    image.save("Labeled_Images/" + labels[output][-8:-1] + "x" + image_names[i])

    # for j in range(len(labels)):
    #     if output == fixed_labels[j]:
    #         print(labels[j])
    #         # os.rename("Temp_Images/" + image_names[i], "Temp_Images/" + labels[j][-8:-1] + "x" + image_names[i])
    #         image.save("Labeled_Images/" + labels[j][-8:-1] + "x" + image_names[i])
