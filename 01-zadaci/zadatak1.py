def strings(listOfStrings):
	assert all(isinstance(item, str) for item in listOfStrings), "Not all items of list are strings."
	return [item for item in listOfStrings if len(item)>4]

print(strings(["Pas", "Macka", "Stol"]))
print(strings(["Hrcak", "Macka", "Krava"]))
print(strings(["Pas", "Riba", "Stol"]))
print(strings([1, "Macka", "Stol"]))
