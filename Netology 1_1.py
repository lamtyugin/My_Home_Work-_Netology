# Mortgage Calculator: version 1.0
base_rate_Moscow = 10.25
base_rate_St_Petersburg = 9.95
base_rate_South = 8.99
base_rate_Privolzhsky = 10.05
base_rate_Far_East = 2

three_children_in_family = 1
salary_project = 0.5
insurance_in_bank = 1.5

question_about_place = '\nВыберете регион,\nв котором планируете преобретать недвижимость?\nФормат ответ: ДА/НЕТ\n\n'
question_about_children = ', государственная программа ипотечного кредитования' \
                          '\nдополнительно снижает ставку для многодетных семей.' \
                          '\nМногодетными являются те семьи в которых три и более ребенка" ' \
                          '\nВаша семья подходит под программу ?' \
                          '\nФормат ответа: ДА/НЕТ'
question_about_salary = ', Вы подключены к зарплатному проекту?\nФормат ответа: ДА/НЕТ'
question_about_insurance = ', Вы готовы дополнительно оформить\nстрахование ипотечного кредита?\nФормат ответа: ДА/НЕТ'

mortgage_rate_response = '!\nВаша процентная ставка,\nна преобретение жилья с использованием \nипотечного займа ' \
                         '\nсоставляет:'

while True:
    user_name = input(f'\nЗдравствуйте 👋\nДавайте с начала познакомимся !!!'
                      f'\nЯ - Ипотечный калкулятор,\nсозданый для удобства расчетов. 🤝'
                      f'\nКак я могу к Вам обрашаться?\n\nВведите имя: \n')
    user_name = user_name.title()
    if user_name.isalpha():
        print(f'Приятно познакомится, {user_name}! 🥳')
    else:
        print(f'\nВижу, Вы решили сохранить анномносить,\nНу вот! {user_name}, '
              f'а я хотел подзароботать на данных.\nЛадно, погнали!!! 🥲\n')
    last_name = input(f'Введите Вашу фамилию: \n')
    last_name = last_name.title()
    if last_name.isalpha():
        print(f'\n{last_name} {user_name}, у Вас прекрасная фамилия! 🎉')
    else:
        print(f'\nНе прокатило!\nПочему? {last_name}, '
              f'и пин-код, наверное не скажешь?\nЛадно, пошутили и хвать, погнали!!! 🥲\n')

    while True:
        region = input(f'{question_about_place}Москва и МО? -> ')
        region = region.upper()
        if region == 'ДА':
            children = input(f'\n{user_name}{question_about_children}\n-> ')
            children = children.upper()
            if children == 'ДА':
                project = input(f'\n{user_name}{question_about_salary}\n-> ')
                project = project.upper()
                if project == 'ДА':
                    insurance = input(f'\n{user_name}{question_about_insurance}\n-> ')
                    insurance = insurance.upper()
                    if insurance == 'ДА':
                        print(f'\nУважаемый"ая" {user_name}{mortgage_rate_response}', base_rate_Moscow
                              - three_children_in_family - salary_project - insurance_in_bank, '%')
                        break
                    else:
                        print(f'\nУважаемый"ая"{user_name}{mortgage_rate_response}', base_rate_Moscow -
                              three_children_in_family - salary_project, '%')
                else:
                    insurance = input(f'\n{user_name}{question_about_insurance}\n-> ')
                    insurance = insurance.upper()
                    if insurance == 'ДА':
                        print(f'\nУважаемый"ая" {user_name}{mortgage_rate_response}', base_rate_Moscow -
                              three_children_in_family - insurance_in_bank, '%')
                    else:
                        print(f'\nУважаемый"ая" {user_name}{mortgage_rate_response}', base_rate_Moscow -
                              three_children_in_family, '%')
            else:
                project = input(f'\n{user_name}{question_about_salary}\n-> ')
                project = project.upper()
                if project == 'ДА':
                    insurance = input(f'\n{user_name}{question_about_insurance}\n-> ')
                    insurance = insurance.upper()
                    if insurance == 'ДА':
                        print(f'\nУважаемый"ая" {user_name}{mortgage_rate_response}', base_rate_Moscow -
                              salary_project - insurance_in_bank, '%')
                    else:
                        print(f'\nУважаемый"ая" {user_name}{mortgage_rate_response}', base_rate_Moscow -
                              salary_project, '%')
                else:
                    insurance = input(f'\n{user_name}{question_about_insurance}\n-> ')
                    insurance = insurance.upper()
                    if insurance == 'ДА':
                        print(f'\nУважаемый"ая" {user_name}{mortgage_rate_response}', base_rate_Moscow -
                              insurance_in_bank, '%')
                    else:
                        print(f'\nУважаемый"ая" {user_name}{mortgage_rate_response}', base_rate_Moscow, '%')
            break
        region = input(f'{question_about_place}Санкт-Петербург и Ленинградская область? -> ')
        region = region.upper()
        if region == 'ДА':
            children = input(f'\n{user_name}{question_about_children}\n-> ')
            children = children.upper()
            if children == 'ДА':
                project = input(f'\n{user_name}{question_about_salary}\n-> ')
                project = project.upper()
                if project == 'ДА':
                    insurance = input(f'\n{user_name}{question_about_insurance}\n-> ')
                    insurance = insurance.upper()
                    if insurance == 'ДА':
                        print( f'\nУважаемый"ая" {user_name}{mortgage_rate_response}', base_rate_St_Petersburg -
                               three_children_in_family - salary_project -
                               insurance_in_bank, '%')
                    else:
                        print( f'\nУважаемый"ая" {user_name}{mortgage_rate_response}', base_rate_St_Petersburg -
                               three_children_in_family - salary_project, '%')
                else:
                    insurance = input(f'\n{user_name}{question_about_insurance}\n-> ')
                    insurance = insurance.upper()
                    if insurance == 'ДА':
                        print( f'\nУважаемый"ая" {user_name}{mortgage_rate_response}', base_rate_St_Petersburg -
                               three_children_in_family - insurance_in_bank, '%')
                    else:
                        print(f'\nУважаемый"ая" {user_name}{mortgage_rate_response}', base_rate_St_Petersburg -
                              three_children_in_family, '%')
            else:
                project = input(f'\n{user_name}{question_about_salary}\n-> ')
                project = project.upper()
                if project == 'ДА':
                    insurance = input(f'\n{user_name}{question_about_insurance}\n-> ')
                    insurance = insurance.upper()
                    if insurance == 'ДА':
                        print( f'\nУважаемый"ая" {user_name}{mortgage_rate_response}', base_rate_St_Petersburg -
                               salary_project - insurance_in_bank, '%')
                    else:
                        print( f'\nУважаемый"ая"{user_name}{mortgage_rate_response}', base_rate_St_Petersburg -
                               salary_project, '%')
                else:
                    insurance = input(f'\n{user_name}{question_about_insurance}\n-> ')
                    insurance = insurance.upper()
                    if insurance == 'ДА':
                        print( f'\nУважаемый"ая" {user_name}{mortgage_rate_response}', base_rate_St_Petersburg -
                               insurance_in_bank, '%')
                    else:
                        print( f'\nУважаемый"ая" {user_name}{mortgage_rate_response}', base_rate_St_Petersburg, '%')
            break
        region = input(f'{question_about_place}Дальневосточный федеральный округ? -> ')
        region = region.upper()
        if region == 'ДА':
            print(f'\nУважаемый"ая" {user_name}{mortgage_rate_response}', base_rate_Far_East, '%')
            break
        region = input(f'{question_about_place}Южный федеральный округ? -> ')
        region = region.upper()
        if region == 'ДА':
            children = input(f'\n{user_name}{question_about_children}\n-> ')
            children = children.upper()
            if children == 'ДА':
                project = input(f'\n{user_name}{question_about_salary}\n-> ')
                project = project.upper()
                if project == 'ДА':
                    insurance = input(f'\n{user_name}{question_about_insurance}\n-> ')
                    insurance = insurance.upper()
                    if insurance == 'ДА':
                        print( f'\nУважаемый"ая" {user_name}{mortgage_rate_response}', base_rate_South -
                               three_children_in_family - salary_project - insurance_in_bank, '%')
                    else:
                        print( f'\nУважаемый"ая" {user_name}{mortgage_rate_response}', base_rate_South -
                               three_children_in_family - salary_project, '%')
                else:
                    insurance = input(f'\n{user_name}{question_about_insurance}\n-> ')
                    insurance = insurance.upper()
                    if insurance == 'ДА':
                        print( f'\nУважаемый"ая" {user_name}{mortgage_rate_response}', base_rate_South -
                               three_children_in_family - insurance_in_bank, '%')
                    else:
                        print(f'\nУважаемый"ая" {user_name}{mortgage_rate_response}', base_rate_South -
                              three_children_in_family, '%')
            else:
                project = input(f'\n{user_name},{question_about_salary}\n-> ')
                project = project.upper()
                if project == 'ДА':
                    insurance = input(f'\n{user_name}{question_about_insurance}\n-> ')
                    insurance = insurance.upper()
                    if insurance == 'ДА':
                        print( f'\nУважаемый"ая" {user_name}{mortgage_rate_response}', base_rate_South -
                               salary_project - insurance_in_bank, '%')
                    else:
                        print( f'\nУважаемый"ая" {user_name}{mortgage_rate_response}', base_rate_South -
                               salary_project, '%')
                else:
                    insurance = input(f'\n{user_name}{question_about_insurance}\n-> ')
                    insurance = insurance.upper()
                    if insurance == 'ДА':
                        print( f'\nУважаемый"ая" {user_name}{mortgage_rate_response}', base_rate_South -
                               insurance_in_bank, '%')
                    else:
                        print( f'\nУважаемый"ая" {user_name}{mortgage_rate_response}', base_rate_South, '%')
            break
        region = input(f'{question_about_place}Приволжский федеральный округ? -> ')
        region = region.upper()
        if region == 'ДА':
            children = input(f'\n{user_name}{question_about_children}\n-> ')
            children = children.upper()
            if children == 'ДА':
                project = input(f'\n{user_name}{question_about_salary}\n-> ')
                project = project.upper()
                if project == 'ДА':
                    insurance = input(f'\n{user_name}{question_about_insurance}\n-> ')
                    insurance = insurance.upper()
                    if insurance == 'ДА':
                        print( f'\nУважаемый"ая" {user_name}{mortgage_rate_response }', base_rate_Privolzhsky -
                               three_children_in_family - salary_project -
                               insurance_in_bank, '%')
                    else:
                        print( f'\nУважаемый"ая" {user_name}{mortgage_rate_response }', base_rate_Privolzhsky -
                               three_children_in_family -
                               salary_project, '%')
                else:
                    insurance = input(f'\n{user_name}{question_about_insurance}\n-> ')
                    insurance = insurance.upper()
                    if insurance == 'ДА':
                        print( f'\nУважаемый"ая" {user_name}{mortgage_rate_response }', base_rate_Privolzhsky -
                               three_children_in_family - insurance_in_bank, '%')
                    else:
                        print(f'\nУважаемый"ая" {user_name}!{mortgage_rate_response }', base_rate_Privolzhsky -
                              three_children_in_family, '%')
            else:
                project = input(f'\n{user_name}{question_about_salary}\n-> ')
                project = project.upper()
                if project == 'ДА':
                    insurance = input(f'\n{user_name}{question_about_insurance}\n-> ')
                    insurance = insurance.upper()
                    if insurance == 'ДА':
                        print( f'\nУважаемый"ая" {user_name}{mortgage_rate_response }', base_rate_Privolzhsky -
                               salary_project - insurance_in_bank, '%')
                    else:
                        print( f'\nУважаемый"ая" {user_name}{mortgage_rate_response }', base_rate_Privolzhsky -
                               salary_project, '%')
                else:
                    insurance = input(f'\n{user_name}{question_about_insurance}\n-> ')
                    insurance = insurance.upper()
                    if insurance == 'ДА':
                        print( f'\nУважаемый"ая" {user_name}{mortgage_rate_response }', base_rate_Privolzhsky -
                               insurance_in_bank, '%')
                    else:
                        print( f'\nУважаемый"ая"{user_name}{mortgage_rate_response }', base_rate_Privolzhsky, '%')
    break