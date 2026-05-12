
import sys
# Use the absolute path to the directory containing your module
sys.path.append('../src')

import BrowserApp

BApp = BrowserApp.BrowserApp()

BApp.run_browser_app("https://duck.ai")

