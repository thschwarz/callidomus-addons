# Heizungswidget

![Heizungswidget-Anzeige](screen.png)<br>
Basis für das Widget war die Anzeige an einer Ochsner Wärmepumpe.<br>
Das Beispiel wurde von "mumpf" (Waldemar) und "RoyalTS" (Thorsten) erstellt.

# Installation
Einfach kompletten Ordner unter 

> /data/callidomus/local/visu/widgets 

kopieren.
Und in der Konsole folgendes ausführen:

> callidomus.gui build

Danach Widget in der Visualisierung einfügen.


Parameter:
* 'Status' : Item des Status-Textes der Heizung (z.B. WP.Heizung.Statustext - "0: Ausgeschalten" oder "1: Normal Heizbetrieb")
* 'Fussbodenheizung (Temp)' : z.B. Vorlauftemperatur des Heizkreises in °C
* 'Außentemperatur' : Außentemperatur in °C
* 'Innentemperatur' : Innentemperatur in °C
* 'Warmwassertemperatur' : Warmwassertemperatur in °C
* 'Status Kopfzeile' : Der Wert dieses Items wird in der Kopfzeile ausgegeben (z.B. Heizleistung)

![Heizungs-Visu](visu.png)
