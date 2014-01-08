#!/usr/bin/python
import subprocess

class CameraSettings:

	def __init__(self):
		#Init structure for list cameras on combobox
		self.camera_list = [["Webcam Predeterminada", None]]
		self.camera_id = [["Webcam Predeterminada", -1]]

	def initcamera(self):
		# Read last camera
		last_camera = open("camera", "r")
		lines = last_camera.readlines()
		camera_id = int(lines[0])
		last_camera.close()

		if (camera_id == -1):
			return

		elif (camera_id != -1):

			# validate last camera id
			count_cameras = subprocess.Popen([" ls /dev/video* | grep video -c"], stdout=subprocess.PIPE, shell=True)
			(num, err) = count_cameras.communicate()
			count  = int(num)
			for i in range(0,count):
				if (camera_id == i):
					
					break 
			else:
				
				# Set default camera
				default_camera = open("camera", "w")
				default_camera.write("%s" % (-1))
				default_camera.close()
					
	def get_camera_data(self):
		#Read camera names
		self.camera_list[:] = []
		self.camera_id[:] = []
		self.camera_list = [["Webcam Predeterminada", None]]
		self.camera_id = [["Webcam Predeterminada", -1]]
		cameras = subprocess.Popen([" ls /dev/video* | grep video -c"], stdout=subprocess.PIPE, shell=True)
		(num, err) = cameras.communicate()
		self.count_cameras  = int(num)
		
		for i in range(self.count_cameras): 
			id_camera = str(i)
			device = "/dev/video" + id_camera
			proc = subprocess.Popen(["/sbin/udevadm info --query=property --name=" + device + " | grep ID_MODEL="], stdout=subprocess.PIPE, shell=True)
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
