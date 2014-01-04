#!/usr/bin/python
from gi.repository import Gio

class ScreenMagnifier():
	CONFIGURATION_KEY = "org.gnome.desktop.a11y.applications"
	#Enable or disable Screen Magnifier
	def __init__(self):
		self.configuration_key = Gio.Settings.new(self.CONFIGURATION_KEY)

	def enable_ScreenMagnifier(self):
		self.configuration_key.set_boolean("screen-magnifier-enabled", True)
 
	def disable_ScreenMagnifier(self):
		self.configuration_key.reset("screen-magnifier-enabled")

