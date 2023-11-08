tedad = int(input())
geymat = []
keyfiat = []
for i in range(0, tedad):
    vorodi = input()
    vorodi = vorodi.split()
    geymat.append(int(vorodi[0]))
    keyfiat.append(int(vorodi[1]))
vaziat = ""
max_geymat = max(geymat)
index_keyfiat_max_geymat = geymat.index(max_geymat)
keyfiat_geymate_max = keyfiat[index_keyfiat_max_geymat]
for i in range(0, tedad):
    for i in geymat:
        if max_geymat > i:
            price_jadid = i
            index_keyfiat_jadid = geymat.index(price_jadid)
            keyfiate_jadid = keyfiat[index_keyfiat_jadid]
            if keyfiate_jadid > keyfiat_geymate_max:
                vaziat = "t"
if vaziat == "t":
    print("happy irsa")
else:
    print("poor irsa")




