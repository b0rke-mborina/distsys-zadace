def equalLists(list1, list2):
	if len(list1) != len(list2): raise Exception()
	return [itemFromList1 if itemFromList1==itemFromList2 else -1 for itemFromList1,itemFromList2 in zip(list1, list2)]

print(equalLists([1, 2, 3, 4, 5], [2, 2, 4, 4, 5]))
print(equalLists([5, 4, 3, 2, 1], [5, 4, 3, 2, 1]))
print(equalLists([1, 2, 3, 4, 5], [6, 7, 8, 9, 0]))
print(equalLists([1, 2, 3, 4, 5], [6, 7, 8, 9]))
