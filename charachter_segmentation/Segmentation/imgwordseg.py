
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

#  This is a word segmentation code
MIN_CONTOUR_AREA = 100

RESIZED_IMAGE_WIDTH = 20
RESIZED_IMAGE_HEIGHT = 30

def seperate_word():
    print("hi")

    # Create a window
    root = Tk()

    # Set Title as Image Loader
    root.title("Image Loader for word Segmentation")

    # Set the resolution of window
    root.geometry('200x150')
    # Allow Window to be resizable
    root.resizable(width=True, height=True)

    # Create a button and place it into the window using grid layout
    btn = Button(root, text='open image', command= main).grid( column=4,row=4)

    root.mainloop()




def main():
    # open file dialog box to select image
    # The dialogue box has a title "open image"
    filename = filedialog.askopenfilename(title='"pen')
    print(filename)
    # get the file name only
    print(os.path.basename(filename))

    imgTrainingNumbers = cv2.imread(filename)

    if imgTrainingNumbers is None:
        print ("error: image not read from file \n\n")
        os.system("pause")
        return


    imgGray = cv2.cvtColor(imgTrainingNumbers, cv2.COLOR_BGR2GRAY)
    imgBlurred = cv2.GaussianBlur(imgGray, (5,5), 0)

                                                        
    imgThresh = cv2.adaptiveThreshold(imgBlurred,                           # input image
                                      255,                                  
                                      cv2.ADAPTIVE_THRESH_GAUSSIAN_C,       
                                      cv2.THRESH_BINARY_INV,                
                                      11,                                   
                                      2)                                    

    cv2.imshow("imgThresh", imgThresh)
    # make a copy
    imgThreshCopy = imgThresh.copy()        
    # findContours detects change in the image color and marks it as contour
    npaContours, npaHierarchy = cv2.findContours(imgThreshCopy,
                                                 cv2.RETR_EXTERNAL,
                                                 cv2.CHAIN_APPROX_SIMPLE)



    for npaContour in npaContours:
        if cv2.contourArea(npaContour) > MIN_CONTOUR_AREA:          
            [intX, intY, intW, intH] = cv2.boundingRect(npaContour)     

            # draw rectangle around each contour as we ask user for input
            cv2.rectangle(imgTrainingNumbers,
                          (intX, intY),
                          (intX+intW,intY+intH),
                          (0, 0, 255),
                          2)
            w=time.time()
            imgROI = imgThresh[intY:intY+intH, intX:intX+intW]                                  
            imgROIResized = cv2.resize(imgROI, (RESIZED_IMAGE_WIDTH, RESIZED_IMAGE_HEIGHT))
            dirname_imgWORD = 'imgWORD/%s'%(os.path.basename(filename))

            if (not (os.path.isdir(dirname_imgWORD))):
                os.mkdir(dirname_imgWORD)

            cv2.imwrite(os.path.join(dirname_imgWORD, 'imgROI.%s.%s' % (w,'png')), imgROI)
            #######################################
            ##############################################################################
            #######################################

            dirname_imgWORDResized = 'imgWORDResized/%s' % (os.path.basename(filename))
            if (not (os.path.isdir(dirname_imgWORDResized))):
                os.mkdir(dirname_imgWORDResized)
            cv2.imwrite(os.path.join(dirname_imgWORDResized, "imgROIResized.%s.%s"%(w,'png')), imgROIResized)
            #######################################
            ##############################################################################
            #######################################
            dirname_imgTraining = 'imgTraining/%s' % (os.path.basename(filename))
            if (not (os.path.isdir(dirname_imgTraining))):
                os.mkdir(dirname_imgTraining)
            cv2.imwrite(os.path.join(dirname_imgTraining,"imgTrainingNumbers.%s.%s"%(w,'png')), imgTrainingNumbers)


            intChar = cv2.waitKey(0)                     # get key press

            if intChar == 27:                   # if esc key was pressed
                sys.exit()                      

    cv2.destroyAllWindows()           

    return

if __name__ == "__main__":

    seperate_word()
# end if




