boys = ['Artem', 'Nikita', 'Oleg', 'Danila', 'Alexander', 'Roman']
girls = ['Kate', 'Liza', 'Kira', 'Amalia', 'Daria', 'Liubov', 'Karina']
if len(boys) == len(girls):
	print('Возможно, идеальные пары: ')
	boys.sort()
	girls.sort()
	dating = zip(boys, girls)
	for company in dating:
		print(f'{company[0]} и {company[1]}')
else:
	print('Кто то может остаться без пары')
