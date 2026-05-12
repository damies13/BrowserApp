import shutil

class ModuleEdge():

	def locate_browser(self):
		return self._locate_browser_linux()

	def _locate_browser_windows(self):
		return shutil.which("Edge")

	def _locate_browser_macos(self):
		return shutil.which("Edge")

	def _locate_browser_linux(self):
		chromepath = shutil.which("Edge")
		if chromepath is None:
			# try to find the flatpak version
			chromepath = shutil.which("com.microsoft.Edge")
		return chromepath

# 
