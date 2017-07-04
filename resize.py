import cv2
import numpy as np
import glob
import os
from datetime import datetime as dt

################## Note ############################################
#   This script is written by python2.                             #
#   If you use Python3, you have to change the following points    #
#   please change                                                  #
#   "raw_input()" to "input()"                                     #
#   "if not (img is None):" to "if not (img.all() is None):"       #
####################################################################

count = 0

if __name__ == '__main__':
    
    # ask you the size you want
    print("What size do you want?")
    print("What is the height?")
    input_height = raw_input('>>>  ')
    print("You decided  {}  pixels.(height)".format(input_height))
    print("What is the width?")
    input_width = raw_input('>>>  ')
    print("You decided  {}  pixels.(width)".format(input_width))
    
    # make a directory to save resized images
    dtime = dt.now()
    dirname = dtime.strftime('%Y%m%d-%H%M%S')
    os.mkdir(dirname)
    
    # Resize images
    for f in glob.glob(os.path.join("/Users/nakamura/Desktop/ResizeJPG/images/","*.jpg")):
        img = cv2.imread(f)
        if not (img is None):
            re_size = cv2.resize(img, (int(input_height), int(input_width)))
            count += 1
            cv2.imwrite("./{}/output-{}.jpg".format(dirname, count), re_size)
        else:
            print("Not Exist the image: {}".format(f))
