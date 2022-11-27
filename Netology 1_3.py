# Mortgage Calculator: version 3.0
location = input('Введите локацию из перечня:\n-Центральный\n-Северо-Западный\n-Южный\n-Приволжский'
                 '\n-Уральский\n-Сибирский\n-Дальневосточный\n')

central = 10.05
northwest = 8.6
south = 9.2
volga = 9.5
ural = 8.8
siberian = 7.25
far_Eastern = 2.0

if location == 'Центральный':
    mortgage_final = central
    child_amount = int(input('Введите количество детей: '))
    if child_amount >= 3:
        mortgage_final -= 1
    salary_project = input('Участник зарплатного проекта: ')
    if salary_project.lower() == 'да':
        mortgage_final -= 0.5
    insurance = input('Дополнительное страхование: ')
    if insurance.lower() == 'да':
        mortgage_final -= 1.5
elif location == 'Северо-Западный':
    mortgage_final = northwest
    child_amount = int(input('Введите количество детей: '))
    if child_amount >= 3:
        mortgage_final -= 1
    salary_project = input('Участник зарплатного проекта: ')
    if salary_project.lower() == 'да':
        mortgage_final -= 0.5
    insurance = input('Дополнительное страхование: ')
    if insurance.lower() == 'да':
        mortgage_final -= 1.5
elif location == 'Южный':
    mortgage_final = south
    child_amount = int(input('Введите количество детей: '))
    if child_amount >= 3:
        mortgage_final -= 1
    salary_project = input('Участник зарплатного проекта: ')
    if salary_project.lower() == 'да':
        mortgage_final -= 0.5
    insurance = input('Дополнительное страхование: ')
    if insurance.lower() == 'да':
        mortgage_final -= 1.5
elif location == 'Приволжский':
    mortgage_final = volga
    child_amount = int(input('Введите количество детей: '))
    if child_amount >= 3:
        mortgage_final -= 1
    salary_project = input('Участник зарплатного проекта: ')
    if salary_project.lower() == 'да':
        mortgage_final -= 0.5
    insurance = input('Дополнительное страхование: ')
    if insurance.lower() == 'да':
        mortgage_final -= 1.5
elif location == 'Уральский':
    mortgage_final = ural
    child_amount = int(input('Введите количество детей: '))
    if child_amount >= 3:
        mortgage_final -= 1
    salary_project = input('Участник зарплатного проекта: ')
    if salary_project.lower() == 'да':
        mortgage_final -= 0.5
    insurance = input('Дополнительное страхование: ')
    if insurance.lower() == 'да':
        mortgage_final -= 1.5
elif location == 'Сибирский':
    mortgage_final = siberian
    child_amount = int(input('Введите количество детей: '))
    if child_amount >= 3:
        mortgage_final -= 1
    salary_project = input('Участник зарплатного проекта: ')
    if salary_project.lower() == 'да':
        mortgage_final -= 0.5
    insurance = input('Дополнительное страхование: ')
    if insurance.lower() == 'да':
        mortgage_final -= 1.5
else:
    mortgage_final = far_Eastern
print(f'Ипотечная ставка составляет: {mortgage_final} %')
