with open("tekst.txt", "r") as plik:                    #otwieranie pliku tekst.txt z uprawnieniem do odczytania
    for line in plik:
        slowa = line.strip().split()                    #rozdzielanie słów


odpowiedz = []                                          #stworzenie tabeli "odpowiedz"


for slowo in slowa:
    if slowo[0] == slowo[-1] and slowo[0] == "d":       #sprawdzanie, czy słowo zaczyna i kończy się na literę "d"
        odpowiedz.append(slowo)                         #dodawanie słowa do tablicy "odpowiedz"


for slowo in odpowiedz:
    print(slowo)                                        #wypisywanie wszystkich słów w tablicy "odpowiedz"