#!/usr/bin/python
from gi.repository import Gio
import os

class MouseTweak():
	CONFIGURATION_KEY = "org.gnome.desktop.a11y.mouse"
	#Enable or disable MouseTweak
	def __init__(self):
		self.configuration_key = Gio.Settings.new(self.CONFIGURATION_KEY)
	def enable_MouseTweak(self):
		os.system("python Camera.py &")
		self.configuration_key.set_boolean("dwell-click-enabled", True)
		self.configuration_key.set_boolean("click-type-window-visible", True)
		
	def disable_MouseTweak(self):
		self.configuration_key.reset("dwell-click-enabled")
		self.configuration_key.reset("click-type-window-visible")
		
