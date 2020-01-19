type_of_activity = [ 
    {'type': 'sport', 'time': 2},
    {'type': 'walking', 'time': 1},
    {'type': 'ride to work', 'time': 1.1},
    {'type': 'homework', 'time': 1.3},  
    {'type': 'cooking', 'time': 1.3},
    {'type': 'coding', 'time': 2},
]

activity=(input ("What`s your plan? "))
if activity == type_of_activity:
        print(f'Рекомендуемое время: {(type_of_activity.get(type_of_activity_type["time"]))}')

if type_of_activity.get == 0:
        print('Укажите необходимое время!')
        
