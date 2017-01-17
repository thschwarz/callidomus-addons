from datetime import date,timedelta
import sys
import caldav
from caldav.davclient import DAVClient
from caldav.elements import dav, cdav

# Caldav url
url = "p53-caldav.icloud.com"
username = "xxxx@xxx.xxx"
password = "xxxx"
calendar_names = ["Müll","Family","Privat"]
final_url = "https://"+username+":"+password+"@"+url

client = caldav.DAVClient(final_url)
principal = client.principal()
calendars = principal.calendars()

caldata_today = []
caldata_tomorrow = []

if len(calendars) > 0:
    for i in range(0, len(calendars)-1):
        calendar_displayname = str(calendars[i].get_properties([dav.DisplayName(),]))
        #print(calendar_displayname)
        for calendar_name in calendar_names:
            if calendar_displayname.find(calendar_name) > 0:         
                calendar = calendars[i]
                html_today = '<table>'
                html_tomorrow = '<table>'
                searchdate = date.today()
                #print("Termine heute:",date(searchdate.year, searchdate.month, searchdate.day))
                results = calendar.date_search(date(searchdate.year, searchdate.month, searchdate.day),date(searchdate.year, searchdate.month, searchdate.day+1))
                for event in results:
                    ev = event
                    ev.load()
                    evb = ev.data[ev.data.find('SUMMARY:'):]
                    text = evb[8:evb.find(chr(10))-1]
                    summary = text.encode('latin1').decode('utf8')
                    evb = ev.data[ev.data.find('DTSTART;'):]
                    evb = evb[evb.find(':'):]
                    text = evb[1:evb.find(chr(10))-1]
                    time_start = text[9:11]+':'+text[11:13]                
                    evb = ev.data[ev.data.find('DTEND;'):]
                    evb = evb[evb.find(':'):]
                    text = evb[1:evb.find(chr(10))-1]
                    time_end = text[9:11]+':'+text[11:13]             
                    #print(time_start,'-',time_end,summary)
                    caldata_today.append([time_start,time_end,summary,calendar_name])

                searchdate = date.today() + timedelta(days=1)
                #print("Termine morgen:",date(searchdate.year, searchdate.month, searchdate.day))
                results = calendar.date_search(date(searchdate.year, searchdate.month, searchdate.day),date(searchdate.year, searchdate.month, searchdate.day+1))
                for event in results:
                    ev = event
                    ev.load()
                    evb = ev.data[ev.data.find('SUMMARY:'):]
                    text = evb[8:evb.find(chr(10))-1]
                    summary = text.encode('latin1').decode('utf8')
                    evb = ev.data[ev.data.find('DTSTART;'):]
                    evb = evb[evb.find(':'):]
                    text = evb[1:evb.find(chr(10))-1]
                    time_start = text[9:11]+':'+text[11:13]                
                    evb = ev.data[ev.data.find('DTEND;'):]
                    evb = evb[evb.find(':'):]
                    text = evb[1:evb.find(chr(10))-1]
                    time_end = text[9:11]+':'+text[11:13]             
                    #print(time_start,'-',time_end,summary)
                    caldata_tomorrow.append([time_start,time_end,summary,calendar_name])

    #print('-today--------------')
    if len(caldata_today) > 0:
        caldata_today.sort()
        html_today='<table>'
        for i in range(0,len(caldata_today)):
            html_today=html_today+'<tr><td  width=3 bgcolor="#FF0000"></td><td>'+caldata_today[i][0]+'<br>'+caldata_today[i][1]+'</td><td>'+caldata_today[i][2]+'</td></tr>'
        html_today=html_today+'</table>'
        print(html_today)

    #print('-tomorrow--------------')                
    if len(caldata_tomorrow) > 0:
        caldata_tomorrow.sort()
        html_tomorrow='<table>'
        for i in range(0,len(caldata_tomorrow)):
            html_tomorrow=html_tomorrow+'<tr><td  width=3 bgcolor="#FF0000"></td><td>'+caldata_tomorrow[i][0]+'<br>'+caldata_tomorrow[i][1]+'</td><td>'+caldata_tomorrow[i][2]+'</td></tr>'
        html_tomorrow=html_tomorrow+'</table>'
        print(html_tomorrow)
