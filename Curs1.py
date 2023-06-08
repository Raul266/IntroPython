# curs 1 Functia type() si tipe casting
# cu print (type(variabila)) printeaza tipul de variabila
nume1 = 'Raul'
print(type(nume1))
varsta = 25
print(type(varsta))
varsta = str(varsta)# asa se poate schimba orice tip de variabia in alt tip
print(type(varsta))

#intotdeauna INDEXUL unei variabile cand se numara incepe de la 0 (ZERO)
# cu functia len alfam cate caractere are o variabile
nume = "Alexandru"
print(len(nume))
print(nume[4]) # raspunsul va fi a deoarece numaratoarea incepe de la 0
print(nume[-1]) # incepe numaratoarea din celalalt capat raspunsul va fi u
print(nume[0:4]) # raspunsul va fi alex pt ca se iau toate caracterele de la 0 la 3 adica inainte cu un index de cel scris
print(nume[0:4:2]) # razpunsul va fi Ae deoarece ultimul 2 pe care l-am pus este pasul
print(nume [::-1]) # scriem invers raspunsul va fi urdnaxelA

nume2 = 'Alex Rotaru'
print(nume2[5:]) #printam doar Rotaru adica incepe de la indexul 5 si cu : merge pana la final
print(nume2[-6:]) # printam doar Rotaru doar ca incepem de la -6

nume3 = 'gLeN'
print(nume3.upper()) # mareste toate caracterele si returneaza o copie deci nu schimba valoare pt totdeauna
# daca vrem sa schimbam variabila pt totdeauna folosim suprascriere
nume3 = nume3.upper() # si am schimbat variabila initiala in variabila cu litere mari