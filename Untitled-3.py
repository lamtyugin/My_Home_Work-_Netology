stats = {'facebook': 55, 'yandex': 120, 'vk': 115, 'google': 99, 'mail': 42, 'ok': 98}
max_sales = ''
for sales in stats.keys():
	if stats[sales] > stats.get(max_sales, 0):
		max_sales = sales

print(max_sales)