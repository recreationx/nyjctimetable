from bs4 import BeautifulSoup
from ics import Calendar, Event
import pytz
import datetime
import json
import os.path
import sys
import argparse


parser = argparse.ArgumentParser(description='Process a NYJC timetable.')
parser.add_argument('filename', help='HTML file, in the same directory')
parser.add_argument('outputname', help='Output filename')
parser.add_argument('--type', help='Output type (ics or json)', default='json')
args = parser.parse_args()

if args.filename.endswith('.html') is False and args.filename.endswith('.htm') is False:
    sys.exit('File given is not a html file!')
elif os.path.isfile(args.filename) is False:
    sys.exit('File does not exist.')
    

with open(args.filename, 'r+') as f:
    contents = f.read()

soup = BeautifulSoup(contents, 'html.parser')

times = [
    '0730-0800',
    '0800-0830',
    '0830-0900',
    '0900-0930',
    '0930-1000',
    '1000-1030',
    '1030-1100',
    '1100-1130',
    '1130-1200',
    '1200-1230',
    '1230-1300',
    '1300-1330',
    '1330-1400',
    '1400-1430',
    '1430-1500',
    '1500-1530',
    '1530-1600',
    '1600-1630',
    '1630-1700',
    '1700-1730',
    '1730-1800'
]
table = soup.findAll('table')[1]
days = table.findAll('tr')
day_dict = dict()
for day in days:
    a = day.findAll('td')
    if a[1].contents[0] != '0730':
        day_name = a[0].contents[0]
        day_list = []
        x = 0
        for c, i in enumerate(a):
            if c != 0:
                if i.contents[0] == u'\xa0':
                    day_list.append({'name': 'No Lesson', 'venue': 'NIL', 'time': times[x]})
                    x += 1
                else:
                    title = str(i.findAll('p')[0].contents[0])
                    venue = str(i.findAll('p')[1].contents[0])
                    if venue == '<br/>':
                        venue = 'NIL'
                    for i in range(int(i['colspan'])):
                        day_list.append({'name': title, "venue": venue, "time": times[x]})
                        x += 1
        day_dict[day_name] = day_list

# sorry for the trash variable naming i was tired
def createcalendar():
    calendar = Calendar()
    timezone = pytz.timezone("Asia/Singapore")
    start_date = str(input("Start date (DD/MM/YYYY): "))
    start_date = timezone.localize(datetime.datetime.strptime(start_date, "%d/%m/%Y"))
    current_date = None
    for c, day in enumerate(day_dict.keys()):
        schedule = day_dict[day]
        events = [i for i in schedule if i['name'] != 'No Lesson']
        events_namelist = [i['name'] for i in events]
        duration = []
        final = []
        for i in events:
            if any(i['name'] == d['name'] for d in final) is False:
                final.append({"name": i['name'], "duration": events_namelist.count(i['name']), "begin": i['time'][0:4], 'venue': i['venue']})
        for i in final:
            e = Event()
            e.name = i['name']
            e.description = i['venue']
            if c <= 4:
                current_date = start_date.replace(hour=int(i['begin'][:2]), minute=int(i['begin'][2:4])) + datetime.timedelta(hours=24*c)
            elif c > 4:
                current_date = start_date.replace(hour=int(i['begin'][:2]), minute=int(i['begin'][2:4])) + datetime.timedelta(hours=24*(c+2))
            e.begin = current_date
            e.end = current_date + datetime.timedelta(minutes=int(i['duration']) * 30)
            calendar.events.add(e)

    with open(f'{args.outputname}.ics', 'w') as f:
        f.writelines(calendar)

if args.type == 'json':      
    with open(f'{args.outputname}.json', 'w') as outfile:
        json.dump(day_dict, outfile, indent=4)
elif args.type == 'ics':
    createcalendar()




    

