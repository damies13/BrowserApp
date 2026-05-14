

import os
import re
import subprocess
import shutil

class flatpak():

	fpcommand = None
	fpversion = None
	fpinstallations = None

	def __init__(self):
		self.get_flatpak_version()

	def get_flatpak_path(self, flatpak_id):
		try:
			fppath = self.construct_flatpak_path(flatpak_id)
			# print("fppath:", fppath)
			if os.path.isfile(fppath):
				return fppath
			else:
				return None
		except:
			return None

	def get_flatpak_info(self, flatpak_id):
		if self.fpversion is None:
			return None
		try:
			# flatpak info com.brave.Browser
			command = f"flatpak info {flatpak_id}"
			result = subprocess.check_output(command, shell=True, text=True)
			# print("result:", result)
			regex = r"\W*(?P<key>\w+): (?P<value>.*)"
			m = re.findall(regex, result)
			# print("m:", m)
			info = dict(m)
			# print("info:", info)
			return info
		except:
			return None

	def get_flatpak_version(self):
		if self.fpversion is None:
			fpcommand = shutil.which("flatpak")
			if fpcommand is None:
				return None
			else:
				self.fpcommand = fpcommand.rstrip()
				command = f"flatpak --version"
				result = subprocess.check_output(command, shell=True, text=True)
				print(result)
				self.fpversion = result.rstrip()

		return self.fpversion

	def get_flatpak_installations(self):
		# flatpak --installations
		command = f"flatpak --installations"
		result = subprocess.check_output(command, shell=True, text=True)
		# print("installations path:", result)
		self.fpinstallations = result.rstrip()
		return self.fpinstallations

	def construct_flatpak_path(self, flatpak_id):
		if self.fpversion is None:
			return None
		try:
			# /var/lib/flatpak/app/com.brave.Browser/x86_64/stable/active/export/bin/com.brave.Browser 
			fpinfo = self.get_flatpak_info(flatpak_id)
			if fpinfo is not None:
				print("fpinfo:",fpinfo)
				if "Ref" not in fpinfo:
					return None
				if self.fpinstallations is None:
					self.fpinstallations = self.get_flatpak_installations()
				# print("self.fpinstallations:", self.fpinstallations)
				if self.fpinstallations is None:
					return None
				else:
					# print("self.fpinstallations:", self.fpinstallations)
					# print("fpinfo['Ref']:", fpinfo["Ref"])
					# print("flatpak_id:", flatpak_id)
					fppath = os.path.join(self.fpinstallations, fpinfo["Ref"], "active", "export", "bin", flatpak_id)
					# print("fppath:", fppath)
					return fppath
			return None
		except Exception as e:
			# print("e:", e)
			return None

# 