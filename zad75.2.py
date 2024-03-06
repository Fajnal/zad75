with open("tekst.txt", "r") as plik:                    #otwieranie pliku tekst.txt z uprawnieniem do odczytania
    for line in plik:
        slowa = line.strip().split()                    #rozdzielanie słów


alfabet = "abcdefghijklmnopqrstuvwxyz"                  #stworzenie zmiennej "alfabet" przechowującej litery alfabetu
odpowiedz = []                                          #stworzenie tabeli "odpowiedz"

def szyfr(slowo, A, B):                                 #funkcja szyfrująca słowa
    global alfabet
    wiadomosc = ""
    for znak in slowo:
        litera = ((alfabet.find(znak)*A) + B)%26
        wiadomosc += alfabet[litera]
    return wiadomosc


for slowo in slowa:
    if len(slowo) >= 10:
        odpowiedz.append(szyfr(slowo, 5, 2))     #przywolanie funcji szyfrującej słowa i dodawanie wyniku do tablicy "odpowiedz"


for slowo in odpowiedz:
    print(slowo)                                        #wypisywanie wszystkich słów w tablicy "odpowiedz"