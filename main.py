# -*- coding: utf-8 -*-
import sys
import urllib.parse
import xbmcgui
import xbmcplugin

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
            {"label": "Filmy", "mode": "filmy"},
            {"label": "Deti", "mode": "deti"}
        ]

        for kat in categories:
            li = xbmcgui.ListItem(label="[B]" + kat["label"] + "[/B]")
            url = build_url({'mode': kat['mode']})
            xbmcplugin.addDirectoryItem(handle, url, li, True)
        
        xbmcplugin.endOfDirectory(handle)

    # --- SEKCIA RELÁCIE (Logistika s automatickou upútavkou) ---
    elif mode == 'relacie':
        video_id = "_oFCqhIa9Ls"
        url = "plugin://plugin.video.youtube/play/?video_id=" + video_id
        
        li = xbmcgui.ListItem(label="Logistika")
        li.setInfo('video', {
            'title': 'Logistika', 
            'plot': 'Pripravujeme čoskoro... Po kliknutí sa spustí upútavka.'
        })
        li.setProperty('IsPlayable', 'true')
        
        xbmcplugin.addDirectoryItem(handle, url, li, False)
        xbmcplugin.endOfDirectory(handle)

    # --- SEKCIA DETI (Bambuľka) ---
    elif mode == 'deti':
        # 1. a 2. epizóda sú normálne videá
        episody = [
            {"label": "Bambuľka 1", "id": "UOCo8fLEoUo", "info": ""},
            {"label": "Bambuľka 2", "id": "674vZJ_t4WA", "info": ""},
        ]

        for ep in episody:
            li = xbmcgui.ListItem(label=ep["label"])
            url = "plugin://plugin.video.youtube/play/?video_id=" + ep["id"]
            li.setProperty('IsPlayable', 'true')
            xbmcplugin.addDirectoryItem(handle, url, li, False)
            
        # 3. epizóda - len textové oznámenie
        li3 = xbmcgui.ListItem(label="Bambuľka 3")
        li3.setInfo('video', {
            'title': 'Bambuľka 3',
            'plot': 'Ešte sme nevysielali alebo nebola pridaná.'
        })
        # Pri tejto položke nedávame URL, aby sa nič nespustilo, len ukázal text
        xbmcplugin.addDirectoryItem(handle, "", li3, False)
            
        xbmcplugin.endOfDirectory(handle)

    # --- SEKCIA FILMY ---
    elif mode == 'filmy':
        li = xbmcgui.ListItem(label="[I]Filmy - Už čoskoro...[/I]")
        xbmcplugin.addDirectoryItem(handle, "", li, False)
        xbmcplugin.endOfDirectory(handle)

if __name__ == '__main__':
    main()
    
