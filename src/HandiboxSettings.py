#!/usr/bin/python
from gi.repository import Gio, Gtk
import sys
from CameraSettings import CameraSettings

class HandiboxSettings(Gtk.Window):
	#Dconf Key
	BASE_KEY = "org.gnome.desktop.a11y.mouse"
	def __init__(self):
		Gtk.Window.__init__(self, title="Configuraciones")
		self.settings = Gio.Settings.new(self.BASE_KEY)
		self.set_default_icon_from_file ("handibox.png")
		self.set_default_size(200, 200)
		self.set_border_width(5)

		self.dwell_time = self.settings.get_double("dwell-time")
		#--dwell-time=[0.2-3.0] Time to keep the pointer motionless  
		#before  a  dwell  click  is performed.  Range: 0.2 - 3.0 seconds.
		dwell_time_adjustement = Gtk.Adjustment(self.dwell_time, 0.2, 3.0, 0.1, 10, 0)
		self.threshold = self.settings.get_int("dwell-threshold")
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
		self.reset = Gtk.Button()
		self.reset.set_label("Reiniciar valores")
		self.reset.connect("clicked", self.do_clicked)

		#Camera selection
		camerasettings.get_camera_data()
		self.actions = camerasettings.camera_list
		listmodel = Gtk.ListStore(str, str)
		#Append the data
        
		for i in range(len(self.actions)):
			listmodel.append(self.actions[i])
		
		combobox = Gtk.ComboBox(model=listmodel)
		# Cellrenderers to render the data
		renderer_pixbuf = Gtk.CellRendererPixbuf()
		renderer_text = Gtk.CellRendererText()
		combobox.pack_start(renderer_pixbuf, False)
		combobox.pack_start(renderer_text, False)
		combobox.add_attribute(renderer_text, "text", 0)
		combobox.add_attribute(renderer_pixbuf, "stock_id", 1)
		combobox.set_active(0)
		combobox.connect("changed", self.on_changed)
        
		label = Gtk.Label()
		label.set_text("Retardo click")
		label2 = Gtk.Label()
		label2.set_text("Sensibilidad")
		label3 = Gtk.Label()
		label3.set_text("Webcam")



		# A grid to attach the widgets
		grid = Gtk.Grid()
		grid.set_column_spacing(20)
		grid.set_row_spacing (8)
		grid.attach(label, 0, 0, 1, 1)
		grid.attach(self.dwell_time_scale, 1, 0, 1, 1)
		grid.attach(label2, 0, 1, 1, 1)
		grid.attach(self.threshold_scale, 1, 1, 1, 1)
		grid.attach(label3, 0, 2, 1, 1)
		grid.attach(combobox, 1, 2, 1, 1)
		grid.attach(self.reset, 1, 3, 1, 1)
		self.add(grid)

    # Any signal from the dwell time scale
	def dwell_time_scale_moved(self, event):
		dwell_time_value = self.dwell_time_scale.get_value()
		self.settings.set_double("dwell-time", dwell_time_value) 

	# Any signal from the threshold scale
	def threshold_scale_moved(self, event):
		threshold_value = self.threshold_scale.get_value()
		#print threshold_value
		self.settings.set_int("dwell-threshold", threshold_value)

	# Callback function connected to reset button
	def do_clicked(self, button):
		self.settings.reset("dwell-time")
		self.settings.reset("dwell-threshold")
		self.dwell_time = self.settings.get_double("dwell-time")
		self.threshold = self.settings.get_int("dwell-threshold")
		dwell_time_value = self.dwell_time_scale.set_value(self.dwell_time)
		threshold_value = self.threshold_scale.set_value(self.threshold)
		
	def on_changed(self, combo):

		if combo.get_active() != 0:
			camera_id = str(combo.get_active())
			camerasettings.id_camera(camera_id)
		if combo.get_active() == 0:
			camera_id = str(-1)
			camerasettings.id_camera(camera_id)
			
			
		return True

camerasettings = CameraSettings()
