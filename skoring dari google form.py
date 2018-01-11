import os

blueprint = open("blueprint.txt", "r").read().splitlines()
# print blueprint

data = open("data.txt", "r").read().splitlines()
data = [a.split("\t") for a in data]
# print data

skoring = []
error = False
for a, b in enumerate(data):
	for n, x in enumerate(blueprint):
		if blueprint[n] == "fav":
			if data[a][n] == "Sangat Setuju":
				skoring.append("4")
			elif data[a][n] == "Setuju":
				skoring.append("3")
			elif data[a][n] == "Tidak Setuju":
				skoring.append("2")
			elif data[a][n] == "Sangat Tidak Setuju":
				skoring.append("1")
			else:
				skoring.append("error")
				error = True

		elif blueprint[n] == "unfav":
			if data[a][n] == "Sangat Setuju":
				skoring.append("1")
			elif data[a][n] == "Setuju":
				skoring.append("2")
			elif data[a][n] == "Tidak Setuju":
				skoring.append("3")
			elif data[a][n] == "Sangat Tidak Setuju":
				skoring.append("4")
			else:
				skoring.append("error")
				error = True

skoring = [skoring[i:i+len(blueprint)] for i in range(0,len(skoring),len(blueprint))]
# print skoring
# print skoring[0][11]

hasil = open("hasil.txt", "w")
# print len(data)
# print len(blueprint)

for n, x in enumerate(data):
	for a, b in enumerate(blueprint):
		hasil.write(skoring[n][a])
		hasil.write("\t")
	hasil.write("\n")

if error == True:
	print "Ada error. Cek hasil.txt"
print "Selesai."
os.system("pause")