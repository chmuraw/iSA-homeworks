## Listy referencyjne

# lista = [1, 2, 3]
# nowa_lista = lista    ## zmianiamy wartosc tylko na podstawowej liscie, ale przez to ze sa referencyjne, to w nowa lista wartosc rowniez bedzie zmieniona (uzywaja tego samego adresu w pamieci)
#
# kopia_listy = lista.copy() ## wyrzuci pierwsza wartosc bez zmian (oryginalna liste)
#
# lista[0] = 'x'
# print(lista)
# print(nowa_lista)
# print(kopia_listy)

# import copy    #importuje, zeby moc uzyc glebokiego kopiowania (to nie jest wbudowana funkcja)
#
#
# lista = [1,
#          2,
#          3,
#          ['A', 'B', 'C']
#          ]
#
# nowa_lista = lista
# kopia_listy = lista.copy() # wezmie bez zmian pierwsza czesc listy, ale zmieni w zagniezdzeniu - troche misz masz w pamieci
# gleboka_kopia_listy = copy.deepcopy(lista)
# lista[0] = 'x'
# lista[3][0] = 'y'     #zamieni A (zagniezdzone listy - szuka pozycji zero z trzeciego elementu, czyli z tej zagniezdzonej)
#
# print(lista)
# print(nowa_lista) # to dziala referencyjnie w kazdym przypadku - zawsze odnoscik do glownej listy
# print(kopia_listy)  # pierwszy poziom jest kopiowany bez zmian, a druga czesc jest zmieniona
# print(gleboka_kopia_listy) # skopiowana "doglebnie" cokolwiek zrobie z pierwotna lista. nie wprowadzi zadnych zmian ani w pierwszej liscie ani w zagniezdzonej

## !!!! Referencja powoduje ze mamy zapisany adres do pamieci, a nie kopiujemy samych wartosci !!!!
# jezeli pracujemy na jakichs danych, ktorych zrodla nie mozemy zmieniac, to korzystamy z kopii albo glebokich kopii. dla pewnosci, zeby nie modyfikowac bez potrzeby i zeby nie przechowywac w pamieci duzej ilosci danych



##=================================================================

## FUNKCJE!

# #definiuje funkcje, ktora ma drukowac komunikat.
# def witaj():
#     print('Czesc, jestem twoim nowym programem.')
# hi = witaj   # tutaj przypisuje funkcje do zmiennej. potem moge wywolac ja wywolujac zmienna.
# #wywolanie funkcji
# #witaj()
# hi()

## jezeli napisalabym tak: hi = witaj()  <--- to juz w tym momencie interpreter bedzie chcial wywolac funkcje. wiec przypisze wynik funkcji.
## print(hi) - ciekawe, bo wyswietli po prostu adres funkcji. nie wyswietli przypisanej wartosci





## zdefioniowane argumenty funkcji

# def do_nothing(x, y, imie="Ola", wiek=22):
#     pass  #uzywam tego, zeby interpreter przeszedl dalej, kiedy wiem ze funkcja bedzie uzywana dalej.
   # print("Not implemented yet")   # zamiennie do pass

#do_nothing(1)   #trzeba podac drugi argument!
#do_nothing(1,2, "Iza") #bez problemu
#do_nothing(1,2, imie = "Iza", 22) #nie zadziala bo trzeba by bylo nazwac tez argument wiek
#do_nothing(1, 2, imie = Iza", wiek=14) #tu rozkmin bo cos sie nie zgadza
#do_nothing(1,2, wiek=22, imie = "Iza") # tu dziala bez problemu

# dobra zasada jest wprowadzanie argumentow zgodnie z kolejnoscia z definiowania funkcji.

## ================================================================

## RETURN







