import cv2
import time
import datetime
import os


"""
# This script will take images at a fixed time interval using a USB webcam


# This script will run for approximately 28 hours, and capture an image every 20 seconds (28*60*3)

# Start this script before you start flumeControl.py
"""

# image capture configuration
timeinterval = 20  # seconds
imagestocapture = 1000  # images

dir2save = 'C:/Users/User/Documents/flumeImagery/temp_control/with_ac/5_hr/20mm'

if os.path.exists(dir2save):
    os.chdir(dir2save)
else:
    os.makedirs(dir2save)
    os.chdir(dir2save)
    print("The new directory is created!")

camera = cv2.VideoCapture(0, cv2.CAP_DSHOW)
camera.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)  # set new dimensions to cam object (not cap)
camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

for i in range(imagestocapture):
    tNow = time.time()
    return_value, image = camera.read()
    cv2.imwrite(str(i) + '-' + datetime.datetime.now().strftime('%d-%m-%Y-%H-%M-%S') + '.jpg', image)
    print(time.time() - tNow)
    time.sleep(timeinterval)
    print('Just wrote jpg # ' + str(i) + '...')

del (camera)
