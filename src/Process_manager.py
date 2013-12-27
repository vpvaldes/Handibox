#!/usr/bin/python

import os, sys, signal

class Process_manager:

	def stophandimouse(self, state):
		# Stop OpenCV process
		if state == False:
			os.system("pkill -9 -f Camera.py &")
			os.system("pkill -9 -f FaceTracking.py &")
