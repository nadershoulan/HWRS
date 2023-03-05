import sys
from datetime import datetime
from tkinter import *
import time
# loading Python Imaging Library
from PIL import ImageTk, Image

# To get the dialog box to open when required
from tkinter import filedialog

import numpy as np
import cv2
import os

import cv2
import numpy as np

#  This is a line segmentation code
def sep_line():
    # open file dialog box to select image
    # The dialogue box has a title "open image"
    filename = filedialog.askopenfilename(title='"pen')
    print(filename)
    # get the file name only
    print(os.path.basename(filename))
    image = cv2.imread(filename)
    if image is None:
        print ("error: image not read from file \n\n")
        os.system("pause")
        return


    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV)
    kernel = np.ones((5, 32), np.uint8)
    img_dilation = cv2.dilate(thresh, kernel, iterations=1)
    # print(kernel)
    ctrs, hier = cv2.findContours(img_dilation.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    sorted_ctrs = sorted(ctrs, key=lambda ctr: cv2.boundingRect(ctr)[0])

    for i, ctr in enumerate(sorted_ctrs):
        x, y, w, h = cv2.boundingRect(ctr)
        roi = image[y:y + h, x:x + w]
        q=time.time()
        #######################################
        ##############################################################################
        #######################################
        dirname_line = 'Lines/%s' % (os.path.basename(filename))
        if (not (os.path.isdir(dirname_line))):
            os.mkdir(dirname_line)
        cv2.imwrite(os.path.join(dirname_line,'line-%s%s.png' % (q, i)), roi)
        cv2.rectangle(image, (x, y), (x + w, y + h), (90, 0, 255), 2)
        cv2.waitKey(0)

    cv2.imshow('marked Line', image)
    cv2.waitKey(0)


def seperate_line():

    # Create a window
    root = Tk()

    # Set Title as Image Loader
    root.title("Image Loader for word Segmentation")

    # Set the resolution of window
    root.geometry('200x150')
    # Allow Window to be resizable
    root.resizable(width=True, height=True)

    # Create a button and place it into the window using grid layout
    btn = Button(root, text='open image', command=sep_line).grid(column=4, row=4)

    root.mainloop()

if __name__ == "__main__":

    seperate_line()