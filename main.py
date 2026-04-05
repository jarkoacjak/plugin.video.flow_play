# -*- coding: utf-8 -*-
import sys
import urllib.parse
import xbmcgui
import xbmcplugin

# Pomocná funkcia na vytvorenie URL adries v menu
def build_url(query):
    return sys.argv[0] + '?' + urllib.parse.urlencode(query)

def main():
    handle = int(sys.argv[1])
    arg_string = sys.argv[2][1:] if len(sys.argv[2]) > 1 else ""
    params = dict(urllib.parse.parse_qsl(arg_string))

    mode = params.get('mode')

    # --- HLAVNÉ MENU ---
    if not mode:
        categories = [
            {"label": "Relácie", "mode": "relacie"},
            {"label": "Logistika", "mode": "logistika"},
            {"label": "Filmy", "mode": "filmy"},
            {"label": "Deti", "mode": "deti"}
        ]

        for kat in categories:
            # Vytvoríme položku v menu
            li = xbmcgui.ListItem(label="[B]" + kat["label"] + "[/B]")
            url = build_url({'mode': kat['mode']})
            # True znamená, že ide o priečinok (otvorí ďalšie menu)
            xbmcplugin.addDirectoryItem(handle, url, li, True)
        
        xbmcplugin.endOfDirectory(handle)

    # --- SEKCIA LOGISTIKA (Upútavka) ---
    elif mode == 'logistika':
        # Tvoje YouTube video pre Logistiku
        video_id = "_oFCqhIa9Ls"
        url = "plugin://plugin.video.youtube/play/?video_id=" + video_id
        
        li = xbmcgui.ListItem(label="Logistika - Upútavka")
        li.setInfo('video', {'title': 'Logistika Upútavka', 'plot': 'Pripravujeme čoskoro...'})
        li.setProperty('IsPlayable', 'true') # Povie Kodi, že je to video
        
        xbmcplugin.addDirectoryItem(handle, url, li, False)
        xbmcplugin.endOfDirectory(handle)

    # --- SEKCIA DETI (Bambuľka) ---
    elif mode == 'deti':
        # Zoznam epizód Bambuľky, ktoré si poslal
        episody = [
            {"label": "Bambuľka 1", "id": "UOCo8fLEoUo"},
            {"label": "Bambuľka 2", "id": "674vZJ_t4WA"},
            {"label": "Bambuľka 3 (Ešte sme nevysielali)", "id": "imTt7UiToYY"}
        ]

        for ep in episody:
            li = xbmcgui.ListItem(label=ep["label"])
            url = "plugin://plugin.video.youtube/play/?video_id=" + ep["id"]
            li.setProperty('IsPlayable', 'true')
            xbmcplugin.addDirectoryItem(handle, url, li, False)
            
        xbmcplugin.endOfDirectory(handle)

    # --- SEKCIE FILMY A RELÁCIE (Pripravujeme) ---
    else:
        oznam = "Už čoskoro pripravujeme..."
        label_text = "Relácie" if mode == 'relacie' else "Filmy"
        
        li = xbmcgui.ListItem(label="[I]" + label_text + " - " + oznam + "[/I]")
        # Prázdna URL, pretože tam ešte nič nie je
        xbmcplugin.addDirectoryItem(handle, "", li, False)
        xbmcplugin.endOfDirectory(handle)

if __name__ == '__main__':
    main()
       
