type_of_activity = { 
    'спорт': 2,
    'прогулка': 1,
    'дорога до работы': 1.1,
    'домашние дела': 1.3,  
    'приготовление пищи': 1.3,
    'кодинг': 2,
    'пробежка': 1.3,
}

while True:
    user_say = input('Какие планы: ')
    if user_say == 'спорт':
        print(f'Рекомендуемое время мероприятия: {(type_of_activity(user_say), 0)}')
        break
    else:
        print('Укажите необходимое время планируемого мероприятия {}'.format(user_say))