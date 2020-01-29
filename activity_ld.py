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
    
def find_in_activities(activity):
    for dict in type_of_activity:
        if dict.get('activity')==activity:
            print('Рекомендуемое время мероприятия {}'.format(activity))
            return dict.get("time")
    print('Укажите необходимое время ч:м:с планируемого мероприятия {}'.format(activity))
    time = input()
activity = input()
print(find_in_activities(activity))

type_of_activity.append({'activity': activity ,'time': time})
print(type_of_activity)