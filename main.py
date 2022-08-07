import cv2
import time
import datetime
import os


"""
This script will capture images at a fixed time interval using a USB webcam

"""

# image capture configuration
timeinterval = 20  # seconds
imagestocapture = 1000  # images

dir2save = 'C:/Users/SampleUser/DirectoryToSave/'

if os.path.exists(dir2save):
    os.chdir(dir2save)
else:
    os.makedirs(dir2save)
    os.chdir(dir2save)
    print("The new directory is created!")

camera = cv2.VideoCapture(0, cv2.CAP_DSHOW)
camera.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)  # set new image width dimension (pixels)
camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)  # set new image height dimension (pixels)

for i in range(imagestocapture):
    tNow = time.time()
    return_value, image = camera.read()
    # write the image with the file name "image number-capture time.jpg"
    cv2.imwrite(str(i) + '-' + datetime.datetime.now().strftime('%d-%m-%Y-%H-%M-%S') + '.jpg', image)
    print(time.time() - tNow)
    time.sleep(timeinterval)
    print('Just wrote jpg # ' + str(i) + '...')

del (camera)
