def articles(listOfDicts):
	if not isinstance(listOfDicts, list): raise Exception()
	if not all(isinstance(item, dict) for item in listOfDicts): raise Exception()
	if not all(True if tuple(item)==("cijena", "naziv", "kolicina") else False for item in listOfDicts): raise Exception()
	artikli, cijena = [], 0
	for artiklDict in listOfDicts:
		artikli.append(artiklDict["naziv"])
		cijena += artiklDict["cijena"] * artiklDict["kolicina"]
	return {"ukupno": {"artikli": artikli, "cijena": cijena}}

print(articles([{"cijena": 8, "naziv": "Kruh", "kolicina": 1}, {"cijena": 13, "naziv": "Sok", "kolicina": 2}, {"cijena": 7, "naziv": "Upaljac", "kolicina": 1}]))
print(articles([{"cijena": 8, "naziv": "Kruh", "kolicina": 3}, {"cijena": 8, "naziv": "Sok", "kolicina": 10}]))
print(articles([{"kolicina": 8, "naziv": "Kruh", "cijena": 3}, {"cijena": 3, "naziv": "Sok", "kolicina": 10}]))
print(articles([{"Cijena": 8, "naziv": "Kruh", "kolicina": 3}, {"cijena": 8, "naziv": "Sok", "kolicina": 10}]))
