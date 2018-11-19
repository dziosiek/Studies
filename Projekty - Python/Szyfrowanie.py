# -*- coding: utf-8 -*-

lista_slow_plik = "lista_slow.txt"

def zaladuj_lista_slow():
    """
    zwraca liste slow ze slownika
    """

    print "czytam slownik..."
    with open(lista_slow_plik, 'r+', 0) as plik:
        linia = plik.read()
    ls = linia.split()
    print "\t", len(ls), "slow wczytano."  
    return ls

lista_slow = zaladuj_lista_slow()

def jest_slowem(lista_slow, slowo):
    """
    sprawdza czy slowo jest slowem (polskim)

    lista_slow: lista slow.
    slowo: slowo podejrzane o bycie slowem.
    zwraca: True jezeli slowo jest w liscie.

    Np:
    >>> jest_slowem(lista_slow, 'kot')
    True
    >>> jest_slowem(lista_slow, 'asdf')
    False
    """

    slowo = slowo.lower()
    slowo = slowo.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\'")
    return slowo in lista_slow

def czytaj_info():
    """
    Pobiera zaszyfrowany tekst z paroma informacjami.
    """

    with open("szyfrogram.txt", "r") as f:
        historia = str(f.read())
    return historia

def zbuduj_szyfr(przesuniecie):
    """
    Zwraca slownik, ktory mozna zastosowac do szyfru Cezara.
    Szyfr jest zdefiniowany poprzez przesuniecie. Ignoruje wszystkie
    znaki nie bedace literami alfabetu PL lub spacja.
    Spacja mapowana jest do litery odleglej od litery 'a' o
    przesuniecie - 1.
    
    przesuniecie: 0 <= int < 27 (tylko alfabet EN)
    zwraca: slownik

    Przyklad:
    >>> zbuduj_szyfr(3)
    {' ': 'c', 'A': 'D', 'C': 'F', 'B': 'E', 'E': 'H', 'D': 'G',
    'G': 'J', 'F': 'I', 'I': 'L', 'H': 'K', 'K': 'N', 'J': 'M',
    'M': 'P', 'L': 'O', 'O': 'R', 'N': 'Q', 'Q': 'T', 'P': 'S',
    'S': 'V', 'R': 'U', 'U': 'X', 'T': 'W', 'W': 'Z', 'V': 'Y',
    'Y': 'A', 'X': ' ', 'Z': 'B', 'a': 'd', 'c': 'f', 'b': 'e',
    'e': 'h', 'd': 'g', 'g': 'j', 'f': 'i', 'i': 'l', 'h': 'k',
    'k': 'n', 'j': 'm', 'm': 'p', 'l': 'o', 'o': 'r', 'n': 'q',
    'q': 't', 'p': 's', 's': 'v', 'r': 'u', 'u': 'x', 't': 'w',
    'w': 'z', 'v': 'y', 'y': 'a', 'x': ' ', 'z': 'b'}
    (kolejnosc moze sie roznic - w koncu to slownik)
    """

    alfabet = [
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
        'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' '
    ]

    slownik = {}
    for i in range(len(alfabet)):
        tmp = i + przesuniecie
        if tmp > len(alfabet) - 1:
            if alfabet[i] == ' ':
                slownik[alfabet[i]] = alfabet[tmp - len(alfabet)]
            else:
                slownik[alfabet[i]] = alfabet[tmp - len(alfabet)]
                slownik[alfabet[i].upper()] = alfabet[tmp - len(alfabet)].upper()
        else:
            slownik[alfabet[i]] = alfabet[tmp]
            slownik[alfabet[i].upper()] = alfabet[tmp].upper()

    return slownik

def zbuduj_koder(przesuniecie):
    """
    Zwraca slownik ktory bedzie sluzyl do szyfrowania tekstu jawnego,
    tak by mozna bylo uzyc tego typu wywolan:
    >>> szyfr = zbuduj_koder(3)
    >>> szyfrogram = zastosuj_szyfr(tekst_jawny, szyfr)

    przesuniecie: 0 <= int < 27 (tylko alfabet EN)
    zwraca: slownik
    
    >>> zbuduj_koder(3)
    {' ': 'c', 'A': 'D', 'C': 'F', 'B': 'E', 'E': 'H', 'D': 'G',
    'G': 'J', 'F': 'I', 'I': 'L', 'H': 'K', 'K': 'N', 'J': 'M',
    'M': 'P', 'L': 'O', 'O': 'R', 'N': 'Q', 'Q': 'T', 'P': 'S',
    'S': 'V', 'R': 'U', 'U': 'X', 'T': 'W', 'W': 'Z', 'V': 'Y',
    'Y': 'A', 'X': ' ', 'Z': 'B', 'a': 'd', 'c': 'f', 'b': 'e',
    'e': 'h', 'd': 'g', 'g': 'j', 'f': 'i', 'i': 'l', 'h': 'k',
    'k': 'n', 'j': 'm', 'm': 'p', 'l': 'o', 'o': 'r', 'n': 'q',
    'q': 't', 'p': 's', 's': 'v', 'r': 'u', 'u': 'x', 't': 'w',
    'w': 'z', 'v': 'y', 'y': 'a', 'x': ' ', 'z': 'b'}
    (kolejnosc moze sie roznic - w koncu to slownik)
    """

    return zbuduj_szyfr(przesuniecie)

def zbuduj_dekoder(przesuniecie):
    """
    Zwraca slownik ktory bedzie sluzyl do odszyfrowywania tekstu zakodowanego,
    tak by mozna bylo uzyc tego typu wywolan:
    >>> szyfr = zbuduj_koder(3)
    >>> szyfrogram = zastosuj_szyfr(tekst_jawny, szyfr)
    >>> deszyfr = zbuduj_dekoder(3)
    >>> test_odszyfrowany = zastosuj_szyfr(szyfrogram, deszyfr)    
    przesuniecie: 0 <= int < 27 (tylko alfabet EN)
    zwraca: slownik
    

    >>> zbuduj_dekoder(3)
    {' ': 'x', 'A': 'Y', 'C': ' ', 'B': 'Z', 'E': 'B', 'D': 'A', 'G': 'D',
    'F': 'C', 'I': 'F', 'H': 'E', 'K': 'H', 'J': 'G', 'M': 'J', 'L': 'I',
    'O': 'L', 'N': 'K', 'Q': 'N', 'P': 'M', 'S': 'P', 'R': 'O', 'U': 'R',
    'T': 'Q', 'W': 'T', 'V': 'S', 'Y': 'V', 'X': 'U', 'Z': 'W', 'a': 'y',
    'c': ' ', 'b': 'z', 'e': 'b', 'd': 'a', 'g': 'd', 'f': 'c', 'i': 'f',
    'h': 'e', 'k': 'h', 'j': 'g', 'm': 'j', 'l': 'i', 'o': 'l', 'n': 'k',
    'q': 'n', 'p': 'm', 's': 'p', 'r': 'o', 'u': 'r', 't': 'q', 'w': 't',
    'v': 's', 'y': 'v', 'x': 'u', 'z': 'w'}
    (kolejnosc moze sie roznic - w koncu to slownik)
    """

    return zbuduj_koder(przesuniecie)


def zastosuj_koder(tekst, szyfr):
    """
    Zastosuj szyfr (w formie slownika). Zwroc szyfrogram.

    tekst: string
    kod: slownik mapujacy odpowiednie litery na inne
    returns: string - szyfrogram

    Przyklad
    >>> zastosuj_koder("Ala ma kota", zbuduj_koder(3))
    'Dodcpdcnrwd'
    >>> zastosuj_koder("Dodcpdcnrwd", zbuduj_koder(24))
    'Ala ma kota'
    """

    tmp = ''
    for i in tekst:
        try:
            tmp += szyfr[i]
        except KeyError:
            tmp += i
    return tmp


def zastosuj_przesuniecie(szyfr, przesuniecie):
    """
    Zaszyfruj wykorzystujac przesuniecie.

    tekst: string zawierajacy tekst jawny
    przesuniecie: int - odleglosc o ile przesuwamy litery (0 <= int < 27)
    zwraca: string - szyfrogram

    Przyklad
    >>> zastosuj_przesuniecie("Ala ma kota", 8)
    'Itihuihswai'
    >>> zastosuj_przesuniecie("Itihuihswai", 19)
    'Ala ma kota'
    """

    return zastosuj_koder(szyfr, zbuduj_koder(przesuniecie))

def znajdz_najlepsze_przesuniecia(lista_slow, tekst):
    """
    Znajdz przesuniecie jakim zaszyfrowany jest tekst.

    tekst: string
    zwraca: 0 <= int < 27

    Przyklad
    >>> szyfrogram = zastosuj_przesuniecie("Ala ma kota", 13)
    >>> print szyfrogram
    Nynmznmxafn
    >>> znajdz_najlepsze_przesuniecia(lista_slow, szyfrogram)
    14
    >>> zastosuj_przesuniecie(szyfrogram, 14)
    'Ala ma kota'
    """

    found = False
    i = 0

    while not found:
        i += 1
        tmp = zastosuj_przesuniecie(tekst, i).split(' ')
        if tmp[0] == '': tmp.remove('')
        if tmp[len(tmp)-1] == '': tmp.remove('')
        for j in tmp:
            if jest_slowem(lista_slow, j):
                found = True
                break
            else:
                break
    return i

def odkoduj_info(gadaj = False):
    """
    Tu odszyfrowywujemy historyjke.

    zwraca: string - jawny tekst szyfrogramu
    """

    tmp = ''
    tmp2 = []

    plik = open("szyfrogram.txt", 'r')
    lista = list(plik.read())
    plik.close()
    lista.remove('\n')
    lista = ''.join(lista)
    tmp = zastosuj_przesuniecie(lista, znajdz_najlepsze_przesuniecia(lista_slow, lista))

    for i in range(len(tmp)):
        tmp2.append(tmp[i])
        if tmp[i] == '.' and tmp[i-1] not in ['1', '2', '3', '4', '5']: tmp2.append('\n')

    return ''.join(tmp2)

print odkoduj_info()
