# mengolah favorable dan unfavorable

fav = open("1. fav.txt", "r").read()
fav = fav.replace("\n", ",").replace("\t", "").replace(" ", "")
fav = fav.split(",")
fav = [int(a) - 1 for a in fav]

unfav = open("1. unfav.txt", "r").read()
unfav = unfav.replace("\n", ",").replace("\t", "").replace(" ", "")
unfav = unfav.split(",")
unfav = [int(a) - 1 for a in unfav]

blueprint = [0] * 10
for a in fav:
	# blueprint[a] = "fav"
	pass

# blueprint[0] = "fav"
print blueprint


# fav = open("1. fav.txt", "r").read().splitlines()
# fav = [a.replace(", ", ",").replace("\t", "") for a in fav]
# fav = [a.split(",") for a in fav]

# unfav = open("1. unfav.txt", "r").read().splitlines()
# unfav = [a.replace(" ", "").replace("\t", "") for a in unfav]
# unfav = [a.split(",") for a in unfav]

print fav
print unfav

print len(fav)
print len(unfav)

# flat = [x for sublist in nested for x in sublist]