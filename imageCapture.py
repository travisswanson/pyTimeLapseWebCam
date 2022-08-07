import os
import cv2
import time
from datetime import datetime

class imageCapture(object):


    def __init__(self, timeinterval, framewidth=720, frameheight=1280, camera=None, dir2save=None):

        self.timeinterval = timeinterval
        self.framewidth = framewidth
        self.frameheight = frameheight
        self.camera = camera
        self.dir2save = dir2save


    def setDirectory(self,dir2save):
        self.dir2save = dir2save
        if os.path.exists(self.dir2save):
            os.chdir(self.dir2save)
        else:
            os.makedirs(self.dir2save)
            os.chdir(self.dir2save)
            print("The new directory is created!")


    def startCamera(self):
        self.camera = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        self.camera.set(cv2.CAP_PROP_FRAME_WIDTH, self.framewidth)  # set new image width dimension (pixels)
        self.camera.set(cv2.CAP_PROP_FRAME_HEIGHT, self.frameheight)  # set new image height dimension (pixels)


    def captureImage(self,i):
        tNow = time.time()
        return_value, image = self.camera.read()
        # write the image with the file name "image number-capture time.jpg"
        cv2.imwrite(str(i) + '-' + datetime.now().strftime('%d-%m-%Y-%H-%M-%S') + '.jpg', image)
        print(time.time() - tNow)
        time.sleep(self.timeinterval)
        print('Just wrote jpg # ' + str(i) + '...')


    def stopCapture(self):
        del self.camera