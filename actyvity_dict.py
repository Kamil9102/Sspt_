type_of_activity = { 
    'sport': 2,
    'walking': 1,
    'ride to work': 1.1,
    'homework': 1.3,  
    'cooking': 1.3,
    'coding': 2,
    'jogging': 1.3,
}

print(f'Рекомендуемое время: {(type_of_activity.get("art", 0))}')

if type_of_activity.get == ('Рекомендуемое время: 0'):
    print('Укажите необходимое время.')

