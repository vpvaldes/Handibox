#!/usr/bin/python

import cv2.cv as cv
import numpy
import os
import time
import pickle, threading
from CameraSettings import CameraSettings
from FaceTracking import FaceTracking

class Camera:
	def __init__(self):
		#Get camera id
		camerasettings = CameraSettings()
		self.id_device = int(camerasettings.read_id())
		#Width and heigth of Handibox capture window
		self.width = 320
		self.height = 240
		#Capture from selected camera
		self.capture = cv.CreateCameraCapture(self.id_device)

		#Set width and height of current capture 
		if self.width is None:
			self.width = int(cv.GetCaptureProperty(capture, cv.CV_CAP_PROP_FRAME_WIDTH))
		else:
			cv.SetCaptureProperty(self.capture,cv.CV_CAP_PROP_FRAME_WIDTH,self.width)    

		if self.height is None:
			self.height = int(cv.GetCaptureProperty(self.capture, cv.CV_CAP_PROP_FRAME_HEIGHT))
		else:
			cv.SetCaptureProperty(self.capture,cv.CV_CAP_PROP_FRAME_HEIGHT,self.height) 

		result = cv.CreateImage((self.width,self.height),cv.IPL_DEPTH_8U,3)

		#Instantiate FaceTraking Class, return framed face and move mouse pointer 
		faceTraking = FaceTracking()

		#show capture loop, show image with framed face
		while True:
			image = cv.QueryFrame(self.capture)
			show = faceTraking.detectFace(image)
			faceTraking.updateMousePos()
			cv.ShowImage("HandiMouse", image)
			k = cv.WaitKey(10);
			if k == 'f':
				break

if __name__=='__main__':
	start = Camera()   

