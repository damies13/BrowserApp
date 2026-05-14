

# import importlib
# import importlib.util
import os
import subprocess
import sys


class BrowserApp():

	search_order = [ "Chrome", "Chromium", "Edge", "Brave", "Vivaldi", "Opera", "Arc" ]
	browserpath = None
	options = { "window-size":"1024,600", "window-position":"600,600" }

	def __init__(self):

		module_path = os.path.dirname(sys.modules[self.__class__.__module__].__file__)
		print("module_path:",module_path)
		sys.path.append(module_path)
		# load the browser modules 
		module_path = os.path.dirname(sys.modules[self.__class__.__module__].__file__)
		print("module_path:",module_path)
		sys.path.append(module_path)
		pass

	def set_search_order(self, new_order):
		self.search_order = new_order
		return self.search_order

	def get_search_order(self):
		return self.search_order

	def locate_browser(self):
		for brwsr in self.search_order:
			module_name = f"Module{brwsr}"
			thismod = __import__(f'Browser_Modules.{module_name}', globals(), locals(), [module_name], 0)
			print("module_name:", module_name, "	thismod:", thismod)
			thisclass = getattr(thismod, module_name)
			module = thisclass()
			path = module.locate_browser()
			print("brwsr: ",brwsr, path)
			if path is not None:
				self.browserpath = path
				return path
		self.browserpath = None

	def run_browser_app(self, url, options=options):
		if self.browserpath is None:
			self.locate_browser()

		proc_list = [self.browserpath]
		for option in options.keys():
			proc_list.append(f"--{option}={options[option]}")
		proc_list.append(f"--app={url}")
		print(proc_list)
		if self.browserpath is not None:
			proc = subprocess.Popen(proc_list)
			return proc

# 
