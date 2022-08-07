from imageCapture import imageCapture
"""
This script will capture images at a fixed time interval using a USB webcam

"""
timeinterval = 2  # seconds
capturecount = 10  # images

dir2save = 'C:/Users/User/tmpImageDir/'
cam = imageCapture(timeinterval)
cam.setDirectory(dir2save)

cam.startCamera()

for i in range(capturecount):
    cam.captureImage(i)

cam.stopCapture()


