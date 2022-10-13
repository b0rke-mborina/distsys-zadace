def listAndDict(listArg, dictArg):
	if not isinstance(listArg, list) or not isinstance(dictArg, dict): raise Exception()
	if not (len(listArg)==len(dictArg) and all(isinstance(item, int) for item in listArg)): raise Exception()
	return {dictItem:listItem if 5<=listItem<=10 else -1 for listItem,dictItem in zip(listArg, dictArg)}

print(listAndDict([8, 7, 1], {1: 2, 2: 1, 3: 2}))
print(listAndDict([8, 7, 9], {1: 2, 2: 1, 3: 2}))
print(listAndDict([3, 2, 1], {1: 2, 2: 1, 3: 2}))
print(listAndDict([3, 2, 1], [1, 2, 3]))
print(listAndDict({3: 1, 2: 1, 1: 1}, {1: 2, 2: 1, 3: 2}))
print(listAndDict((3, 2, 1), (2, 1, 2)))
print(listAndDict([2, 1], {1: 2, 2: 1, 3: 2}))
print(listAndDict([3, "2", 1], {1: 2, 2: 1, 3: 2}))
