
import platform
import shutil

import Browser_Modules.flatpak as flatpak

class ModuleBrave():

	def locate_browser(self):

		locators = {
			"Windows": self._locate_browser_windows,
			"Darwin": self._locate_browser_macos,
			"Linux": self._locate_browser_linux,
		}

		return locators[platform.system()]()

	def _locate_browser_windows(self):
		return shutil.which("Brave")

	def _locate_browser_macos(self):
		return shutil.which("Brave")

	def _locate_browser_linux(self):
		# This browser doesn't currently exist for Linux
		return None
# 
