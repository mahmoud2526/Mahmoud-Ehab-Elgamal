import os
import sys
import cv2
import numpy as np
import matplotlib.pyplot as plt

v=cv2.VideoCapture("race_car.mp4")
tracker=cv2.
while cv2.waitKey(1)!=27:
    ret,frame=v.read()
    if not ret:
        break


    cv2.imshow("Frame",frame)
    bb=cv2.selectROI("Frame",frame)




c=np.array([1,2,3])

print(c)




