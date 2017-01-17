{{
# Grunddaten
form.guiInput('url', label='web2com-Server-IP', help="""Nur die reine IP des web2com-Servers - z.B. 192.168.178.100""")
form.guiInput('username', label='Username', help="""Benutzername zum Anmelden an der Weboberfläche des web2com""")
form.guiInput('password', label='Password', help="""zugehöriges Passwort""")
form.guiInput('cycle', label='Zykluszeit (alle x Sekunden)', pattern="integer")

# Werte
form.guiInput('oid01', label='Status Wärmeerzeuger', help="""zugehörige Adresse, z.B. /1/2/1/125/0""")
form.guiInput('oid02', label='IST Temp.Wärmepumpe-Vorlauf', help="""zugehörige Adresse, z.B. /1/2/1/125/0""")
form.guiInput('oid03', label='IST Temp.Wärmepumpe-Rücklauf', help="""zugehörige Adresse, z.B. /1/2/1/125/0""")
form.guiInput('oid04', label='IST Temp.Quellenausgang', help="""zugehörige Adresse, z.B. /1/2/1/125/0""")
form.guiInput('oid05', label='IST Temp.Quelleneingang', help="""zugehörige Adresse, z.B. /1/2/1/125/0""")
form.guiInput('oid06', label='Schaltzyklen', help="""zugehörige Adresse, z.B. /1/2/1/125/0""")
form.guiInput('oid07', label='Betriebsstunden', help="""zugehörige Adresse, z.B. /1/2/1/125/0""")
form.guiInput('oid08', label='Volumenstrom Wärmenutzung', help="""zugehörige Adresse, z.B. /1/2/1/125/0""")
form.guiInput('oid09', label='Volumenstrom Wärmequelle', help="""zugehörige Adresse, z.B. /1/2/1/125/0""")
}}
