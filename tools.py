# -*- coding: utf-8 -*-
import xbmc
import xbmcgui
import xbmcaddon
import os

ADDON = xbmcaddon.Addon()
CACHE_DIR = xbmc.translatePath(ADDON.getAddonInfo('profile'))

if not os.path.exists(CACHE_DIR):
    os.makedirs(CACHE_DIR)

def play_video(url, title):
    """Spustí prehrávanie videa s názvom"""
    listitem = xbmcgui.ListItem(title)
    listitem.setInfo('video', {'title': title})
    xbmc.Player().play(url, listitem)

def notify(message):
    """Zobrazí oznámenie Flow Play"""
    xbmcgui.Dialog().notification("Flow Play", message, xbmcgui.NOTIFICATION_INFO, 5000)

def log(msg):
    xbmc.log(f"FLOW_PLAY_LOG: {msg}", xbmc.LOGINFO)

