from imageCapture import imageCapture
from makeMovie import makeMovie
"""
This script will capture images at a fixed time interval using a USB webcam

"""
timeinterval = 1  # seconds
capturecount = 20  # images

dir2save = 'C:/Users/User/tmpImageDir/'
cam = imageCapture(timeinterval)
cam.setDirectory(dir2save)

cam.startCamera()

for i in range(capturecount):
    cam.captureImage(i)

cam.stopCapture()

# let's make a movie from our captured images

videoFilename = 'timelapse.mp4'

mov = makeMovie(dir2save, videoFilename)
# load images into memory (caution!)
mov.loadImages()

# write video file
mov.writeVideo()
