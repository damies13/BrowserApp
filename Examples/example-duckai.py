
import os
import sys
# sys.path.append('../src')
# Use the absolute path to the directory containing your module
modulepath = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src"))
print("modulepath:", modulepath)
sys.path.append(modulepath)

import BrowserApp

BApp = BrowserApp.BrowserApp()


my_search_order = [ "Edge", "Brave", "Chromium", "Chrome", "Vivaldi", "Opera", "Arc" ]
BApp.set_search_order(my_search_order)

BApp.run_browser_app("https://duck.ai")

