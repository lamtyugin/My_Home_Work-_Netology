user_name = input('Введите Ваше имя: ')
user_name = user_name.title()
date = int(input('Введите день рождения: '))
month = int(input('Введите месяц рождения: '))
year = int(input('Введите год рождения: '))

if (date >= 21 and date <=31 and month == 3) or (month == 4 and date >= 1 and date <= 19):
	zodiac_sign = 'Овен'
elif (date >= 20 and date <= 30 and month == 4) or (month == 5 and date >= 1 and date <= 20):
	zodiac_sign = 'Телец'
elif (date >= 21 and date <= 31 and month == 5) or (month == 6 and date >= 1 and date <= 21):
	zodiac_sign = 'Близнецы'
elif (date >= 22 and date <= 30 and month == 6) or (month == 7 and date >= 1 and date <= 22):
	zodiac_sign = 'Рак'
elif (date >= 23 and date <=31 and month ==7 ) or (month == 8 and date >= 1 and date <= 22):
	zodiac_sign = 'Лев'
elif (date >= 23 and date <= 31 and month == 8) or (month == 9 and date >= 1 and date <= 22):
	zodiac_sign = 'Дева'
elif (date >= 23 and date <= 30 and month == 9) or (month == 10 and date >= 1 and date <= 23):
	zodiac_sign = 'Весы'
elif (date >= 24 and date <= 31 and month == 10) or (month == 11 and date >= 1 and date <= 22):
	zodiac_sign = 'Скорпион'
elif (date >= 23 and date <= 30 and month == 11) or (month == 12 and date >= 1 and date <= 21):
	zodiac_sign = 'Стрелец'
elif (date >= 22 and date <= 31 and month == 12) or (month == 1 and date >= 1 and date <= 20):
	zodiac_sign = 'Козерог'
elif (date >= 21 and date <= 31 and month == 1) or ( month == 2 and date >= 1 and date <= 18):
	zodiac_sign = 'Водолей'
elif (date >= 19 and date <= 29 and month == 2) or (month == 3 and date >= 1 and date <= 20):
	zodiac_sign = 'Рыбы'

if month == 1:
	month_birth = 'Январе'
elif month == 2:
	month_birth = 'Феврале'
elif month == 3:
	month_birth = 'Марте'
elif month == 4:
	month_birth = 'Апреле'
elif month == 5:
	month_birth = 'Мае'
elif month == 6:
	month_birth = 'Июне'
elif month == 7:
	month_birth = 'Июлие'
elif month == 8:
	month_birth = 'Августе'
elif month == 9:
	month_birth = 'Сентябре'
elif month == 10:
	month_birth = 'Октябре'
elif month == 11:
	month_birth = 'Ноябре'
else:
	month_birth = 'Декабре'
	
if (year - 2000) % 12 == 0:
    sign = 'год Дракона'
elif (year - 2000) % 12 == 1:
    sign = 'год Змеи'
elif (year - 2000) % 12 == 2:
    sign = 'год Лошади'
elif (year - 2000) % 12 == 3:
    sign = 'год Овцы'
elif (year - 2000) % 12 == 4:
    sign = 'год Обезьяны'
elif (year - 2000) % 12 == 5:
    sign = 'год Петуха'
elif (year - 2000) % 12 == 6:
    sign = 'год Собаки'
elif (year - 2000) % 12 == 7:
    sign = 'год Свиньи'
elif (year - 2000) % 12 == 8:
    sign = 'год Крысы'
elif (year - 2000) % 12 == 9:
    sign = 'год Быка'
elif (year - 2000) % 12 == 10:
    sign = 'год Тигра'
else:
    sign = 'год Зайца'

print(f'\n{user_name}, Вы родились в {month_birth}, в {sign}.\nВаш знак задиака - {zodiac_sign}')
