# BrowserApp
Python module for launching chromium based web browsers in app mode

# Why does this exist

- I was planning to use [Eel](https://github.com/python-eel/Eel), but now that project is effectively unmaintained.
- I also looked at [pywebview](https://github.com/r0x0r/pywebview) as an alternative, however pywebview has [dependancies](https://pywebview.flowrl.com/guide/installation.html) that don't all install with the pip command so users need to take additional action giving a bad experiance for apps based on pywebview

What I wanted is something that chould be installed with pip as a dependancy of my project and not need addional pre-requsites installed.

This project comes close in that it's only pre-requiste is a chromium based browser being installed, it's not fussy which one and will attpempt to auto detect the browser for you.

# How to use BrowserApp:

## Install

> [!WARNING]
> pip install not implimented yet, comming soon

```command
pip install BrowserApp
```

## Import and run

```python
import BrowserApp
BApp = BrowserApp.BrowserApp()
BApp.run_browser_app("https://duck.ai")
```

# Examples

There are examples in the [Examples](/Examples/) folder

