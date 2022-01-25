from typing import final
import cv2
from matplotlib import pyplot as plt
import numpy

def convert_wordle(filename):
    im = cv2.imread(filename)
    B = im[:,:,2]
    Y = 255-B

    thresh = cv2.adaptiveThreshold(Y,255,cv2.ADAPTIVE_THRESH_MEAN_C,\
                cv2.THRESH_BINARY_INV,35,5)

    contours, hierarchy = cv2.findContours(thresh,  
        cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE) 

    x=[]
    for i in range(0, len(contours)):
        if cv2.contourArea(contours[i]) > 13000:
            x.append(contours[i])
    cv2.drawContours(im, x, -1, (255,0,0), 2) 

    top_left = (x[-1][0][0][0], x[-1][0][0][1])
    bot_right = (x[-1][0][0][0] + 670, x[-1][0][0][1] + 800)

    im_crop = im[top_left[1]:bot_right[1], top_left[0]:bot_right[0]]

    height, width = im_crop.shape[1], im_crop.shape[0]
    square_dist = (height + 170) // 6

    final_arr = []
    line = ""
    for i in range (6):
        y = i * square_dist + 30
        for j in range (5):
            x = j * square_dist + 15
            hex = im_crop[y,x]
            if (abs(hex[0] - 50) < 10 and abs(hex[1] - 50) < 10 and abs(hex[2] - 50) < 10):
                line = line + "\U00002b1b"
                im_crop = cv2.circle(im_crop, (x ,y), 10, (0,255,0), 20)
            elif (abs(hex[0] - 80) < 10 and abs(hex[1] - 135) < 10 and abs(hex[2] - 92) < 10):
                line = line + "\U0001f7e9"
                im_crop = cv2.circle(im_crop, (x ,y), 10, (255,0,0), 20)
            elif (abs(hex[0] - 70) < 10 and abs(hex[1] - 155) < 10 and abs(hex[2] - 172) < 10):
                line = line + "\U0001f7e8"
                im_crop = cv2.circle(im_crop, (x ,y), 10, (0,0,255), 20)
        final_arr.append(line)
        line = ""

    return final_arr[0], final_arr[1], final_arr[2], final_arr[3],final_arr[4], final_arr[5]

    # return_string = ""
    # for i in range (6):
    #     return_string = return_string + final_arr[i] + "\n"
    # return return_string

