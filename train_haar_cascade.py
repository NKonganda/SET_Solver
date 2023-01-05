import cv2
import os
import numpy
import kaggle


# === IMPORT NEGATIVE IMAGES FOR TRAINING (RUN ONCE) ===
def download_images():
    print("Downloading negative image dataset...")
    kaggle.api.authenticate()
    kaggle.api.dataset_download_files('muhammadkhalid/negative-images', path='image-data', unzip=True)
    print("Download Complete!")


# === RESIZE IMAGES (RUN ONCE) ===
def format_images():
    print("Formatting images...")
    os.rename("image-data/Negative Images", "image-data/negative-images")
    count = 1
    for subdir, dirs, files in os.walk("image-data/negative-images"):
        for file in files:
            try:
                img_path = os.path.join(subdir, file)
                img = cv2.imread(img_path)
                resized_img = cv2.resize(img, (150, 100))
                cv2.imwrite("image-data/negative-images/" + str(count) + ".jpg", resized_img)
                print(img_path + " formatted")
                count += 1
                os.remove(img_path)
            except Exception as e:
                print(str(e))
    count = 1
    for subdir, dirs, files in os.walk("image-data/positive-images"):
        for file in files:
            try:
                img_path = os.path.join(subdir, file)
                img = cv2.imread(img_path)
                resized_img = cv2.resize(img, (150, 100))
                cv2.imwrite("image-data/positive-images/" + str(count) + ".jpg", resized_img)
                print(img_path + " formatted")
                count += 1
            except Exception as e:
                print(str(e))


# === WRITE DESCRIPTION FILES (RUN ONCE) ===
def create_desc_files():
    for img in os.listdir("image-data/positive-images"):
        line = img + " 1 0 0 150 100\n"
        with open("info.dat", "a") as f:
            f.write(line)
    for img in os.listdir("image-data/negative-images"):
        line = img + "\n"
        with open("bg.txt", "a") as f:
            f.write(line)


# === Run Functions ===
download_images()
format_images()
create_desc_files()
