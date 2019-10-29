# coding=utf-8
# Zadanie 1
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
#Prośba o podanie liczby i zdefiniowanie jej jako int

# liczba = input("Prosze podac liczbe: ")
#
# if liczba.isdigit() == False:
#    print("Prosze podac liczbe calkowita")
# else:
#     pierwsza_cyfra = liczba[0]
#     ostatnia_cyfra = liczba[-1]
#     print("Pierwsza cyfra to {0}".format(pierwsza_cyfra))
#     print("Ostatnia cyfra to {0}".format(ostatnia_cyfra))



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


# Zadanie 8
# wysokosc = int(input("Prosze podac wysokosc piramidy: "))
# for i in range (0, wysokosc):
#     for j in range(0, wysokosc - i):
#         print(end=" ")
#     for j in range(0, (i * 2)-1):
#         print("#", end=" ")
#     print()




