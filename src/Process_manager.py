#!/usr/bin/python

import os, sys, signal
import subprocess

class Process_manager:

	def stophandimouse(self, state):
		# Stop OpenCV process
		if state == False:
			os.system("pkill -9 -f Camera.py &")
			os.system("pkill -9 -f FaceTracking.py &")
			
	def get_screen(self):
		# Get display geometry
		proc = subprocess.Popen(["xdotool getdisplaygeometry"], stdout=subprocess.PIPE, shell=True)
		(out, err) = proc.communicate()
		out = str(out)
		out = out.split()
		width = out[0]
		height = out[1]

		return width, height
		
	def get_pointer(self):
		# Get pointer position
		proc = subprocess.Popen(["xdotool getmouselocation"], stdout=subprocess.PIPE, shell=True)
		(out, err) = proc.communicate()
		out = str(out)
		out = out.split( )
		x = out[0]
		y = out[1]
		x = x.strip("x:")
		y = y.strip("y:")
		
		return x, y

