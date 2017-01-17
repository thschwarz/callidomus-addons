# Diese Imports muessen immer da sein
import collections

import widgets


# Der Name der Widget-Klasse muss immer wie das Widget heißen, nur mit einem Großbuchstaben beginnen
class Heizung(widgets.Widget):

    # Als erstes muss man die API vom Widget beschreiben, also wie wird das Widget technisch aufgerufen
    api = {
        # Name des Widgets (derzeit nur Kleinbuchstaben und Zahlen)
        'name': 'Heizung',
        # Beschreibung des Widgets
        'desc': 'Heizungswidget für Fussboden- und Warmwasserheizung (Vorlage: web2com Wärmepumpenanzeige)',
        'cat': 'Value',
        # Beispielcode für den Aufruf
        # Das folgende MUSS syntaktisch korrekt sein, da es für den Visu- und GUI-Build genutzt wird!
        'examples': [
            {'code': "Heizung(item='demo.temperature', fbh='demo.rtr.set',\
                aussen='demo.rtr.mode', innen='demo.rtr.open', h2o='demo.rtr.set',\
                name='Heizung', desc='Heizung')"},
            {'code': "Heizung(item='demo.temperature', qvl='demo.rtr.set',\
                qrl='demo.rtr.set',aussen='demo.rtr.mode', wpvl='demo.rtr.open',\
                status='demo.rts.state', name='Heizung', desc='Heizung', showstatus=1)"}
        ],
    }

    # Ab hier wird der Dialog fuer den Widget-Editor im GUI definiert
    def __init__(self):
        # Die folgende Zeile ist notwendig
        widgets.Widget.__init__(self)

        # Jedes Widget hat mindestens eine Item-Referenz, der Parameter item ist somit bereits definiert, wir geben dem Paramter
        # nur noch seinen Namen
        self.params['item']['label'] = 'Status'

        # Eine vollstaendige Item-Parameter-Definition mit Namen (label), Wertebereich (pattern), Argumentnotwendigkeit (required),
        # Clickaktion (onfocus) und Online-Hilfe (help). Daraus wird in der GUI ein Eingabefeld für ein Item.
        self.params['fbh'] = {'label': 'Fussbodenheizung (Temp)', 'pattern': 'item', 'required': None,
                              'onfocus': 'cg.acItems.focus(this);',
                              'help': """ Temperatur der Fussbodenheizung in °C """}

        self.params['aussen'] = {'label': 'Außentemperatur', 'pattern': 'item', 'required': None,
                               'onfocus': 'cg.acItems.focus(this);',
                               'help': """ Außentemperatur in °C """}

        self.params['innen'] = {'label': 'Innentemperatur', 'pattern': 'item', 'required': None,
                               'onfocus': 'cg.acItems.focus(this);',
                               'help': """ Innentemperatur in °C """}

        self.params['h2o'] = {'label': 'Warmwassertemperatur', 'pattern': 'item', 'required': None,
                               'onfocus': 'cg.acItems.focus(this);',
                               'help': """ Warmwassertemperatur in °C """}

        self.params['state'] = {'label': 'Status Kopfzeile', 'pattern': 'item', 
                               'onfocus': 'cg.acItems.focus(this);',
                               'help': """ Der Wert dieses Items wird in der Kopfzeile ausgegeben (z.B. Heizleistung)"""}

        self.params['showstatus'] = {
            'label': 'Status im Gruppenkopf anzeigen',
            'type': 'checkbox',
            'checked': None,
            'help': """Wenn dieses Flag gesetzt ist, dann wird der Wert vom 'Status' in der Kopfzeile angezeigt.""",
        }

        # Hiermit kann man die Reihenfolge der Parameter auf der Eingabemaske bestimmen (in umgekehrter Reihnefolge, von unten nach oben)
        self.params.move_to_end('h2o', last=False)
        self.params.move_to_end('innen', last=False)
        self.params.move_to_end('aussen', last=False)
        self.params.move_to_end('fbh', last=False)
        self.params.move_to_end('item', last=False)

    # Das folgende Coding bringt das SVG auf die HTML-Seite der Visu und sagt der Visu auch, welche Items
    # dargestellt werden solen. Die Werte dieser Items aktualisiern sich dann auch automatisch.
    def __call__(self, **kwargs):
        # Notwendige Zeile
        self.include(__file__)

        # Defaultparameter, die vorbelegt werden
        kwargs.setdefault("size", "m")
        kwargs.setdefault("showstatus", 0)

        # Diese Items werden dargestellt und aktualisiert, deren Namen wurde in der oben definierten Maske eingegeben 
        # und stehen in kwargs
        items = [kwargs['item'], kwargs['fbh'], kwargs['aussen'], kwargs['innen'], kwargs['h2o']]

        # Statusausgabe in der Kopfzeile der Gruppe
        # Hier soll exemplarisch eine kleine "Dynamisierung" gezeigt werden
        # Die Statusausgabe wird nur gemacht, wenn auch das entsprechende Flag angegeben ist und das Statusitem vorbelegt ist
        if int(kwargs['showstatus']) == 1 and 'state' in kwargs:
            # Das Statusitem muss dann auch an Javascript gegeben werden
            items.append(kwargs['state'])
            # Das html für die Statusausgabe, nutzt das normale value-widget, deswegen ist kein extra javascript fuer ein Wertupdate noetig
            showStatusHtml = '<span class="showState">' + self.widgets['value'].html(item=kwargs['state'], round=1) + '</span>'
            # und der Laufzeit dieses html als Statusinfo übergeben 
            kwargs['status'] = showStatusHtml

        # Hier wird das Aussehen des Detail-Widgets bestimmt. Das ist das Widget für den Tablet- und Browser-Modus
        # Technisch wird hier das SVG geladen und auf die HTML-Seite gebracht. Ferner bekommt das SVG noch einen 
        # Namen, damit man es spaeter finden kann
        kwargs['detail'] = self.load(
            "widgets/Heizung/detail.svg",
            {'class': 'heizungDetail'})
        # Hier wird das Aussehen des Digest-Widgets bestimmt. Das ist das Widget für den Mobile-Modus (Handy)
        # Bei diesem Widget sieht der Handy-Modus genau so aus wie der Tablet-Modus, trotzdem bekommt das 
        # Widget einen eigenen Namen
        kwargs['digest'] = self.load(
            "widgets/Heizung/detail.svg",
            {'class': 'heizungDigest'})
        # Die oben definierten Items werden hier uebergeben, damit sie gelesen und aktualisiert werden koennen
        kwargs['attr'] = {'data-item': ' '.join(items)}
        # Und der Widget-Name wird noch uebergeben
        kwargs['widget'] = self.name
        # Hier wird technisch auf die HTML-Seite der Visu geschrieben
        print(self.frame(kwargs))

