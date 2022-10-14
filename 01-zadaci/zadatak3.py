def articles(listOfDicts):
	assert isinstance(listOfDicts, list), "Parameter is not a list."
	assert all(isinstance(item, dict) for item in listOfDicts), "Not all list (parameter) elements are dictionaries."
	assert all(True if tuple(item)==("cijena", "naziv", "kolicina") else False for item in listOfDicts), "Not all dictionaries have keys ('cijena', 'naziv', 'kolicina')"
	artikli, cijena = [], 0
	for artiklDict in listOfDicts:
		artikli.append(artiklDict["naziv"])
		cijena += artiklDict["cijena"] * artiklDict["kolicina"]
	return {"ukupno": {"artikli": artikli, "cijena": cijena}}

print(articles([{"cijena": 8, "naziv": "Kruh", "kolicina": 1}, {"cijena": 13, "naziv": "Sok", "kolicina": 2}, {"cijena": 7, "naziv": "Upaljac", "kolicina": 1}]))
print(articles([{"cijena": 8, "naziv": "Kruh", "kolicina": 3}, {"cijena": 8, "naziv": "Sok", "kolicina": 10}]))
print(articles(({"cijena": 8, "naziv": "Kruh", "kolicina": 3}, {"cijena": 8, "naziv": "Sok", "kolicina": 10})))
print(articles([{"cijena": 8, "naziv": "Kruh", "kolicina": 3}, {"cijena", "naziv", "kolicina"}]))
print(articles([{"kolicina": 8, "naziv": "Kruh", "cijena": 3}, {"cijena": 3, "naziv": "Sok", "kolicina": 10}]))
print(articles([{"Cijena": 8, "naziv": "Kruh", "kolicina": 3}, {"cijena": 8, "naziv": "Sok", "kolicina": 10}]))
