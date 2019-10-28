# coding=utf-8
# Zadanie
# Zamiana z Cel na Fah
# F = (C * 9/5) + 32
# Cel = int(input("Podaj temperaturę w skali Cejslujsza: "))
#
# # print(Cel)
#
# Fah = Cel * 9/5 + 32
# print("Fah = Cel * 9/5 +32")
# print(Cel, "stopni Celsjusza to ", Fah, "stopni w skali Fahrenheita")

# Zamiana z Fah na Cel
# C = (F - 32) / 9/5
# Fah = int(input("Podaj temperaturę w skali Fahrenheita: "))
#
# # print(Fah)
#
# Cel = (Fah - 32) * 5/9
# print("Cel = (Fah - 32) / 9/5 ")
# print(Fah, "stopni Fahrenheita to ", Cel, "stopni w skali Celsjusza")


# Zadanie 2
# Sprawdzenie pierwszej i ostatniej cyfry podanej liczby

# liczba = int(input("Prosze podac liczbe: "))
# def pierwsza_cyfra(liczba):
#     # Dzieli przez 10 dopóki nie zostanie ostatnia cyfra
#     while liczba >= 10:
#         liczba = liczba / 10;
#
#         # zwraca pierwszą cyfrę
#     return int(liczba)
#
# # Ostatnia cyfra
# def ostatnia_cyfra(liczba):
#     # reszta z dzielenia przez 10 zwróci ostatnią cyfrę
#     # zwraca ostatnią cyfrę
#     return (liczba % 10)
#
# # podanie cyfr
# print("Pierwsza cyfra to", pierwsza_cyfra(liczba))
# print("Ostatnia cyfra to", ostatnia_cyfra(liczba))


# Zadanie 5
# Sprawdzenie czy podany rok jest przestępny
# Rok jest przestepny jesli jest podzielny przez 4, nie podzielny przez 100, ale podzielny przez 400
# rok = int(input("Prosze podac rok: "))
# if (rok % 4) == 0:
#     if (rok % 100) == 0:
#         if (rok % 400) == 0:
#             print("{0} jest rokiem przestępnym".format(rok))
#         else:
#             print("{0} nie jest rokiem przestępnym".format(rok))
#     else:
#         print("{0} jest rokiem przestępnym".format(rok))
# else:
#     print("{0} nie jest rokiem przestepnym".format(rok))


# Zadanie 9
# Kalkulator wieku psa

# lata = int(input("Prosze podac wiek psa w latach ludzkich: "))
# if lata < 0:
#     print("Pies ma 0 lat w psich latach")
#     exit()
# # dwa pierwsze lata *10.5
# elif lata <= 2:
#     wiek_psa = lata * 10.5
# else:
#     wiek_psa = 21 + (lata - 2) * 4
# print("Pies ma {0} lat w psich latach".format(wiek_psa))




