def listsOrDicts(param1, param2):
	assert type(param1) == type(param2), "Parameters are not of the same type."
	assert isinstance(param1, list) or isinstance(param1, dict), "Parameters are not lists or dictionaries."
	if isinstance(param1, list): return param1+param2
	else: return {**param1, **param2}

print(listsOrDicts([1, 2, 1, 2], [3, 2]))
print(listsOrDicts({1: 2, 3: 2}, {5: 2, 4: 1}))
print(listsOrDicts({1: 2, 3: 2}, [3, 2]))
print(listsOrDicts((1, 2, 1, 2), [3, 2]))
print(listsOrDicts((1, 2, 1, 2), (3, 2)))
