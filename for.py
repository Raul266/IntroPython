# # problema 101 dalmatieni
# for i in range (1, 102):
#     print(f'dalmatianul cu nr {i}')
# # problema numaram dalmatienii din 2 in 2
# for i in range (1, 102, 2):# ultimul parametru ne indica pasul in exemplul dat din 2 in 2
#     print(f'dalmatianul cu nr {i}')

# numere = [3, 7, 10, 20, 30]
# # parcurgerea unei liste cu for prin intermediul indexului
# for i in range(0, len(numere)):
#     print(f'indexul curent este {i}') #aici vedem nr de index din lista
#     print(f'numarul curent este {numere[i]}')# aici ne arata valoare pentru fiecare index in parte

# for each
# s=0
# for numar in numere:
#     print(f' numarul curent este {numar}')
#     s=s+ numar
#     print(f'suma este {s}')

# tema de cate ori apare 3 in  [3, 2, 3, 5 ,3]
numere = [3, 2, 3, 5, 3]

print(numere.count(3))