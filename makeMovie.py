import os
import cv2
import glob
from pathlib import Path


class makeMovie():


    def __init__(self,dir2use,filename):
        self.dir2use = dir2use
        self.filename = filename
        self.size = None
        self.img_array = None

    def loadImages(self):
        img_array = []
        fullPath = Path(self.dir2use)
        # sorting images by the time images were made (incase they are unsorted!)
        paths = sorted(fullPath.iterdir(),key=os.path.getmtime)
        fileNames = [f.name for f in paths if f.suffix == '.jpg']

        print('The following files will be opened..')
        print(*fileNames, sep="\n")

        for filename in fileNames:
            img = cv2.imread(filename)
            height, width, layers = img.shape
            self.size = (width, height)
            img_array.append(img)

        self.img_array = img_array

    def writeVideo(self):
        out = cv2.VideoWriter(self.filename, cv2.VideoWriter_fourcc(*'DIVX'), 15, self.size)
        print('Writing video file from image array \n')
        for i in range(len(self.img_array)):
            out.write(self.img_array[i])

        out.release()
