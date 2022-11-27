# Mortgage Calculator: version 2.0
location = input('Введите локацию из перечня:\n-Центральный\n-Северо-Западный\n-Южный\n-Приволжский'
                 '\n-Уральский\n-Сибирский\n-Дальневосточный\n')
all_location = [['Центральный', 10.05], ['Северо-Западный', 8.6], ['Южный', 9.2],
                ['Приволжский', 9.5], ['Уральский', 8.8], ['Сибирский', 7.25], ['Дальневосточный', 2.0]]

three_children_in_family = 1
salary_project = 0.5
insurance_in_bank = 1.5

for loc in all_location:
    if location in loc:
        if location != 'Дальневосточный':
            children = input('Три и более детей?\nФормат ответа: ДА/НЕТ\n')
            children = children.upper()
            if children == 'ДА':
                project = input('Зарплатный проект?:\nФормат ответа: ДА/НЕТ\n')
                project = project.upper()
                if project == 'ДА':
                    insurance = input('Добровольное страхование?\nФормат ответа: ДА/НЕТ:\n')
                    insurance = insurance.upper()
                    if insurance == 'ДА':
                        print(float(*loc[1:]) - three_children_in_family - salary_project - insurance_in_bank)
                elif project == 'НЕТ':
                    insurance = input('Добровольное страхование?\nФормат ответа: ДА/НЕТ:\n')
                    insurance = insurance.upper()
                    if insurance == 'ДА':
                        print(float(*loc[1:]) - three_children_in_family - salary_project)
                    elif insurance == 'НЕТ':
                        print(float(*loc[1:]) - three_children_in_family)
                    else:
                        print('Формат ввода: ДА/НЕТ')
                else:
                    print('Формат ввода: ДА/НЕТ')
            elif children == 'НЕТ':
                project = input('Зарплатный проект?:\nФормат ответа: ДА/НЕТ\n')
                project = project.upper()
                if project == 'ДА':
                    insurance = input('Добровольное страхование?\nФормат ответа: ДА/НЕТ:\n')
                    insurance = insurance.upper()
                    if insurance == 'ДА':
                        print(float(*loc[1:]) - salary_project - insurance_in_bank)
                    elif insurance == 'НЕТ':
                        print(float(*loc[1:]) - salary_project)
                    else:
                        print('Формат ввода: ДА/НЕТ')
                elif project == 'НЕТ':
                    insurance = input('Добровольное страхование?\nФормат ответа: ДА/НЕТ:\n')
                    insurance = insurance.upper()
                    if insurance == 'ДА':
                        print(float(*loc[1:]) - insurance_in_bank)
                    elif insurance == 'НЕТ':
                        print(float(*loc[1:]))
                else:
                    print('Формат не соответствует условию ввода: ДА/НЕТ')
            else:
                print('Формат не соответствует условию ввода: ДА/НЕТ')
        else:
            print(*loc[1:])
