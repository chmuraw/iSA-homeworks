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
# liczba = input("Proszę podać liczbę: ")
# first_digit = liczba
# while(liczba >= 10):
#     liczba = liczba // 10
# print("Pierwsza cyfra liczby {0} = {1}".format(liczba, first_digit))


def pierwsza_cyfra(liczba):
    # Dzieli przez 10 dopóki nie zostanie ostatnia cyfra
    while liczba >= 10:
        liczba = liczba / 10;

        # zwraca pierwszą cyfrę
    return int(liczba)


# Find the last digit
def lastDigit(liczba):
    # reszta z dzielenia przez 10 zwróci ostatnią cyfrę
    # zwraca ostatnią cyfrę
    return (liczba % 10)


# Driver Code
n = 98562;
print(firstDigit(n))
print(lastDigit(n))