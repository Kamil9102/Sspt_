import csv

type_of_activity = { 
    'спорт': 2,
    'прогулка': 1,
    'дорога до работы': 1.1,
    'домашние дела': 1.3,  
    'приготовление еды': 1.3,
    'кодинг': 2,
    'пробежка': 1.3,
}

with open('project.csv', 'w', encoding='utf-8') as project:
    fields = ['actyvity', 'time']
    writer = csv.DictWriter(project, fields, delimiter=';')
    writer.writeheader()
    for actyvity in type_of_activity:
        writer.writerow(f'(type_of_activity[actyvity])')