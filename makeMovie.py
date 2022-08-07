import os
import cv2
import glob
from pathlib import Path


class makeMovie():


    def __init__(self,dir2use,filename):
        self.dir2use = dir2use
        self.filename = filename

    def loadImages(self):
        img_array = []
        fullPath = Path(self.dir2use)
        # sorting images by the time images were made (incase they are unsorted!)
        paths = sorted(fullPath.iterdir(),key=os.path.getmtime)
        fileNames = [f.name for f in paths if f.suffix == '.jpg']

        print('The following files will be opened..')
        print(*fileNames, sep="\n")

        for filename in glob.glob(sellf.dir2use):
            img = cv2.imread(filename)
            height, width, layers = img.shape
            size = (width, height)
            img_array.append(img)

    def writeVideo(self):
        out = cv2.VideoWriter(self.filename, cv2.VideoWriter_fourcc(*'DIVX'), 15, size)
        print('Writing video file from image array \n')
        for i in range(len(img_array)):
            out.write(img_array[i])

        out.release()
