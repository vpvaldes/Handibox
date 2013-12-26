#!/usr/bin/python
from gi.repository import Gio
import os

class MouseTweak():
	CONFIGURATION_KEY = "org.gnome.desktop.a11y.mouse"
	def __init__(self):
		self.configuration_key = Gio.Settings.new(self.CONFIGURATION_KEY)
	def enable_MouseTweak(self):
		os.system("python Camera.py &")
		self.configuration_key.set_boolean("dwell-click-enabled", True)
		
	def disable_MouseTweak(self):
		self.configuration_key.reset("dwell-click-enabled")
		
