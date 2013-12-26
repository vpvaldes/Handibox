#!/usr/bin/python
from gi.repository import Gio, Gtk
import sys
import os
from Process_manager import Process_manager
from ScreenKeyboard import ScreenKeyboard 
from ScreenMagnifier import ScreenMagnifier
from MouseTweak import MouseTweak
from HandiboxSettings import HandiboxSettings

class HandiboxMain(Gtk.Window):
	#Dconf Key
	CONFIGURATION_KEY = "org.gnome.desktop.a11y.applications"
	def __init__(self):
		Gtk.Window.__init__(self, title="Handibox")
		self.set_default_icon_from_file ("handibox.png")
		self.set_default_size(200, 100)
		self.set_border_width(10)
		self.configuration_key = Gio.Settings.new(self.CONFIGURATION_KEY)

		# create an image (Handibox logo)
		handiboxlogo = Gtk.Image()
		handiboxlogo.set_from_file("handibox.png")

		#First switch: Mouseteak
		self.mousetweak = Gtk.Switch()
		self.mousetweak.set_active(False)
		self.mousetweak.connect("notify::active", self.enable_mousetweak)
		mousetweaklabel = Gtk.Label()
		mousetweaklabel.set_text("Handiface")
		

		#Second switch: Screen Magnifier
		self.magnifier = Gtk.Switch()
		self.magnifier.set_active(False)
		self.magnifier.connect("notify::active", self.screen_magnifier)
		magnifierlabel = Gtk.Label()
		magnifierlabel.set_text("Handizoom")
		
		
		#Third switch: Screen Keyboard
		self.keyboard = Gtk.Switch()
		self.keyboard.set_active(False)
		self.keyboard.connect("notify::active", self.screen_keyboard)
		keyboardlabel = Gtk.Label()
		keyboardlabel.set_text("Handikey")
		
		#Settings button
		settingsbutton = Gtk.Button("Configuraciones")
		settingsbutton.set_label("Configuraciones")
		settingsbutton.connect("clicked", self.on_button_clicked)
		
########################################################################

		#Attach elements to table
		table = Gtk.Table(4, 3, True);
		table.attach (handiboxlogo, 0, 5, 0, 1);
		
		table.attach (mousetweaklabel, 0, 2, 1, 2);
		table.attach (self.mousetweak, 3, 5, 1, 2);
		
		table.attach (magnifierlabel, 0, 2, 2, 3);
		table.attach (self.magnifier, 3, 5, 2, 3);
		
		table.attach (keyboardlabel, 0, 2, 3, 4);
		table.attach (self.keyboard, 3, 5, 3, 4);
		
		table.attach (settingsbutton, 0, 5, 4, 5);

		self.add(table)
########################################################################

	#Enable or disable MouseTweak
	def enable_mousetweak(self, button, active):
		mouseTweak = MouseTweak()
		processmanager = Process_manager()
		if button.get_active():
			self.mousetweak.set_active(True)
			mouseTweak.enable_MouseTweak()
			
		else:	
			mouseTweak.disable_MouseTweak()
			self.mousetweak.set_active(False)
			handimouse = False
			processmanager.stophandimouse(handimouse)
	
	#Enable or disable Screen Magnifier
	def screen_magnifier(self, button, active):
		screenMagnifier = ScreenMagnifier()
		if button.get_active():
			screenMagnifier.enable_ScreenMagnifier()
		else:	
			screenMagnifier.disable_ScreenMagnifier()
	
	#Enable or disable Screen Keyboard
	def screen_keyboard(self, button, active):
		screenKeyboard = ScreenKeyboard()
		if button.get_active():
			screenKeyboard.enable_ScreenKeyboard()
			
		else:	
			screenKeyboard.disable_ScreenKeyboard()
			
	#View Settings
	def on_button_clicked(self, widget):
		handiboxsettings = HandiboxSettings()
		handiboxsettings.show_all()
		
		
handiboxmain = HandiboxMain()
handiboxmain.connect("delete-event", Gtk.main_quit)
handiboxmain.show_all()
Gtk.main()
