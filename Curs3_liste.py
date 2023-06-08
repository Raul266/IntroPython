# declaram o lista
legume = ['ardei', 'morcov', 'dovlecel']
print(legume[1]) # o declaram dupa index, dupa index se printeaza sub forma de string
print(legume[0:1]) # daca face slicing se printeaza sub forma de lista intre paranteze[]
print(legume[0:2])

# adaugarea unui element la sfarsitul unei liste
legume.append('vinete')
print(legume)

# adaugarea unui element dupa un index
legume.insert(2,'castravete')
print(legume)

# extend augam o lista unei alte liste
legume = ['ardei', 'morcov', 'dovlecel']
fructe = ['mere','pere','lamai']
legume.extend(fructe)
print(legume)
# observatie acest extend pune uneste doua liste doar prima lista se modifica

# daca vrem sa creeam o lista noua
lista_noua = legume + fructe
print(lista_noua)

# schimbam un element dintr-o lista (schimbam morcov)
legume = ['ardei', 'morcov', 'dovlecel']
legume[1] = 'vanata'
print(legume)

#schimba mai multe elemente dint-o lista (schimba ardei si morcov)
legume = ['ardei', 'morcov', 'dovlecel']
legume[0:2] = ['conopida', 'brocoli']
print(legume)

# adauga mai multe elemente decate inlocuiesti
legume = ['ardei', 'morcov', 'dovlecel']
legume[0:2] = ['vanata', 'conopida', 'brocoli']
print(legume)

# adauga mai putine elemente decat inlocuiesi
legume = ['ardei', 'morcov', 'dovlecel']
legume[0:2] = ['varza']
print(legume)

# verifica daca ' banana ' este in lista folosind if
fructe = ['mere', 'pere', 'lamai', 'banana']
if 'banana' in fructe:
    print('avem banana in lista de frcute')
else:
    print('nu avem banana in fructe')

#vereifica daca avem cel putin doua banane in fructe
fructe = ['mere','banana', 'pere', 'lamai', 'banana']
if fructe.count('banana') >=2:
    print('avem doua sau mai multe banane in lista de fructe')
else:
    print('nu avem doua banane in lista de fructe')

# TUPLE
# declara si afisaza un tuple
fructe = ('mar', 'para', 'capsuni') # nu se poate schimba nici un element din tuple

# printeaza cate elemente sunt intrun tuple
print(len(fructe))






