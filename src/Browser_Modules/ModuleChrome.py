import shutil

class ModuleChrome():

	def locate_browser(self):
		return self._locate_browser_linux()

	def _locate_browser_windows(self):
		return shutil.which("chrome")

	def _locate_browser_macos(self):
		return shutil.which("google-chrome")

	def _locate_browser_linux(self):
		chromepath = shutil.which("google-chrome")
		if chromepath is None:
			# try to find the flatpak version
			chromepath = shutil.which("com.google.Chrome")
		return chromepath

# 
