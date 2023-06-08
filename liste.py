# listete in python pot sa cuprinda elemente de tipuri diferite
# au dimensiune dinamica

fructe =[100, 'mar' , 'banana' , 'portocala', 3, True, 3]
# afisam o lista
print(fructe)

# accesam un element in functie de index
print(fructe[1])

#adaugam un element
fructe.append('rosie')

# suprascriem un element
fructe[0] = 'para'

#afisam noua lista
print(fructe)

#aflam dimensiunea
print(len(fructe))


# scoate si ne returneaza ultimul element
last = fructe.pop()
print('ultimul element: ',last)
print('noua lista: ' , fructe)

# de cate ori apare un element
print(fructe.count(3))

# extindem lista
fructe_exotice = ['ananas', 'kiwi']
fructe.extend(fructe_exotice)

