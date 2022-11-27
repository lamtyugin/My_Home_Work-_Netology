list_ = ['2018-01-01', 'yandex', 'cpc', 100]
dict_ = {list_[-2]: list_[-1]}
for i in list_[:-2][::-1]:
	dict_ = {i: dict_}
print(dict_)