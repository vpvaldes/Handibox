#!/usr/bin/python
from gi.repository import Gio

class ScreenKeyboard():
	CONFIGURATION_KEY = "org.gnome.desktop.a11y.applications"
	def __init__(self):
		self.configuration_key = Gio.Settings.new(self.CONFIGURATION_KEY)
	
	
	def enable_ScreenKeyboard(self):
		self.configuration_key.set_boolean("screen-keyboard-enabled", True)
		 
	def disable_ScreenKeyboard(self):
		self.configuration_key.reset("screen-keyboard-enabled")
