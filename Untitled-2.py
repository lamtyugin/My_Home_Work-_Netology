queries = [
    'смотреть сериалы онлайн',
    'новости спорта',
    'афиша кино',
    'курс доллара',
    'сериалы этим летом',
    'курс по питону',
    'сериалы про спорт',
	'амфетамины зло',
	'Моргенштерн торгует наркотиками в соцсетях',
	'как растворить труп в ванной ?',
	'как взломать пентагон на питоне',
	'google',
	'Рик и Морти',
	'VPN',
	'Секс в большом городе смотреть онлайн без смс и регистрации'
    ]

repository = {}

for query in queries:
	words = query.split()

	if len(words) in repository.keys():
		repository[len(words)] += 1
	else:
		repository.update({len(words): 1})
sum_repository = sum(repository.values())
for key, value in repository.items():
	percent = round((value / len(queries)) * 100, 2)
	print(f'Поиск запросов содержащих {key} слова: {percent}% ({value} запр. из {sum_repository} запросов)')