
import importlib
import importlib.util
import subprocess
import sys


class BrowserApp():

	search_order = [ "Chrome", "Chromium", "Edge", "Brave", "Vivaldi", "Opera", "Arc" ]
	browserpath = None
	options = { "window-size":"1024,600", "window-position":"600,600" }

	def __init__(self):
		# load the browser modules 
		pass

	def set_search_order(self, new_order):
		self.search_order = new_order
		return self.search_order

	def get_search_order(self):
		return self.search_order

	def locate_browser(self):
		for brwsr in self.search_order:
			# bmod = importlib.import_module(f'Browser_Modules.Module{brwsr}')
			# spec = importlib.import_module(f'Browser_Modules.Module{brwsr}')
			file_path = sys.modules[self.__class__.__module__].__file__
			print(file_path)
			module_name = f"Module{brwsr}"
			module_path = f"Browser_Modules/Module{brwsr}.py"
			spec = importlib.util.spec_from_file_location(module_name, module_path)
			module = importlib.util.module_from_spec(spec)
			spec.loader.exec_module(module)
			# omodule = module()
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
		proc_list.append(f"--url={url}")
		print(proc_list)
		if self.browserpath is None:
			proc = subprocess.Popen(proc_list)
			return proc

# 
