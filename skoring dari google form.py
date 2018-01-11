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

print blueprint

print fav
print unfav