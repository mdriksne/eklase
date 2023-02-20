import json

while True:

    sarakstaIzvele = input("jauns fails / ieladet ? : ")

    if sarakstaIzvele == 'jauns fails':
        atzimjuSaraksts = {}
        print("Izveidots jauns fails")
        break

    elif sarakstaIzvele == 'ieladet':
         fails = input("Ievadiet failu, kuru velaties ieladet: ")
         with open(fails, 'r') as f:
             atzimjuSaraksts = json.load(f)
         print("Dati ielādēti no", fails)
         break
    else:
        print("Nederīga izvēle")

while True:

    izvele = input("Ievadiet 'pievienot' lai pievienotu prieksmetu un atzimi, 'izprintet' lai izprintetu prieksmetus un atzimes, 'saglabat' lai saglabtu sarakstu filā, 'izdzest', lai izdzēstu atzimi vai failu, vai ievadiet 'partraukt' lai partrauktu programmu: ")

    if izvele == 'pievienot':

        prieksmets = input("Ievadiet prieksmeta nosaukumu: ")
        atzimes = []

        while True:
            atzime = input("Ievadiet atzimi no 1 lidz 10, nv vai tukss (lai beigtu ievadi rakstiet partraukt): ")

            if atzime == 'partraukt':
                break

            elif str(atzime)=='tukss':
                atzimjuSaraksts[prieksmets] = atzimes
                break

            elif str(atzime)=='nv':
                atzimes.append(str(atzime))

            elif atzime.isdigit() and int(atzime) >= 1 and int(atzime) <= 10:
                atzimes.append(int(atzime))

            else:
                print("Nederiga atzime. Ludzu ievadiet atzimi no 1-10, nv vai tukss")

        if prieksmets in atzimjuSaraksts:
            esosasAtzimes = atzimjuSaraksts[prieksmets]
            esosasAtzimes.extend(atzimes)
            atzimjuSaraksts[prieksmets] = esosasAtzimes
        else:
            atzimjuSaraksts[prieksmets] = atzimes

    elif izvele == 'izprintet':

        while True:

            printIzvele = input("Ievadiet prieksmeta nosaukumu: ")

            if printIzvele == 'partraukt':
                break

            elif printIzvele == 'visus':
                for prieksmeti in atzimjuSaraksts:
                    print(prieksmeti)

            else:
                if printIzvele in atzimjuSaraksts:
                    printAtzimes = atzimjuSaraksts[printIzvele]
                    print(printIzvele +' atzimes:')
                    for atzime in printAtzimes:
                        print(atzime)
                else:
                    print('Tāds priekšmets nav sarakstā!')

    elif izvele == 'saglabat':

         fails = input("Ievaidiet faila nosaukumu: ")
         with open(fails, 'w') as f:
             json.dump(atzimjuSaraksts, f)
         print("Atzimju saraksts tika saglabats ", fails)

    elif izvele == 'izdzest':

        izdzestIzvele = input("Izdzest priekšmetu vai atzīmi (prieksmetu / atzimi)?")

        if izdzestIzvele == 'prieksmetu':
            prieksmets = input("Ievadiet prieksmetu kuru velaties izdest: ")
            if prieksmets in atzimjuSaraksts:
                del atzimjuSaraksts[prieksmets]
                print("Prieksmets izdzēsts.")
            else:
                print("Prieksmets nav atrasts.")

        elif izdzestIzvele == 'atzimi':
            prieksmets = input("Ievadiet prieksmeta vārdu: ")
            if prieksmets in atzimjuSaraksts:
                atzimes = atzimjuSaraksts[prieksmets]
                atzime = input("Ievadiet atzimi kuru velaties izdzest: ")
                if atzime in atzimes:
                    atzimes.remove(atzime)
                    print("Atzīme izdzēsta.")
                elif int(atzime) in atzimes:
                    atzimes.remove(int(atzime))
                    print("Atzime izdzēsta.")
                else:
                    print("Atzīme nav atrasta.")
            else:
                print("Prieksmets nav atrasts.")

        else: 
            print("Nederīga izvēle")


    elif izvele == 'partraukt':
        break

    else:
        print("Nederīga izvele! Lūdzu ievadiet pievienot vai izprintet, vai izdzest, vai saglabat, vai vai partraukt.")
