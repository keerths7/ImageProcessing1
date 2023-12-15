import numpy as np 
import cv2
from tkinter.filedialog import *
import os
import sys

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


def bnwtocolor():
    print("loading models.....")
    net = cv2.dnn.readNetFromCaffe(resource_path('./model/colorization_deploy_v2.prototxt'),resource_path('./model/colorization_release_v2.caffemodel'))
    pts = np.load(resource_path('./model/pts_in_hull.npy'))


    class8 = net.getLayerId("class8_ab")
    conv8 = net.getLayerId("conv8_313_rh")
    pts = pts.transpose().reshape(2,313,1,1)

    net.getLayer(class8).blobs = [pts.astype("float32")]
    net.getLayer(conv8).blobs = [np.full([1,313],2.606,dtype='float32')]

    photo = askopenfilename()
    image = cv2.imread(photo)
    #image = cv2.imread(r'C:/Users/skeer/Desktop/bnw/images/leaves.jpg')
    scaled = image.astype("float32")/255.0
    lab = cv2.cvtColor(scaled,cv2.COLOR_BGR2LAB)


    resized = cv2.resize(lab,(224,224))
    L = cv2.split(resized)[0]
    L -= 50


    net.setInput(cv2.dnn.blobFromImage(L))
    ab = net.forward()[0, :, :, :].transpose((1,2,0))

    ab = cv2.resize(ab, (image.shape[1],image.shape[0]))

    L = cv2.split(lab)[0]
    colorized = np.concatenate((L[:,:,np.newaxis], ab), axis=2)

    colorized = cv2.cvtColor(colorized,cv2.COLOR_LAB2BGR)
    colorized = np.clip(colorized,0,1)

    colorized = (255 * colorized).astype("uint8")

    cv2.imshow("Original",image)
    cv2.imshow("Colorized",colorized)

    cv2.waitKey(0)
