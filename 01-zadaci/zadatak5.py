def students(listOfStudents):
	return sorted([{"id": student[0], "ime": student[1], "prezime": student[2]} for student in listOfStudents if student[1][1].casefold()==student[2][1].casefold()], key=lambda k: k["id"])

print(students([(121, "Ivan", "Ivic"), (431, "Pero", "Horvat"), (31, "Marija", "Maric")]))
print(students([(121, "ivan", "Ivic"), (431, "Pero", "Horvat"), (31, "Marija", "maric")]))
print(students([(121, "Ivan", "Maric"), (431, "Pero", "Horvat"), (31, "Marija", "Ivic")]))
