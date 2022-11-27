# Mortgage Calculator: version 4.0
all_location = {'Центральный': 10.05, 'Северо-Западный': 8.6, 'Южный': 9.2, 'Приволжский': 9.5, 'Уральский': 8.8,
                'Сибирский': 7.25, 'Дальневосточный': 2.0}
location = input('Введите локацию из перечня:\n- Центральный\n- Северо-Западный\n- Южный\n- Приволжский'
                 '\n- Уральский\n- Сибирский\n- Дальневосточный\n')
if location == 'Дальневосточный':
    mortgage_final = all_location[location]
else:
    child_amount = input('Количество детей: ')
    salary_project = input('Зарплатный проект: ')
    insurance = input('Доп. страхование: ')
    mortgage_final = all_location[location.title()]
    if int(child_amount) >= 3:
        mortgage_final -= 1
    if salary_project.lower() == 'да':
        mortgage_final -= 0.5
    if insurance.lower() == 'да':
        mortgage_final -= 1.5
print(f'Ипотечная ставка составляет: {round(mortgage_final, 2)} %')
