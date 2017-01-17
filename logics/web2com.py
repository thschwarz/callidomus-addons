import requests

url='http://192.168.1.200/ws'
username="USER"
password="123"
headers = {
    'Content-Type': 'text/xml; charset=UTF-8',
    'SOAPAction': 'http://ws01.lom.ch/soap/getDP',
}

def web2com_values(oid):
    data = '<?xml version="1.0" encoding="UTF-8"?><SOAP-ENV:Envelope xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/" xmlns:SOAP-ENC="http://schemas.xmlsoap.org/soap/encoding/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:ns="http://ws01.lom.ch/soap/"><SOAP-ENV:Body><ns:getDpRequest><ref><oid>' + oid + '</oid><prop/></ref><startIndex>0</startIndex><count>1</count></ns:getDpRequest></SOAP-ENV:Body></SOAP-ENV:Envelope>'
    resp = requests.post(url, auth=(username,password), headers=headers, data=data)
    if resp.text.find("faultstring") < 0:
        return resp.text[(resp.text.index("<value>")+len("<value>")):resp.text.index("</value>")]   
    else :
        return 0

cd.WP.Waermepumpe.Betriebsdaten.Betriebsstunden = web2com_values('/1/2/1/125/7')
cd.WP.Waermepumpe.Betriebsdaten.IstTempTQA = web2com_values('/1/2/1/125/4')
cd.WP.Waermepumpe.Betriebsdaten.IstTempTQE = web2com_values('/1/2/1/125/5')
cd.WP.Waermepumpe.Betriebsdaten.IstTempTWV = web2com_values('/1/2/1/125/1')
cd.WP.Waermepumpe.Betriebsdaten.IstTempTWR = web2com_values('/1/2/1/125/3')
cd.WP.Waermepumpe.Betriebsdaten.Schaltzyklen = web2com_values('/1/2/1/125/6')
cd.WP.Waermepumpe.Betriebsdaten.VolumenstromWaermenutzung = web2com_values('/1/2/1/125/8')
cd.WP.Waermepumpe.Betriebsdaten.VolumenstromWaermequelle = web2com_values('/1/2/1/125/9')
cd.WP.Waermepumpe.Betriebsdaten.VorlauftempSollwert = web2com_values('/1/2/1/125/2')
cd.WP.Waermepumpe.Betriebsdaten.Leistung =  60/1000*cd.WP.Waermepumpe.Betriebsdaten.VolumenstromWaermequelle*abs(cd.WP.Waermepumpe.Betriebsdaten.IstTempTQA-cd.WP.Waermepumpe.Betriebsdaten.IstTempTQE)*1.163
temp = web2com_values('/1/2/1/125/0')
cd.WP.Waermepumpe.Betriebsdaten.StatusWaermeerzeuger = temp

if int(temp) == 0:
    cd.WP.Waermepumpe.Betriebsdaten.Statustext = '0: Abgeschalten'
elif int(temp) == 1:
    cd.WP.Waermepumpe.Betriebsdaten.Statustext = '1: Heizbetrieb'
elif int(temp) == 2:
    cd.WP.Waermepumpe.Betriebsdaten.Statustext = '2: Vorlaufzeit Heizbetrieb'
elif int(temp) == 3:
    cd.WP.Waermepumpe.Betriebsdaten.Statustext = '3: Extern gesperrt'
elif int(temp) == 4:
    cd.WP.Waermepumpe.Betriebsdaten.Statustext = '4: Kühlbetrieb'
elif int(temp) == 5:
    cd.WP.Waermepumpe.Betriebsdaten.Statustext = '5: Vorlaufzeit Kühlbetrieb'
elif int(temp) == 6:
    cd.WP.Waermepumpe.Betriebsdaten.Statustext = '6: Vorlaufzeit Abtaubetrieb'
elif int(temp) == 7:
    cd.WP.Waermepumpe.Betriebsdaten.Statustext = '7: Abtaubetrieb'
elif int(temp) == 8:
    cd.WP.Waermepumpe.Betriebsdaten.Statustext = '8: Störung'
elif int(temp) == 9:
    cd.WP.Waermepumpe.Betriebsdaten.Statustext = '9: Abtropfen'
elif int(temp) == 10:
    cd.WP.Waermepumpe.Betriebsdaten.Statustext = '10: Abtausperrzeit'
elif int(temp) == 11:
    cd.WP.Waermepumpe.Betriebsdaten.Statustext = '11: Abtau Vorheizung'
elif int(temp) == 12:
    cd.WP.Waermepumpe.Betriebsdaten.Statustext = '12: Abtauen 1'
elif int(temp) == 13:
    cd.WP.Waermepumpe.Betriebsdaten.Statustext = '13: Abtauen 2'
elif int(temp) == 14:
    cd.WP.Waermepumpe.Betriebsdaten.Statustext = '14: Abtauen 3'
elif int(temp) == 15:
    cd.WP.Waermepumpe.Betriebsdaten.Statustext = '15: Alarm'
elif int(temp) == 16:
    cd.WP.Waermepumpe.Betriebsdaten.Statustext = '16: Störung - Wärmequelle zu kalt'
elif int(temp) == 17:
    cd.WP.Waermepumpe.Betriebsdaten.Statustext = '17: Blockiert'
elif int(temp) == 18:
    cd.WP.Waermepumpe.Betriebsdaten.Statustext = '18: Vorglühen'
elif int(temp) == 19:
    cd.WP.Waermepumpe.Betriebsdaten.Statustext = '19: Eindüsung Ein'
elif int(temp) == 20:
    cd.WP.Waermepumpe.Betriebsdaten.Statustext = '20: Eindüsung Aus'
elif int(temp) == 22:
    cd.WP.Waermepumpe.Betriebsdaten.Statustext = '22: TWVmax Abschaltung'
elif int(temp) == 23:
    cd.WP.Waermepumpe.Betriebsdaten.Statustext = '23: TWEmax Abschaltung'
elif int(temp) == 24:
    cd.WP.Waermepumpe.Betriebsdaten.Statustext = '24: TWAmin Abschaltung'
elif int(temp) == 25:
    cd.WP.Waermepumpe.Betriebsdaten.Statustext = '25: TKAmin Abschaltung'
elif int(temp) == 26:
    cd.WP.Waermepumpe.Betriebsdaten.Statustext = '26: Bivalzenabschaltung'
elif int(temp) == 27:
    cd.WP.Waermepumpe.Betriebsdaten.Statustext = '27: Warmwasser Ladesperre'
elif int(temp) == 28:
    cd.WP.Waermepumpe.Betriebsdaten.Statustext = '28: Minimale Auszeit'
elif int(temp) == 29:
    cd.WP.Waermepumpe.Betriebsdaten.Statustext = '29: Minimale Einzeit'
elif int(temp) == 30:
    cd.WP.Waermepumpe.Betriebsdaten.Statustext = '30: Anheizen'
elif int(temp) == 31:
    cd.WP.Waermepumpe.Betriebsdaten.Statustext = '31: Ausbrand'
elif int(temp) == 32:
    cd.WP.Waermepumpe.Betriebsdaten.Statustext = '32: Pumpen-Nachlauf'
elif int(temp) == 33:
    cd.WP.Waermepumpe.Betriebsdaten.Statustext = '33: Verzögerung Folge-WE'
elif int(temp) == 34:
    cd.WP.Waermepumpe.Betriebsdaten.Statustext = '34: Betrieb Übertemperatur'
elif int(temp) == 35:
    cd.WP.Waermepumpe.Betriebsdaten.Statustext = '35: Fülltüre geöffnet'
elif int(temp) == 36:
    cd.WP.Waermepumpe.Betriebsdaten.Statustext = '36: Passivkühlung'
elif int(temp) == 37:
    cd.WP.Waermepumpe.Betriebsdaten.Statustext = '37: Heizbetrieb angefordert'
elif int(temp) == 38:
    cd.WP.Waermepumpe.Betriebsdaten.Statustext = '38: Kühlbetrieb angefordert'
else:
    cd.WP.Waermepumpe.Betriebsdaten.Statustext = temp

cd.WP.Fussbodenheizung.Betriebsdaten.Aussentemperatur = web2com_values('/1/2/5/119/1')
cd.WP.Fussbodenheizung.Betriebsdaten.HeizkreisVorlauftemperatur = web2com_values('/1/2/5/119/5')
cd.WP.Fussbodenheizung.Betriebsdaten.MittelwertAussentemperatur = web2com_values('/1/2/5/119/2')
cd.WP.Fussbodenheizung.Betriebsdaten.Raumtemperatur = web2com_values('/1/2/5/119/3')
cd.WP.Fussbodenheizung.Betriebsdaten.RelativeFeuchte = web2com_values('/1/2/5/119/7')
cd.WP.Fussbodenheizung.Betriebsdaten.SollwertHeizkreisVorlauftemperatur = web2com_values('/1/2/5/119/6')
cd.WP.Fussbodenheizung.Betriebsdaten.SollwertRaumtemperatur = web2com_values('/1/2/5/119/4')

temp = web2com_values('/1/2/5/119/0')
cd.WP.Fussbodenheizung.Betriebsdaten.StatusHeizkreis = temp

if int(temp) == 0:
    cd.WP.Fussbodenheizung.Betriebsdaten.Statustext = '0: Abgeschaltet'
elif int(temp) == 1:
    cd.WP.Fussbodenheizung.Betriebsdaten.Statustext = '1: Normal Heizbetrieb'
elif int(temp) == 2:
    cd.WP.Fussbodenheizung.Betriebsdaten.Statustext = '2: Komfort Heizbetrieb'
elif int(temp) == 3:
    cd.WP.Fussbodenheizung.Betriebsdaten.Statustext = '3: Spar Heizbetrieb'
elif int(temp) == 4:
    cd.WP.Fussbodenheizung.Betriebsdaten.Statustext = '4: Frostschutzbetrieb'
elif int(temp) == 5:
    cd.WP.Fussbodenheizung.Betriebsdaten.Statustext = '5: Zwangsabnahme'
elif int(temp) == 6:
    cd.WP.Fussbodenheizung.Betriebsdaten.Statustext = '6: Zwangsdrosselung'
elif int(temp) == 7:
    cd.WP.Fussbodenheizung.Betriebsdaten.Statustext = '7: Ferienbetrieb'
elif int(temp) == 8:
    cd.WP.Fussbodenheizung.Betriebsdaten.Statustext = '8: Partybetrieb'
elif int(temp) == 9:
    cd.WP.Fussbodenheizung.Betriebsdaten.Statustext = '9: Normal Kühlbetrieb'
elif int(temp) == 10:
    cd.WP.Fussbodenheizung.Betriebsdaten.Statustext = '10: Komfort Kühlbetrieb'
elif int(temp) == 11:
    cd.WP.Fussbodenheizung.Betriebsdaten.Statustext = '11: Spar Kühlbetrieb'
elif int(temp) == 12:
    cd.WP.Fussbodenheizung.Betriebsdaten.Statustext = '12: Störung'
elif int(temp) == 13:
    cd.WP.Fussbodenheizung.Betriebsdaten.Statustext = '13: Handbetrieb'
elif int(temp) == 14:
    cd.WP.Fussbodenheizung.Betriebsdaten.Statustext = '14: Schutz Kühlbetrieb'
elif int(temp) == 15:
    cd.WP.Fussbodenheizung.Betriebsdaten.Statustext = '15: Partybetrieb Kühlen'
elif int(temp) == 16:
    cd.WP.Fussbodenheizung.Betriebsdaten.Statustext = '16: Austrocknung Aufheizen'
elif int(temp) == 17:
    cd.WP.Fussbodenheizung.Betriebsdaten.Statustext = '17: Austrocknung Stationär'
elif int(temp) == 18:
    cd.WP.Fussbodenheizung.Betriebsdaten.Statustext = '18: Austrocknung Auskühlen'
elif int(temp) == 19:
    cd.WP.Fussbodenheizung.Betriebsdaten.Statustext = '19: Austrocknung Endphase'
elif int(temp) == 20:
    cd.WP.Fussbodenheizung.Betriebsdaten.Statustext = '20: Nachtlüftung'
elif int(temp) == 21:
    cd.WP.Fussbodenheizung.Betriebsdaten.Statustext = '21: Belüftung'
elif int(temp) == 22:
    cd.WP.Fussbodenheizung.Betriebsdaten.Statustext = '22: Kühlbetrieb extern'
elif int(temp) == 23:
    cd.WP.Fussbodenheizung.Betriebsdaten.Statustext = '23: Heizbetrieb extern'
else :
    cd.WP.Fussbodenheizung.Betriebsdaten.Statustext = temp

cd.WP.Waermeverteiler.Betriebsdaten.AnlageVorlauftemperatur = web2com_values('/1/2/8/122/2')
cd.WP.Waermeverteiler.Betriebsdaten.HeizleistungHeizbetrieb = web2com_values('/1/2/8/122/4')
cd.WP.Waermeverteiler.Betriebsdaten.HeizleistungWarmwasserbetrieb = web2com_values('/1/2/8/122/5')
cd.WP.Waermeverteiler.Betriebsdaten.IstTempTPMPuffertemperatur = web2com_values('/1/2/8/122/1')
cd.WP.Waermeverteiler.Betriebsdaten.IstTempTPOPuffertemperatur = web2com_values('/1/2/8/122/0')
cd.WP.Waermeverteiler.Betriebsdaten.SollwertAnlagevorlauf = web2com_values('/1/2/8/122/3')

temp = web2com_values('/1/2/8/122/6')
cd.WP.Waermeverteiler.Betriebsdaten.StatusWaermemanager = temp

if int(temp) == 0:
    cd.WP.Waermeverteiler.Betriebsdaten.Statustext = '0: Abgeschaltet'
elif int(temp) == 1:
    cd.WP.Waermeverteiler.Betriebsdaten.Statustext = '1: Heizen'
elif int(temp) == 2:
    cd.WP.Waermeverteiler.Betriebsdaten.Statustext = '2: Kühlen'
elif int(temp) == 3:
    cd.WP.Waermeverteiler.Betriebsdaten.Statustext = '3: WWA'
elif int(temp) == 4:
    cd.WP.Waermeverteiler.Betriebsdaten.Statustext = '4: PWA'
elif int(temp) == 5:
    cd.WP.Waermeverteiler.Betriebsdaten.Statustext = '5: Heizen Kühlen'
elif int(temp) == 6:
    cd.WP.Waermeverteiler.Betriebsdaten.Statustext = '6: Heizen WWA'
elif int(temp) == 7:
    cd.WP.Waermeverteiler.Betriebsdaten.Statustext = '7: Heizen PWA'
elif int(temp) == 8:
    cd.WP.Waermeverteiler.Betriebsdaten.Statustext = '8: Heizen Kühlen WWA'
elif int(temp) == 9:
    cd.WP.Waermeverteiler.Betriebsdaten.Statustext = '9: Heizen Kühlen PWA'
elif int(temp) == 10:
    cd.WP.Waermeverteiler.Betriebsdaten.Statustext = '10: Heizen WWA PWA'
elif int(temp) == 11:
    cd.WP.Waermeverteiler.Betriebsdaten.Statustext = '11: Heizen Kühlen WWA PWA'
elif int(temp) == 12:
    cd.WP.Waermeverteiler.Betriebsdaten.Statustext = '12: Kühlen WWA'
elif int(temp) == 13:
    cd.WP.Waermeverteiler.Betriebsdaten.Statustext = '13: Kühlen PWA'
elif int(temp) == 14:
    cd.WP.Waermeverteiler.Betriebsdaten.Statustext = '14: Kühlen WWA PWA'
elif int(temp) == 15:
    cd.WP.Waermeverteiler.Betriebsdaten.Statustext = '15: WWA PWA'
elif int(temp) == 16:
    cd.WP.Waermeverteiler.Betriebsdaten.Statustext = '16: Störung'
else:
    cd.WP.Waermeverteiler.Betriebsdaten.Statustext = temp
    
cd.WP.Warmwasserkreis.Betriebsdaten.IstTempTBWarmwasser = web2com_values('/1/2/7/121/1')
cd.WP.Warmwasserkreis.Betriebsdaten.SollwertWarmwassertemperatur = web2com_values('/1/2/7/121/2')

temp = web2com_values('/1/2/7/121/0')
cd.WP.Warmwasserkreis.Betriebsdaten.StatusWarmwasser = temp

if int(temp) == 0:
    cd.WP.Warmwasserkreis.Betriebsdaten.Statustext = '0: Abgeschaltet'
elif int(temp) == 1:
    cd.WP.Warmwasserkreis.Betriebsdaten.Statustext = '1: Normal Ladebetrieb'
elif int(temp) == 2:
    cd.WP.Warmwasserkreis.Betriebsdaten.Statustext = '2: Komfort Ladebetrieb'
elif int(temp) == 3:
    cd.WP.Warmwasserkreis.Betriebsdaten.Statustext = '3: Zwangsdrosselung'
elif int(temp) == 4:
    cd.WP.Warmwasserkreis.Betriebsdaten.Statustext = '4: Zwangsladung'
elif int(temp) == 5:
    cd.WP.Warmwasserkreis.Betriebsdaten.Statustext = '5: Störung'
elif int(temp) == 6:
    cd.WP.Warmwasserkreis.Betriebsdaten.Statustext = '6: WW Entnahme aktiv'
elif int(temp) == 7:
    cd.WP.Warmwasserkreis.Betriebsdaten.Statustext = '7: Warnung'
else:
    cd.WP.Warmwasserkreis.Betriebsdaten.Statustext = temp

cd.WP.Zusatzheizung.Betriebsdaten.Betriebsstunden = web2com_values('/1/2/2/126/4')
cd.WP.Zusatzheizung.Betriebsdaten.HeizenergieMWh = web2com_values('/1/2/2/126/6')
cd.WP.Zusatzheizung.Betriebsdaten.HeizenergiekWh = web2com_values('/1/2/2/126/5')
cd.WP.Zusatzheizung.Betriebsdaten.IstTempVWV = web2com_values('/1/2/2/126/1')
cd.WP.Zusatzheizung.Betriebsdaten.Schaltzyklen = web2com_values('/1/2/2/126/3')
cd.WP.Zusatzheizung.Betriebsdaten.VorlauftempSollwertAnforderung = web2com_values('/1/2/2/126/2')

temp = web2com_values('/1/2/2/126/0')
cd.WP.Zusatzheizung.Betriebsdaten.StatusWaermeerzeuger = temp

if int(temp) == 0:
    cd.WP.Zusatzheizung.Betriebsdaten.Statustext = '0: Abgeschalten'
elif int(temp) == 1:
    cd.WP.Zusatzheizung.Betriebsdaten.Statustext = '1: Heizbetrieb'
elif int(temp) == 2:
    cd.WP.Zusatzheizung.Betriebsdaten.Statustext = '2: Vorlaufzeit Heizbetrieb'
elif int(temp) == 3:
    cd.WP.Zusatzheizung.Betriebsdaten.Statustext = '3: Extern gesperrt'
elif int(temp) == 4:
    cd.WP.Zusatzheizung.Betriebsdaten.Statustext = '4: Kühlbetrieb'
elif int(temp) == 5:
    cd.WP.Zusatzheizung.Betriebsdaten.Statustext = '5: Vorlaufzeit Kühlbetrieb'
elif int(temp) == 6:
    cd.WP.Zusatzheizung.Betriebsdaten.Statustext = '6: Vorlaufzeit Abtaubetrieb'
elif int(temp) == 7:
    cd.WP.Zusatzheizung.Betriebsdaten.Statustext = '7: Abtaubetrieb'
elif int(temp) == 8:
    cd.WP.Zusatzheizung.Betriebsdaten.Statustext = '8: Störung'
elif int(temp) == 9:
    cd.WP.Zusatzheizung.Betriebsdaten.Statustext = '9: Abtropfen'
elif int(temp) == 10:
    cd.WP.Zusatzheizung.Betriebsdaten.Statustext = '10: Abtausperrzeit'
elif int(temp) == 11:
    cd.WP.Zusatzheizung.Betriebsdaten.Statustext = '11: Abtau Vorheizung'
elif int(temp) == 12:
    cd.WP.Zusatzheizung.Betriebsdaten.Statustext = '12: Abtauen 1'
elif int(temp) == 13:
    cd.WP.Zusatzheizung.Betriebsdaten.Statustext = '13: Abtauen 2'
elif int(temp) == 14:
    cd.WP.Zusatzheizung.Betriebsdaten.Statustext = '14: Abtauen 3'
elif int(temp) == 15:
    cd.WP.Zusatzheizung.Betriebsdaten.Statustext = '15: Alarm'
elif int(temp) == 16:
    cd.WP.Zusatzheizung.Betriebsdaten.Statustext = '16: Störung'
elif int(temp) == 17:
    cd.WP.Zusatzheizung.Betriebsdaten.Statustext = '17: Blockiert'
elif int(temp) == 18:
    cd.WP.Zusatzheizung.Betriebsdaten.Statustext = '18: Vorglühen'
elif int(temp) == 19:
    cd.WP.Zusatzheizung.Betriebsdaten.Statustext = '19: Eindüsung Ein'
elif int(temp) == 20:
    cd.WP.Zusatzheizung.Betriebsdaten.Statustext = '20: Eindüsung Aus'
elif int(temp) == 21:
    cd.WP.Zusatzheizung.Betriebsdaten.Statustext = '21: TWVmax Abschaltung'
elif int(temp) == 22:
    cd.WP.Zusatzheizung.Betriebsdaten.Statustext = '22: TWVsoll Abschaltung'
elif int(temp) == 23:
    cd.WP.Zusatzheizung.Betriebsdaten.Statustext = '23: TWEmax Abschaltung'
elif int(temp) == 24:
    cd.WP.Zusatzheizung.Betriebsdaten.Statustext = '24: TWAmin Abschaltung'
elif int(temp) == 25:
    cd.WP.Zusatzheizung.Betriebsdaten.Statustext = '25: TKAmin Abschaltung'
elif int(temp) == 26:
    cd.WP.Zusatzheizung.Betriebsdaten.Statustext = '26: Bivalenzabschaltung'
elif int(temp) == 27:
    cd.WP.Zusatzheizung.Betriebsdaten.Statustext = '27: Warmwasser Ladesperre'
elif int(temp) == 28:
    cd.WP.Zusatzheizung.Betriebsdaten.Statustext = '28: Minimale Auszeit'
elif int(temp) == 29:
    cd.WP.Zusatzheizung.Betriebsdaten.Statustext = '29: Minimale Einzeit'
elif int(temp) == 30:
    cd.WP.Zusatzheizung.Betriebsdaten.Statustext = '30: Anheizen'
elif int(temp) == 31:
    cd.WP.Zusatzheizung.Betriebsdaten.Statustext = '31: Ausbrand'
elif int(temp) == 32:
    cd.WP.Zusatzheizung.Betriebsdaten.Statustext = '32: Pumpen-Nachlauf'
elif int(temp) == 33:
    cd.WP.Zusatzheizung.Betriebsdaten.Statustext = '33: Verzögerung Folge-WE'
elif int(temp) == 34:
    cd.WP.Zusatzheizung.Betriebsdaten.Statustext = '34: Betrieb Uebertemperatur'
elif int(temp) == 35:
    cd.WP.Zusatzheizung.Betriebsdaten.Statustext = '35: Fülltüre geöffnet'
elif int(temp) == 36:
    cd.WP.Zusatzheizung.Betriebsdaten.Statustext = '36: Passivkühlung'
elif int(temp) == 37:
    cd.WP.Zusatzheizung.Betriebsdaten.Statustext = '37: Heizbetrieb angefordert'
elif int(temp) == 38:
    cd.WP.Zusatzheizung.Betriebsdaten.Statustext = '38: Kühlbetrieb angefordert'
else:
    cd.WP.Zusatzheizung.Betriebsdaten.Statustext = temp


