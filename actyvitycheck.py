type_of_activity = { 
    'спорт': 2,
    'прогулка': 1,
    'дорога до работы': 1.1,
    'домашние дела': 1.3,  
    'приготовление пищи': 1.3,
    'кодинг': 2,
    'пробежка': 1.3,
}

user_say = input('Какие планы: ')

if (bool(user_say)) in type_of_activity is False:
    print('Укажите необходимое время планируемого мероприятия {}'.format(user_say))
    type_of_activity.append(user_say)
else:
    print(f'Рекомендуемое время: {(type_of_activity.get(user_say))}')

    


