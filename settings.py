import tkinter as tk
import time

# Window Settings
APP_TITLE = 'Personal APP'

# Colors
COLOR_BACKGROUND = '#1a1a1a'

COLOR_BLACK = '#0000000'
COLOR_WHITE = '#ffffff'
COLOR_LIGHTGREY = '#383838'

# Window Dimensions
def GetWindowWidth(_root):
    return _root.winfo_screenwidth()
def GetWindowHeight(_root):
    return _root.winfo_screenheight()

# Time
def GetCurrentHour():
    return time.strftime('%H:%M:%S')

def GetCurrentDate():
    return time.strftime('%d/%m/%Y')

def GetDateTime():
    return f'[{GetCurrentDate()} {GetCurrentHour()}]'