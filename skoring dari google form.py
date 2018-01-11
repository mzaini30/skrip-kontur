fav = open("1. fav.txt", "r").read()
fav = fav
		.replace(", ", ",")



# fav = open("1. fav.txt", "r").read().splitlines()
# fav = [a.replace(", ", ",").replace("\t", "") for a in fav]
# fav = [a.split(",") for a in fav]

# unfav = open("1. unfav.txt", "r").read().splitlines()
# unfav = [a.replace(" ", "").replace("\t", "") for a in unfav]
# unfav = [a.split(",") for a in unfav]

print fav
# print unfav


# flat = [x for sublist in nested for x in sublist]