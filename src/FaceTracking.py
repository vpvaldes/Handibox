#!/usr/bin/python

import cv2.cv as cv
import numpy
import os
import time
import pickle, threading
from Process_manager import Process_manager

class FaceTracking:	
	def __init__(self):
		self.faceCascade = cv.Load("/usr/share/opencv/haarcascades/haarcascade_frontalface_default.xml")
		self.xx = 0 #Cursor coordinate
		self.yy = 0 #Cursor coordinate
		self.pt1 = 0 #Coordinates for draw face frame
		self.pt2 = 0 #Coordinates for draw face frame
		self.posPre = 0  #Relative position of cursor on screen
		self.Data = {"cursor" : (640, 400),} #Current coordinares of cursor on screen
		self.lastData = self.Data #Update cursor coordinates
		self.olddata = {"pointer" : (640, 400),} # Old coordinates
		self.lastold = self.olddata #Update cursor coordinates
		
	def detectFace(self, image):
		#Haarcascade param
		min_size = (20,20)
		image_scale = 2
		haar_scale = 1.2
		min_neighbors = 2
		haar_flags = 0
		cv.Flip (image, image, 1)
	
		# Allocate the temporary images
		gray = cv.CreateImage((image.width, image.height), 8, 1)
		smallImage = cv.CreateImage((cv.Round(image.width / image_scale),cv.Round (image.height / image_scale)), 8 ,1)

		# Convert color input image to grayscale
		cv.CvtColor(image, gray, cv.CV_BGR2GRAY)

		# Scale input image for faster processing
		cv.Resize(gray, smallImage, cv.CV_INTER_LINEAR)

		# Equalize the histogram
		cv.EqualizeHist(smallImage, smallImage)

		# Detect the faces
		face = cv.HaarDetectObjects(smallImage, self.faceCascade, cv.CreateMemStorage(0),
		haar_scale, min_neighbors, haar_flags, min_size)

		# If face are found
		if face:
			((x, y, w, h), n) = face[0]
			# the input to cv.HaarDetectObjects was resized, so scale the
			# bounding box of each face and convert it to two CvPoints
			self.pt1 = (int(x * image_scale), int(y * image_scale))
			self.pt2 = (int((x + w) * image_scale), int((y + h) * image_scale))
			cv.Rectangle(image, self.pt1, self.pt2, cv.RGB(255, 0, 0), 3, 8, 0)
			self.xx = (self.pt1[0] + self.pt2[0])/2
			self.yy = (self.pt1[1] + self.pt2[1])/2
			cv.Circle(image, (self.xx, self.yy), 3, (0, 255, 0, 0), -1, 15, 0)
			self.Data["cursor"] = (self.xx, self.yy)
		return (image)
					
	def updateMousePos(self):
		
		pos = self.Data["cursor"]
		posPre = self.posPre
		npos = numpy.subtract(pos, posPre)
		self.posPre = pos
		self.t = threading.Thread(target=self.moveMouse, args=(npos))
		self.t.start()
        
	def moveMouse(self, x, y):
		
		newx, newy = self.Data["cursor"]
		oldx, oldy = self.olddata["pointer"]
		
		
		mul = 10
		x *= mul
		y *= mul
		posy = lambda n:(y/x) * n  
		stepp = 40
		if (abs(oldx - newx) > 1.5):
		
			if x > 0:
				for i in range(0, x, stepp): os.system("xdotool mousemove_relative -- %d %d" %(i, posy(i)))    
			if x < 0:
				for i in range(x, 0, stepp): os.system("xdotool mousemove_relative -- %d %d" %(i, posy(i)))
			time.sleep(0.15)  	
		self.olddata["pointer"] = (newx, newy)
