def listAndDict(listArg, dictArg):
	assert isinstance(listArg, list) and isinstance(dictArg, dict), "Parameters are not a list and a dictionary respectively."
	assert len(listArg)==len(dictArg), "Parameters are not of equal length."
	assert all(isinstance(item, int) for item in listArg), "Not all list elements are integers."
	return {dictItem:listItem if 5<=listItem<=10 else -1 for listItem,dictItem in zip(listArg, dictArg)}

print(listAndDict([8, 7, 1], {1: 2, 2: 1, 3: 2}))
print(listAndDict([8, 7, 9], {1: 2, 2: 1, 3: 2}))
print(listAndDict([3, 2, 1], {1: 2, 2: 1, 3: 2}))
print(listAndDict([3, 2, 1], [1, 2, 3]))
print(listAndDict({3: 1, 2: 1, 1: 1}, {1: 2, 2: 1, 3: 2}))
print(listAndDict((3, 2, 1), (2, 1, 2)))
print(listAndDict([2, 1], {1: 2, 2: 1, 3: 2}))
print(listAndDict([3, "2", 1], {1: 2, 2: 1, 3: 2}))
