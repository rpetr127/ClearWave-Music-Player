from pathlib import Path

import getpass
import os
import sys


def resource_path(relative):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative)
    else:
        return os.path.join(os.path.abspath("."), relative)


app_icon = resource_path('Icons/app.png')
logo_icon = resource_path('Icons/icons8-radio-waves-48.png')
homepath = str(Path.home().absolute())
dirpath = os.path.normpath(homepath + '/Music')
play_icon = resource_path('Icons/play.PNG')
pause_icon = resource_path('Icons/pause.png')
prev_icon = resource_path('Icons/prev.png')
forward_icon = resource_path('Icons/forward.png')
stop_icon = resource_path('Icons/stop.png')
ffprobe = resource_path('lib/ffprobe.exe')
ffplay = resource_path('lib/ffplay.exe')
logo_urls = resource_path('logo_urls/logo_urls.CSV')
