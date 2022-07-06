def delete_nth(order,max_e):
	one_list = order
	two_list = []
	for element in one_list:
		if two_list.count(element) < max_e:
			two_list.append(element)



	return two_list

a = delete_nth([1, 1, 1, 2, 3, 3, 4], 2)
print(a)