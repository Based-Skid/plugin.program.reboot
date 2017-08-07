import xbmc
import xbmcaddon, xbmcgui, xbmcplugin,os,sys,xbmcvfs
import shutil
import urllib2,urllib
import re



if(xbmc.getCondVisibility("Player.HasMedia") == False):
            xbmc.executebuiltin("Reset")
else:
            xbmc.executebuiltin("Action(Back)")
