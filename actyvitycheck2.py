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

while True:
    user_say = input('Какие планы: ')

    if  user_say == type_of_activity_activity.get('activity'):
        print(f'Рекомендуемое время: {(type_of_activity(user_say))}')
        break 
    else:
        print('Укажите необходимое время ч:м:с планируемого мероприятия {}'.format(user_say))
        time = input()
        type_of_activity.append({user_say: time})
        break
#для проверки
print(type_of_activity)
    


