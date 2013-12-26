#!/usr/bin/python
import subprocess

class CameraSettings:

	def __init__(self):
		#Init structure for list cameras on combobox
		self.camera_list = [["Webcam Predeterminada", None]]
		self.camera_id = [["Webcam Predeterminada", -1]]
		# Set camera id
		camera = open("camera", "w")
		camera.write("%s" % (-1))
		camera.close()
		
	def get_camera_data(self):
		#Read camera names
		cameras = subprocess.Popen([" ls /dev/video* | grep video -c"], stdout=subprocess.PIPE, shell=True)
		(num, err) = cameras.communicate()
		self.count_cameras  = int(num)
		
		for i in range(self.count_cameras): 
			id_camera = str(i)
			device = "/dev/video" + id_camera
			proc = subprocess.Popen(["udevadm info --query=property --name=" + device + " | grep ID_MODEL="], stdout=subprocess.PIPE, shell=True)
			camera_name = proc.stdout.readline()
			camera_name = camera_name.strip("ID_MODEL")
			camera_name = camera_name.replace("="," ")
			camera_name = camera_name.replace("\n"," ")
			#List cameras  
			if camera_name:
				new_camera = [camera_name, None]
				camera_id = [camera_name, id_camera]
				self.camera_list.append(new_camera)
				self.camera_id.append(camera_id)

	def id_camera(self, id_camera):
		# Write new camera id
		camera = open("camera", "w")
		camera.write("%s" % (id_camera))
		camera.close()

	def read_id(self):
		# Read new camera id
		camera = open("camera", "r")
		lines = camera.readlines()
		id_camera = lines[0]
		camera.close()
		return id_camera
