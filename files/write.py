import date
f = open("students.txt", "w")
dt = datetime.datetime.now()
f.write(dt, "- datetime")
f.write("Richard Jaroensawas\n")
f.write("Vorachet Jaroensawsas\n")
f.close()