<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<addon id="plugin.video.flowplay" 
       name="Flow Play" 
       version="1.0.1" 
       provider-name="Jarko">
    <requires>
        <import addon="xbmc.python" version="3.0.0"/>
        <import addon="plugin.video.youtube" version="6.8.0"/>
        <import addon="script.module.requests" version="2.25.1"/>
        <import addon="script.module.urlresolver" version="5.0.0" optional="true"/>
    </requires>
    <extension point="xbmc.python.pluginsource" library="main.py">
        <provides>video</provides>
    </extension>
    <extension point="xbmc.addon.metadata">
        <summary lang="sk">Streamovací portál Flow Play</summary>
        <description lang="sk">Prístup k reláciám, logistike a detskému obsahu v rámci Flow Play systému.</description>
        <platform>all</platform>
        <assets>
            <icon>icon.png</icon>
            <fanart>fanart.jpg</fanart>
        </assets>
        <news>v1.0.1 - Pridaná sekcia Deti a oprava logistiky.</news>
    </extension>
</addon>
