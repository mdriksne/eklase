import json

atzimjuSaraksts = {
    "Matematika" : [7, 9, 10, 8],
    "Fizika": [10, 10, 10, 9]
}



while True:

    izvele = input("Ievadiet 'pievienot' lai pievienotu prieksmetu un atzimi, 'izprintet' lai izprintetu prieksmetus un atzimes, 'saglabat' lai saglabtu sarakstu filā, ieladet, lai ieladetu failu, 'izdzest atzimi', lai izdzēstu atzimi, 'izdzest prieksmetu', lai izdzestu prieksmetu, 'jauns fails', lai izvedotu jaunu sarakstu vai ievadiet 'partraukt' lai partrauktu programmu: ")

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

    elif izvele == 'jauns fails':
        saraksts = {}
        atzimjuSaraksts = saraksts
        print("Izveidots jauns fails")

    elif izvele == 'ieladet':
         fails = input("Ievadiet failu, kuru velaties ieladet: ")
         with open(fails, 'r') as f:
             atzimjuSaraksts = json.load(f)
         print("Dati ielādēti no", fails)

    elif izvele == 'saglabat':

         fails = input("Ievaidiet faila nosaukumu: ")
         with open(fails, 'w') as f:
             json.dump(atzimjuSaraksts, f)
         print("Atzimju saraksts tika saglabats ", fails)



    elif izvele == 'izdzest prieksmetu':
         prieksmets = input("Ievadiet prieksmetu kuru velaties izdest: ")
         if prieksmets in atzimjuSaraksts:
             del atzimjuSaraksts[prieksmets]
             print("Prieksmets izdzēsts.")
         else:
             print("Prieksmets nav atrasts.")

    elif izvele == 'izdzest atzimi':
         prieksmets = input("Ievadiet prieksmeta vārdu: ")
         if prieksmets in atzimjuSaraksts:
             atzimes = atzimjuSaraksts[prieksmets]
             atzime = input("Ievadiet atzimi kuru velaties izdzest: ")
             if atzime in atzimes:
                 atzimes.remove(atzime)
                 print("Atzime izdzēsta.")
             else:
                 print("Atzīme nav atrasta.")
         else:
             print("Prieksmets nav atrasts.")


    elif izvele == 'partraukt':
        break

    else:
        print("Nederīga izvele! Lūdzu ievadiet pievienot vai izprintet, vai izdzest atzimi, vai izdezest prieksmetu, vai ieladet, vai saglabat, vai jauns fails vai partraukt.")
        
        
