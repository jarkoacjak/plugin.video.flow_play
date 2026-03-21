importovať systém
import urllib.parse
importovať xbmcgui
importovať plugin xbmc

# Pomocná funkcia na navigáciu v menu
def build_url(dotaz):
    vrátiť sys.argv[0] + '?' + urllib.parse.urlencode(dotaz)

def main():
    handle = int(sys.argv[1])
    arg_string = sys.argv[2][1:] ak len(sys.argv[2]) > 1 inak ""
    params = dict(urllib.parse.parse_qsl(arg_string))

    # HLAVNÉ MENU (zobrazí sa hneď po otvorení)
    ak nie parametre:
        kategória = [
            {"label": "Relácie", "mode": "relacie"},
            {"label": "Logistika", "mode": "logistika"},
            {"label": "Filmový", "mode": "filmový"}
        ]

        pre kat v kategórii:
            li = xbmcgui.ListItem(label="[B]" + kat["label"] + "[/B]")
            url = build_url({'režim': kat['režim']})
            xbmcplugin.addDirectoryItem(handle, url, li, True)
        
        xbmcplugin.endOfDirectory(handle)

    # SEKCIE (čo sa stane po kliknutí)
    inak:
        režim = params.get('režim')
        oznam = "Už čoskoro pripravujeme..."
        
        # Vytvoríme jednoduchý riadok s informáciou
        ak režim == 'relacie':
            li = xbmcgui.ListItem(label="[I]Relácie - " + oznam + "[/I]")
        elif mode == 'logistika':
            li = xbmcgui.ListItem(label="[I]Logistika - " + oznam + "[/I]")
        režim elif == 'filmový':
            li = xbmcgui.ListItem(label="[I]Filmový - " + oznam + "[/I]")
        
        xbmcplugin.addDirectoryItem(handle, "", li, False)
        xbmcplugin.endOfDirectory(handle)

ak __name__ == '__main__':
    hlavný()


