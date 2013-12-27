#!/usr/bin/python
from gi.repository import Gio, Gtk
import sys
from CameraSettings import CameraSettings

class HandiboxSettings(Gtk.Window):
	#Dconf Key
	BASE_KEY = "org.gnome.desktop.a11y.mouse"
	def __init__(self):
		Gtk.Window.__init__(self, title="Configuraciones")
		self.configuration_key = Gio.Settings.new(self.BASE_KEY)
		self.set_default_icon_from_file ("handibox.png")
		self.set_default_size(200, 200)
		self.set_border_width(5)

		self.dwell_time = self.configuration_key.get_double("dwell-time")
		#--dwell-time=[0.2-3.0] Time to keep the pointer motionless  
		#before  a  dwell  click  is performed.  Range: 0.2 - 3.0 seconds.
		dwell_time_adjustement = Gtk.Adjustment(self.dwell_time, 0.2, 3.0, 0.1, 10, 0)
		self.threshold = self.configuration_key.get_int("dwell-threshold")
		# -t, --threshold=INT Ignore small pointer movements. Range 0 - 30 pixels.
		threshold_adjustement = Gtk.Adjustment(self.threshold, 0, 30, 1, 10, 0)
        

		#Dwell time scale
		self.dwell_time_scale = Gtk.Scale(orientation=Gtk.Orientation.HORIZONTAL, adjustment=dwell_time_adjustement)
		self.dwell_time_scale.set_digits(1)
		self.dwell_time_scale.set_hexpand(True)
		self.dwell_time_scale.set_valign(Gtk.Align.START)

		#Threshold scale
		self.threshold_scale = Gtk.Scale(orientation=Gtk.Orientation.HORIZONTAL, adjustment=threshold_adjustement)
		self.threshold_scale.set_digits(0)
		self.threshold_scale.set_hexpand(True)
		self.threshold_scale.set_valign(Gtk.Align.START)

        #"value-changed" emitted by the dwell time scale with the callback
        # function dwell_time_scale_moved 
		self.dwell_time_scale.connect("value-changed", self.dwell_time_scale_moved)

        #"value-changed" emitted by the threshold scale with the callback
        # function threshold_scale_moved 
		self.threshold_scale.connect("value-changed", self.threshold_scale_moved)

		#Button reset
		self.reset_button = Gtk.Button()
		self.reset_button.set_label("Reiniciar valores")
		self.reset_button.connect("clicked", self.reset_configurations)

		#Camera selection
		camerasettings.get_camera_data()
		self.cameracombo = camerasettings.camera_list
		cameralist = Gtk.ListStore(str, str)
		#Append the data

		for i in range(len(self.cameracombo)):
			cameralist.append(self.cameracombo[i])
		
		selectcamera = Gtk.ComboBox(model=cameralist)
		# Cellrenderers to render the data
		renderer_pixbuf = Gtk.CellRendererPixbuf()
		renderer_text = Gtk.CellRendererText()
		selectcamera.pack_start(renderer_pixbuf, False)
		selectcamera.pack_start(renderer_text, False)
		selectcamera.add_attribute(renderer_text, "text", 0)
		selectcamera.add_attribute(renderer_pixbuf, "stock_id", 1)
		selectcamera.set_active(0)
		selectcamera.connect("changed", self.select_camera)

		dwelllabel = Gtk.Label()
		dwelllabel.set_text("Retardo click")
		thresholdlabel = Gtk.Label()
		thresholdlabel.set_text("Sensibilidad")
		webcamlabel = Gtk.Label()
		webcamlabel.set_text("Webcam")



		# A grid to attach the widgets
		grid = Gtk.Grid()
		grid.set_column_spacing(20)
		grid.set_row_spacing (8)
		grid.attach(dwelllabel, 0, 0, 1, 1)
		grid.attach(self.dwell_time_scale, 1, 0, 1, 1)
		grid.attach(thresholdlabel, 0, 1, 1, 1)
		grid.attach(self.threshold_scale, 1, 1, 1, 1)
		grid.attach(webcamlabel, 0, 2, 1, 1)
		grid.attach(selectcamera, 1, 2, 1, 1)
		grid.attach(self.reset_button, 1, 3, 1, 1)
		self.add(grid)

    # Any signal from the dwell time scale
	def dwell_time_scale_moved(self, event):
		dwell_time_value = self.dwell_time_scale.get_value()
		self.configuration_key.set_double("dwell-time", dwell_time_value) 

	# Any signal from the threshold scale
	def threshold_scale_moved(self, event):
		threshold_value = self.threshold_scale.get_value()
		#print threshold_value
		self.configuration_key.set_int("dwell-threshold", threshold_value)

	# Callback function connected to reset button
	def reset_configurations(self, button):
		self.configuration_key.reset("dwell-time")
		self.configuration_key.reset("dwell-threshold")
		self.dwell_time = self.configuration_key.get_double("dwell-time")
		self.threshold = self.configuration_key.get_int("dwell-threshold")
		dwell_time_value = self.dwell_time_scale.set_value(self.dwell_time)
		threshold_value = self.threshold_scale.set_value(self.threshold)
		
	def select_camera(self, combo):

		if combo.get_active() != 0:
			camera_id = str(combo.get_active()) 
			camera_id = int(combo.get_active()) - 1
			print camera_id
			camerasettings.id_camera(camera_id)
		if combo.get_active() == 0:
			camera_id = str(-1)
			camerasettings.id_camera(camera_id)
			
			
		return True

camerasettings = CameraSettings()
