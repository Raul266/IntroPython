# list = [expresie for item in iterable]
# list = [expresie for item in iterable if conditie]
# expresia se va adauga la lista doar daca conditia IF este True

# EX 1:Adaugati intr-o lista toate numerele de la 0 la 10 inmutite cu 3
# METODA CLASICA
# lst = []
# for i in range (11):
#     lst.append(i*3)
# print(lst)

# METODA COMPREHENSION
# lst = [i*3 for i in range(11)]
# print(lst)

# EX 2 Adaugati toate numerele impare care se afla intr-o lista de la 0 la 100. Afisati lista

# METODA CLASICA
# lst  = []
# for i in  range(101):
#     if i%2 != 0:
#         lst.append(i)
# print(lst)

# METODA COMPREHENSION
# lst = [i for i in range(101) if i%2 != 0]
# print(lst)

# EX 3 Adaugati intr-o lista noua striungurile (sau in cazul nostru limbile) FARA spatiu
# lst_of_languages = ['   romana    ', '    germana   ', '   poloneza    ', '   engleza   ']
# # METODA CLASICA
# # new_lst_of_languages = []
# # for limba in lst_of_languages:
# #     new_lst_of_languages.append(limba.strip())
# # print(new_lst_of_languages)
#
# # Metoda COmprehension
# new_lst_of_languages = [limba.strip() for limba in lst_of_languages]
# print(new_lst_of_languages)

# ex 4 Adaugati intr=o lista noua toate persoanele care au peste 18 ani
# persoane = [ ('Maria', 16), ('Radu' , 26), ('Matei', 87), ('Dani', 27), ('Raluca', 11)]
# adulti = []
# for nume in persoane:
#     if nume[1] >= 18:
#         adulti.append(nume[0])
# print(adulti)

# for nume, varsta in persoane:
#     if varsta >=18:
#         adulti.append(nume)
# print(adulti)


# METODA COMPEHENSIONS
# adulti = [nume[0] for nume in persoane if nume[1]>=18]
# print(adulti)
