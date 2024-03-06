with open("probka.txt", "r") as plik:                                                           #otwieranie pliku tekst.txt z uprawnieniem do odczytania
    probka = [line.strip().split() for line in plik]                                            #rozdzielanie słów


alfabet = "abcdefghijklmnopqrstuvwxyz"                                                          #stworzenie zmiennej "alfabet" przechowującej litery alfabetu
odpowiedz = []                                                                                  #stworzenie tabeli "odpowiedz"


def zakoduj(slowo, A, B):                                                                       #funkcja szyfrująca słowa
    global alfabet
    wiadomosc = ""
    for znak in slowo:
        litera = ((alfabet.find(znak)*A) + B)%26
        wiadomosc += alfabet[litera]
    return wiadomosc


def dekoduj(tekst1, tekst2):                                                                    #funkcja dekodująca słowa
    global alfabet
    for A in range(26):
        for B in range(26):
            if zakoduj(tekst1, A, B) == tekst2:
                return [A, B]


for komplet in probka:
    szyfrujacy = dekoduj(komplet[0], komplet[1])                                                #określenie klucza szyfrującego
    deszyfrujacy = dekoduj(komplet[1], komplet[0])                                              #określenie klucza deszyfrującego
    odpowiedz.append([komplet, szyfrujacy, deszyfrujacy])                                       #dodawanie słów oraz kluczy do tablicy "odpowiedz"


for i in odpowiedz:
    print("\"{}\", szyfrujacy: {}, deszyfrujacy: {}".format(" ".join(i[0]), i[1], i[2]))    #wypisywanie odpowiedzi