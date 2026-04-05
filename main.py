import sys
import urllib.parse
import xbmcgui
import xbmcplugin

# Pomocná funkcia na navigáciu v menu
def build_url(query):
    return sys.argv[0] + '?' + urllib.parse.urlencode(query)

def main():
    handle = int(sys.argv[1])
    arg_string = sys.argv[2][1:] if len(sys.argv[2]) > 1 else ""
    params = dict(urllib.parse.parse_qsl(arg_string))

    mode = params.get('mode')

    # HLAVNÉ MENU
    if not mode:
        categories = [
            {"label": "Relácie", "mode": "relacie"},
            {"label": "Logistika", "mode": "logistika"},
            {"label": "Filmy", "mode": "filmy"},
            {"label": "Deti", "mode": "deti"}
        ]

        for kat in categories:
            li = xbmcgui.ListItem(label="[B]" + kat["label"] + "[/B]")
            url = build_url({'mode': kat['mode']})
            xbmcplugin.addDirectoryItem(handle, url, li, True)
        
        xbmcplugin.endOfDirectory(handle)

    # SEKCIA LOGISTIKA - Spustí upútavku
    elif mode == 'logistika':
        video_url = "https://www.youtube.com/watch?v=_oFCqhIa9Ls"
        # plugin://plugin.video.youtube/ kód pre priame spustenie cez YT doplnok
        final_url = "plugin://plugin.video.youtube/play/?video_id=_oFCqhIa9Ls"
        
        li = xbmcgui.ListItem(label="Logistika - Upútavka")
        li.setInfo('video', {'title': 'Logistika Upútavka', 'plot': 'Pripravujeme čoskoro...'})
        li.setProperty('IsPlayable', 'true')
        
        xbmcplugin.addDirectoryItem(handle, final_url, li, False)
        xbmcplugin.endOfDirectory(handle)

    # SEKCIA DETI - Zoznam epizód
    elif mode == 'deti':
        episody = [
            {"label": "Bambuľka 1", "id": "UOCo8fLEoUo"},
            {"label": "Bambuľka 2", "id": "674vZJ_t4WA"},
            {"label": "Bambuľka 3 (Ešte sme nevysielali)", "id": "imTt7UiToYY"}
        ]

        for ep in episody:
            li = xbmcgui.ListItem(label=ep["label"])
            # Ak je to 3. epizóda, môžeme len vypísať info alebo ju nechať prehrať
            url = "plugin://plugin.video.youtube/play/?video_id=" + ep["id"]
            li.setProperty('IsPlayable', 'true')
            xbmcplugin.addDirectoryItem(handle, url, li, False)
            
        xbmcplugin.endOfDirectory(handle)

    # OSTATNÉ SEKCIE (Relácie, Filmy)
    else:
        oznam = "Už čoskoro pripravujeme..."
        li = xbmcgui.ListItem(label="[I]" + mode.capitalize() + " - " + oznam + "[/I]")
        xbmcplugin.addDirectoryItem(handle, "", li, False)
        xbmcplugin.endOfDirectory(handle)

if __name__ == '__main__':
    main()
    
