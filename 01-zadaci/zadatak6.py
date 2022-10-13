def listsOrDicts(param1, param2):
	if type(param1)!=type(param2): raise Exception()
	if not (isinstance(param1, list) or isinstance(param1, dict)): raise Exception()
	if isinstance(param1, list): return param1+param2
	else: return {**param1, **param2}

print(listsOrDicts([1, 2, 1, 2], [3, 2]))
print(listsOrDicts({1: 2, 3: 2}, {5: 2, 4: 1}))
print(listsOrDicts((1, 2, 1, 2), (3, 2)))
print(listsOrDicts({1: 2, 3: 2}, [3, 2]))
print(listsOrDicts((1, 2, 1, 2), [3, 2]))
