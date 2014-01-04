#!/usr/bin/python
from gi.repository import Gio

class Calibrations():
	CONFIGURATION_KEY = "org.gnome.desktop.a11y.mouse"
	#Get threshold value
	def __init__(self):
		self.configuration_key = Gio.Settings.new(self.CONFIGURATION_KEY)
	def get_threshold(self):
		threshold = self.configuration_key.get_int("dwell-threshold")
		return threshold
