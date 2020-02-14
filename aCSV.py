import csv
from datetime import datetime

dt_now = datetime.now()
time = datetime.strftime(dt_now, '%d/%m/%y %H:%M:%S.%f')

type_of_activity = [
    {'activity': 'спорт', 'time': '2:00:00'},
    {'activity': 'прогулка', 'time': '1:00:00'},
    {'activity': 'дорога до работы', 'time': '1:10:00'},
    {'activity': 'домашние дела', 'time': '1:30:00'},  
    {'activity': 'приготовление еды', 'time': '1:30:00'},
    {'activity': 'кодинг', 'time': '2:00:00'},
    {'activity': 'пробежка', 'time': '1:30:00'},
]

with open('project.csv', 'w', encoding='utf-8') as project:
    fields = ['activity', 'time']
    writer = csv.DictWriter(project, fields, delimiter=';')
    writer.writeheader()
    for activity in type_of_activity:
        writer.writerow(activity)
