

macibas = []
n = int(input("Cik priekšmeti?: "))
for i in range(n):
    prieksmets = input("Mācību priekšmeta nosaukums?: ")
    atzime = int
    while atzime != "beigt":
        atzime = input("Kādas ir Tavas atzīmes?: ")
        macibas.append(atzime)
    print(prieksmets, macibas[i])
