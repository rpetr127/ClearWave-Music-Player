from pathlib import Path

import getpass
import os
import sys


def resource_path(relative):
    # if hasattr(sys, '_MEIPASS'):
    #     return os.path.join(sys._MEIPASS, relative)
    # else:
    #     return os.path.join(os.path.abspath("."), relative)
    return os.path.join(os.path.dirname(__file__), relative)


app_icon = resource_path('Icons/app.png')
logo_icon = resource_path('Icons/icons8-radio-waves-48.png')
homepath = os.path.join(os.path.dirname(sys.argv[0]), str(Path.home().absolute()))
dirpath = os.path.normpath(homepath + '/Music')
play_icon = resource_path('Icons/play.PNG')
pause_icon = resource_path('Icons/pause_icon_3.png')
prev_icon = resource_path('Icons/prev.png')
forward_icon = resource_path('Icons/forward.png')
stop_icon = resource_path('Icons/stop.png')
music_icon = resource_path("Icons/music.png")
ffprobe = resource_path('lib/ffprobe.exe')
ffplay = resource_path('lib/ffplay.exe')
logo_urls = resource_path('logo_urls/logo_urls.CSV')
