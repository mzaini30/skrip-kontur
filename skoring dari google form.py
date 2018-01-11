import os

# mengolah favorable dan unfavorable

fav = open("1. fav.txt", "r").read()
fav = fav.replace("\n", ",").replace("\t", "").replace(" ", "")
fav = fav.split(",")
fav = [int(a) - 1 for a in fav]

unfav = open("1. unfav.txt", "r").read()
unfav = unfav.replace("\n", ",").replace("\t", "").replace(" ", "")
unfav = unfav.split(",")
unfav = [int(a) - 1 for a in unfav]

blueprint = [None] * (len(fav) + len(unfav))
for a in fav:
	blueprint[a] = "fav"
for a in unfav:
	blueprint[a] = "unfav"

# copas dari skrip sebelumnya

data = open("data.txt", "r").read().splitlines()
data = [a.split("\t") for a in data]

opsi = open("opsi.txt", "r").read().splitlines()

skoring = []
error = False

for a, b in enumerate(data):
	for n, x in enumerate(blueprint):

		if len(opsi) == 4:
			if blueprint[n] == "fav":
				if data[a][n] == opsi[0]:
					skoring.append("4")
				elif data[a][n] == opsi[1]:
					skoring.append("3")
				elif data[a][n] == opsi[2]:
					skoring.append("2")
				elif data[a][n] == opsi[3]:
					skoring.append("1")
				else:
					skoring.append("error")
					error = True

			elif blueprint[n] == "unfav":
				if data[a][n] == opsi[0]:
					skoring.append("1")
				elif data[a][n] == opsi[1]:
					skoring.append("2")
				elif data[a][n] == opsi[2]:
					skoring.append("3")
				elif data[a][n] == opsi[3]:
					skoring.append("4")
				else:
					skoring.append("error")
					error = True

			else:
				print "Cek blueprint.txt"

		elif len(opsi) == 5:
			if blueprint[n] == "fav":
				if data[a][n] == opsi[0]:
					skoring.append("5")
				elif data[a][n] == opsi[1]:
					skoring.append("4")
				elif data[a][n] == opsi[2]:
					skoring.append("3")
				elif data[a][n] == opsi[3]:
					skoring.append("2")
				elif data[a][n] == opsi[4]:
					skoring.append("1")
				else:
					skoring.append("error")
					error = True

			elif blueprint[n] == "unfav":
				if data[a][n] == opsi[0]:
					skoring.append("1")
				elif data[a][n] == opsi[1]:
					skoring.append("2")
				elif data[a][n] == opsi[2]:
					skoring.append("3")
				elif data[a][n] == opsi[3]:
					skoring.append("4")
				elif data[a][n] == opsi[4]:
					skoring.append("5")
				else:
					skoring.append("error")
					error = True

			else:
				print "Cek blueprint.txt"

		else:
			print "Berapa jumlah opsinya?"

skoring = [skoring[i:i+len(blueprint)] for i in range(0,len(skoring),len(blueprint))]

hasil = open("hasil.txt", "w")

for n, x in enumerate(data):
	for a, b in enumerate(blueprint):
		hasil.write(skoring[n][a])
		hasil.write("\t")
	hasil.write("\n")

if error == True:
	print "Ada error. Cek hasil.txt"
print "Selesai."
os.system("pause")