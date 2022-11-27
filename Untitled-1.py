ids = {'user1': [213, 213, 213, 15, 213],
       'user2': [54, 54, 119, 119, 119],
       'user3': [213, 98, 98, 35]}

lst = ids.values()
my_list = []
for i in lst:
	for j in i:
		my_list.append(j)
print(list(set(my_list)), '\n') 

new_list = []
for i in my_list:
	if i not in new_list:
		new_list.append(i)
print(new_list)
