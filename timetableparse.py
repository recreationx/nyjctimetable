from bs4 import BeautifulSoup
import json
import os.path
import sys
import argparse

parser = argparse.ArgumentParser(description='Process a NYJC timetable.')
parser.add_argument('filename', help='HTML file, in the same directory')
parser.add_argument('outputname', help='Output filename (.json)')
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

        
with open(f'{args.outputname}.json', 'w') as outfile:
    json.dump(day_dict, outfile, indent=4)
print(day_dict)

    

