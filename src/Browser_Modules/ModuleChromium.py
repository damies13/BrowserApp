import shutil

class ModuleChromium():

	def locate_browser(self):
		return self._locate_browser_linux()

	def _locate_browser_windows(self):
		return shutil.which("chromium")

	def _locate_browser_macos(self):
		return shutil.which("chromium")

	def _locate_browser_linux(self):
		chromepath = shutil.which("chromium")
		if chromepath is None:
			# try to find the flatpak version
			chromepath = shutil.which("org.chromium.Chromium")
		return chromepath

# 
