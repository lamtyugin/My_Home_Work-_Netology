boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard']
girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']

if len(boys) == len(girls):
    print('Найдены идеальные пары:\n')
    boys.sort()
    girls.sort()
    for boys_, girls_ in zip(boys, girls):
        print(f'{boys_} и {girls_}')
else:
    print('Кто-то может остаться без пары.')
