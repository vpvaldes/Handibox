#!/usr/bin/python

import cv2.cv as cv

import os
import threading
from Process_manager import Process_manager
from Calibrations import Calibrations

class FaceTracking:
	def __init__(self):
		######Set FaceTraking constructor initial values################
		################################################################
		self.faceCascade = cv.Load("haarcascade/haarcascade_frontalface_default.xml") #Haar classifier cascade
		self.xx = 0 #Pointer coordinate
		self.yy = 0 #Pointer coordinate
		self.pt1 = 0 #Coordinates for draw face frame
		self.pt2 = 0 #Coordinates for draw face frame
		self.realscreenwidth, self.realscreenheight = pman.get_screen()
		self.calibration = calibrations.get_threshold()
		self.posPre = 0  #Relative position of pointer on screen
		self.Data = {"current" : ((int(self.realscreenwidth)/2), (int(self.realscreenheight)/2)),} #Current coordinares of pointer on screen
		self.lastData = self.Data #Update pointer coordinates
		self.olddata = {"old" : (0,0),} # Old coordinates
		self.lastold = self.olddata #Update pointer coordinates
		
	def detectFace(self, image):
		#Haarcascade param
		min_size = (20,20) #Minimum possible object size. Objects smaller than that are ignored.
		image_scale = 2 #Parameter specifying how much the image size is reduced at each image scale.
		haar_scale = 1.2 # The factor by which the search window is scaled between the subsequent scans, 1.2 means increasing window by 12 %
		min_neighbors = 2 #Parameter specifying how many neighbors each candidate rectangle should have to retain it
		haar_flags = 0 #If it is set, the function uses Canny edge detector to reject some image regions that contain too few or too much edges and thus can not contain the searched object.
		cv.Flip (image, image, 1) #Flip image
	
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
			# The input to cv.HaarDetectObjects was resized, so scale the
			# Bounding box of each face and convert it to two CvPoints
			self.pt1 = (int(x * image_scale), int(y * image_scale))
			self.pt2 = (int((x + w) * image_scale), int((y + h) * image_scale))
			# Draw principal rectangle for face detection 
			cv.Rectangle(image, self.pt1, self.pt2, cv.RGB(255, 0, 0), 3, 8, 0)
			self.xx = (self.pt1[0] + self.pt2[0])/2
			self.yy = (self.pt1[1] + self.pt2[1])/2
			# Draw central point in face
			cv.Circle(image, (self.xx, self.yy), 3, (0, 255, 0, 0), -1, 15, 0)
			# Draw neutral circle
			cv.Circle(image, (320/2, 240/2), 10, (255, 0, 0, 0), 2, 15, 0)
			# Write current pointer position 
			self.Data["current"] = (self.xx, self.yy)
			
		return (image)
					
	def updateMousePos(self):
		#Get current pointer position and send it to movemouse by thread
		pos = self.Data["current"]
		posPre = self.posPre
		self.posPre = pos
		self.t = threading.Thread(target=self.moveMouse, args=(pos))
		self.t.start()


	def moveMouse(self, x, y): 
		#update and move pointer
		#Get coordinates x & y of virtual screen from thread on UpdateMousePos method 
		virtual_screen_x = 320/2 # Size of virtualscreen X axis
		virtual_screen_y = 240/2 # Size of virtualscreen y axis
		calibration = int(self.calibration)
		oldx,oldy = self.olddata["old"] 
		# 0,0 neutral zone... no movement
		if (x==oldx and y==oldy):
			return
		if (x <=0 and y<=0):
			return 
		#Get current pointer coordinates 
		px,py = pman.get_pointer()
		px = int(px)
		py = int(py)
		diff_x = abs((virtual_screen_x) - x)
		diff_y = abs((virtual_screen_y) - y)
		if (diff_x <=10  and diff_y<=10 ):
			return
		if (virtual_screen_x > x):
			px = (px)- calibration
		else: 
			px = (px)+ calibration
		if (virtual_screen_y > y):
			py = (py)- calibration
		else:
			py = (py)+ calibration
		#Trigger movement
		os.system("xdotool mousemove %d %d" %( (px) , (py) ))
		#Save coordinates
		self.olddata["old"] = (x, y)

pman = Process_manager()
calibrations = Calibrations()

