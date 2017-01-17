# Diese Imports muessen immer da sein
import collections
import widgets

# Der Name der Widget-Klasse muss immer wie das Widget heißen, nur mit einem Großbuchstaben beginnen
class Waermepumpe(widgets.Widget):

    # Als erstes muss man die API vom Widget beschreiben, also wie wird das Widget technisch aufgerufen
    api = {
        # Name des Widgets (derzeit nur Kleinbuchstaben und Zahlen)
        'name': 'Waermepumpe',
        # Beschreibung des Widgets
        'desc': 'Wäremepumpen-Widget (Vorlage: web2com Wärmepumpen)',
        'cat': 'Value',
        # Beispielcode für den Aufruf
        # Das folgende MUSS syntaktisch korrekt sein, da es für den Visu- und GUI-Build genutzt wird!
        'examples': [
            {'code': "Waermepumpe(item='demo.temperature', qvl='demo.rtr.set',\
                qrl='demo.rtr.set',aussen='demo.rtr.mode', wpvl='demo.rtr.open',\
                name='Waermepumpe', desc='Wärmepumpe')"},
            {'code': "Waermepumpe(item='demo.temperature', qvl='demo.rtr.set',\
                qrl='demo.rtr.set',aussen='demo.rtr.mode', wpvl='demo.rtr.open',\
                status='demo.rts.state', name='Waermepumpe', desc='Wärmepumpe', showstatus=1)"}
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
        self.params['qvl'] = {'label': 'Quelle - Vorlauf', 'pattern': 'item', 'required': None,
                              'onfocus': 'cg.acItems.focus(this);',
                              'help': """ Temperatur des Vorlaufs zur WP-Quelle in °C """}

        self.params['qrl'] = {'label': 'Quelle - Rücklauf', 'pattern': 'item', 'required': None,
                              'onfocus': 'cg.acItems.focus(this);',
                              'help': """ Temperatur des Rücklaufs von der WP-Quelle in °C """}

        self.params['aussen'] = {'label': 'Außentemperatur', 'pattern': 'item', 'required': None,
                               'onfocus': 'cg.acItems.focus(this);',
                               'help': """ Außentemperatur in °C """}

        self.params['wpvl'] = {'label': 'Vorlauf der WP', 'pattern': 'item', 'required': None,
                               'onfocus': 'cg.acItems.focus(this);',
                               'help': """ Temperatur des Wärmepumpen Vorlaufs in °C """}

        self.params['wprl'] = {'label': 'Rücklauf der WP', 'pattern': 'item', 'required': None,
                               'onfocus': 'cg.acItems.focus(this);',
                               'help': """ Temperatur des Wärmepumpen Rücklaufs in °C """}

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
        self.params.move_to_end('wprl', last=False)
        self.params.move_to_end('wpvl', last=False)
        self.params.move_to_end('aussen', last=False)
        self.params.move_to_end('qvl', last=False)
        self.params.move_to_end('qrl', last=False)
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
        items = [kwargs['item'], kwargs['qvl'], kwargs['qrl'], kwargs['aussen'], kwargs['wpvl'], kwargs['wprl']]

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
            "widgets/waermepumpe/detail.svg",
            {'class': 'waermepumpeDetail'})
        # Hier wird das Aussehen des Digest-Widgets bestimmt. Das ist das Widget für den Mobile-Modus (Handy)
        # Bei diesem Widget sieht der Handy-Modus genau so aus wie der Tablet-Modus, trotzdem bekommt das 
        # Widget einen eigenen Namen
        kwargs['digest'] = self.load(
            "widgets/waermepumpe/detail.svg",
            {'class': 'waermepumpeDigest'})
        # Die oben definierten Items werden hier uebergeben, damit sie gelesen und aktualisiert werden koennen
        kwargs['attr'] = {'data-item': ' '.join(items)}
        # Und der Widget-Name wird noch uebergeben
        kwargs['widget'] = self.name
        # Hier wird technisch auf die HTML-Seite der Visu geschrieben
        print(self.frame(kwargs))
