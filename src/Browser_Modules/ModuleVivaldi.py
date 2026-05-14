
import platform
import shutil

import Browser_Modules.flatpak as flatpak

class ModuleVivaldi():

	def locate_browser(self):

		locators = {
			"Windows": self._locate_browser_windows,
			"Darwin": self._locate_browser_macos,
			"Linux": self._locate_browser_linux,
		}

		return locators[platform.system()]()

	def _locate_browser_windows(self):
		return shutil.which("Vivaldi")

	def _locate_browser_macos(self):
		return shutil.which("Vivaldi")

	def _locate_browser_linux(self):
		# This will find packaged installs and snaps
		browserpath = shutil.which("Vivaldi")
		if browserpath is None:
			# try to find the flatpak version
			fp = flatpak.flatpak()
			browserpath = fp.get_flatpak_path("com.vivaldi.Vivaldi")
		return browserpath

# 
