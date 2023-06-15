# # Ex1 afisaza date in functie de viteza masinii.
'''
daca se da de la tastatura viteza negativa afiseaza "viteza invalida"
daca avem 0  km/h afiseaza stationare
daca avem 50 km/h afiseaza locatitate
daca avem 90 km/h afiseaza drum european
daca avem peste 90 km/h afiseaza autostrada
'''
viteza = int(input('introdu viteza km/h'))
if viteza < 0:
    print('viteza invalida')
elif viteza == 0:
    print('masina stationeaza')
elif viteza <= 50:
    print('masina este in localitate')
elif viteza <=90:
    print('masina este pe un drum european')
else:
    print('masina este pe autostrada')

# Ex2 Afisaza date despre persoana in functie de varsta
'''
daca are sub 0 ani afiseaza nenascut
daca are intre 0 si 1 ani afiseza nou nascut
daca are intre 2 si 14 ani afiseza copil
daca are intre 15 si 17 ani afiseza adolescent
daca are peste 18 ani afiseaza adult
daca are peste 60 de ani afiseza batran
'''
varsta = int(input('scrie varsta'))
if varsta < 0 :
    print('nenascut')
elif varsta == 0:
    print('nou-nascut')
elif varsta == 1:
    print('nou-nascut')
elif varsta >= 2 and  varsta <= 14 :
    print('copil')
elif varsta <= 17:
    print('adolescent')
elif varsta >= 18 and varsta < 60:
    print('adult')
elif varsta >= 60 :
    print('batran')

# # 4. Exercițiu:
'''
- citește un string de la tastatură (ex: alabala portocala);
- salvează primul caracter într-o variabilă - indiferent care este el;
- capitalizează acest caracter peste tot, mai puțin pentru primul și ultimul
caracter => alAbAlA portocAla.
'''
x = input('String')
text, xlow = x[1:-1], x.lower()
first, last = xlow[0], xlow[-1]
print(f"{first}{text.replace(first, first.upper())}{last}")

# Exerciții Opționale - grad de dificultate: Mediu spre greu(may need google) .
# 1. Ne imaginăm o echipă de fotbal pt teren sintetic.
# 3 Schimbări maxime admise:
# ● Declară o Listă cu 5 jucători
# ● Schimbari_efectuate = te joci tu cu valori diferite
# ● Schimbari_max = 3
# Dacă Jucătorul x e în teren și mai avem schimbări la dispoziție
# - Efectuează schimbarea
# - Șterge jucătorul scos din listă
# - Adaugă jucătorul intrat
# - Afișaza a intra x, a ieșit y, mai ai z schimbări
# Dacă jucătorul nu e în teren:
# - Afișază ‘ nu se poate efectua schimbarea deoarece jucătorul x nu e în
# teren’
# - Afișază ‘mai ai z schimbări
echipa = {'Raul', 'Dani', 'Ovi', 'Gabi', 'Alex'}
rezerve = {'Cristi','Bogdan','Tudor', 'Mircea'}
schimbari_efectuate = 0
schimbari_max = 3
while schimbari_efectuate < schimbari_max:
    jucator_schimbat = input('scoateti jucator: ')
    jucator_intrat = input('introduceti jucator: ')
    if  jucator_schimbat in echipa:
        echipa.remove(jucator_schimbat)
        rezerve.remove(jucator_intrat)
        echipa.add(jucator_intrat)
        schimbari_efectuate = schimbari_efectuate + 1
        print(echipa)
        print(f'A intrat jucatorul {jucator_intrat}, si a iesit {jucator_schimbat}, mai ai inca  {3-schimbari_efectuate} schimbari')
    elif jucator_intrat in rezerve:
        print(f'Jucatorul {jucator_intrat} nu e pe banca de rezerve')
        print(f'mai ai inca  {3-schimbari_efectuate} schimbari')
    else:
        print(f'Jucatorul {jucator_schimbat} nu e in teren')
        print(f'mai ai inca  {3 - schimbari_efectuate} schimbari')
print('Ai folosit toate schimbarile')

# Exercitiu Dictionar roman-englez si englez-roman
rom_eng =  input('Introduceti tasta 1 pentru romana si tasta 2 pentru engleza: ')
cuvinte_romana = ['mama', 'tata']
cuvinte_engleza = ['mother', 'father']
while rom_eng != '1' and rom_eng != '2':
    print('Ati introdus un caracter diferit de 1 sau 2')
    rom_eng = input('Introduceti tasta 1 pentru romana si tasta 2 pentru engleza: ')
if rom_eng == '1':
    cuvant = input('Introduceti cuvantul in romana')
    if cuvant in cuvinte_romana:
        indx = cuvinte_romana.index(cuvant)
        print(cuvinte_engleza.index(indx))
    else:
        raspuns = input('Nu exista traducerea. Stii traducerea? yes/no')# # Ex1 afisaza date in functie de viteza masinii.
'''
daca se da de la tastatura viteza negativa afiseaza "viteza invalida"
daca avem 0  km/h afiseaza stationare
daca avem 50 km/h afiseaza locatitate
daca avem 90 km/h afiseaza drum european
daca avem peste 90 km/h afiseaza autostrada
'''
viteza = int(input('introdu viteza km/h'))
if viteza < 0:
    print('viteza invalida')
elif viteza == 0:
    print('masina stationeaza')
elif viteza <= 50:
    print('masina este in localitate')
elif viteza <=90:
    print('masina este pe un drum european')
else:
    print('masina este pe autostrada')

# Ex2 Afisaza date despre persoana in functie de varsta
'''
daca are sub 0 ani afiseaza nenascut
daca are intre 0 si 1 ani afiseza nou nascut
daca are intre 2 si 14 ani afiseza copil
daca are intre 15 si 17 ani afiseza adolescent
daca are peste 18 ani afiseaza adult
daca are peste 60 de ani afiseza batran
'''
varsta = int(input('scrie varsta'))
if varsta < 0 :
    print('nenascut')
elif varsta == 0:
    print('nou-nascut')
elif varsta == 1:
    print('nou-nascut')
elif varsta >= 2 and  varsta <= 14 :
    print('copil')
elif varsta <= 17:
    print('adolescent')
elif varsta >= 18 and varsta < 60:
    print('adult')
elif varsta >= 60 :
    print('batran')

# 4. Exercițiu:
'''
- citește un string de la tastatură (ex: alabala portocala);
- salvează primul caracter într-o variabilă - indiferent care este el;
- capitalizează acest caracter peste tot, mai puțin pentru primul și ultimul
caracter => alAbAlA portocAla.
'''
x = input('String')
text, xlow = x[1:-1], x.lower()
first, last = xlow[0], xlow[-1]
print(f"{first}{text.replace(first, first.upper())}{last}")

# Exerciții Opționale - grad de dificultate: Mediu spre greu(may need google) .
# 1. Ne imaginăm o echipă de fotbal pt teren sintetic.
# 3 Schimbări maxime admise:
# ● Declară o Listă cu 5 jucători
# ● Schimbari_efectuate = te joci tu cu valori diferite
# ● Schimbari_max = 3
# Dacă Jucătorul x e în teren și mai avem schimbări la dispoziție
# - Efectuează schimbarea
# - Șterge jucătorul scos din listă
# - Adaugă jucătorul intrat
# - Afișaza a intra x, a ieșit y, mai ai z schimbări
# Dacă jucătorul nu e în teren:
# - Afișază ‘ nu se poate efectua schimbarea deoarece jucătorul x nu e în
# teren’
# - Afișază ‘mai ai z schimbări
echipa = {'Raul', 'Dani', 'Ovi', 'Gabi', 'Alex'}
rezerve = {'Cristi','Bogdan','Tudor', 'Mircea'}
schimbari_efectuate = 0
schimbari_max = 3
while schimbari_efectuate < schimbari_max:
    jucator_schimbat = input('scoateti jucator: ')
    jucator_intrat = input('introduceti jucator: ')
    if  jucator_schimbat in echipa:
        echipa.remove(jucator_schimbat)
        rezerve.remove(jucator_intrat)
        echipa.add(jucator_intrat)
        schimbari_efectuate = schimbari_efectuate + 1
        print(echipa)
        print(f'A intrat jucatorul {jucator_intrat}, si a iesit {jucator_schimbat}, mai ai inca  {3-schimbari_efectuate} schimbari')
    elif jucator_intrat in rezerve:
        print(f'Jucatorul {jucator_intrat} nu e pe banca de rezerve')
        print(f'mai ai inca  {3-schimbari_efectuate} schimbari')
    else:
        print(f'Jucatorul {jucator_schimbat} nu e in teren')
        print(f'mai ai inca  {3 - schimbari_efectuate} schimbari')
print('Ai folosit toate schimbarile')

# Exercitiu Dictionar roman-englez si englez-roman

cuvinte_romana = ['mama', 'tata']
cuvinte_engleza = ['mother', 'father']
while True:
    rom_eng =  input('Introduceti tasta 1 pentru romana si tasta 2 pentru engleza: ')
    while rom_eng != '1' and rom_eng != '2':
        print('Ati introdus un caracter diferit de 1 sau 2')
        rom_eng = input('Introduceti tasta 1 pentru romana si tasta 2 pentru engleza: ')
    if rom_eng == '1':
        cuvant = input('Introduceti cuvantul in romana ')
        if cuvant in cuvinte_romana:
            indx = cuvinte_romana.index(cuvant)
            print(cuvinte_engleza[indx])
        else:
            raspuns = input('Nu exista traducerea. Stii traducerea? yes/no')
            if raspuns == 'yes':
                traducerea = input('Scrie-ti traducea')
                cuvinte_romana.append(cuvant)
                cuvinte_engleza.append(traducerea)
            else:
                print('nu exista traducerea')
    else:
        cuvant = input('Introduceti cuvantul in engleza ')
        if cuvant in cuvinte_engleza:
            indx = cuvinte_engleza.index(cuvant)
            print(cuvinte_romana[indx])
        else:
            raspuns = input('Nu exista traducerea. Stii traducerea? yes/no')
            if raspuns == 'yes':
                traducerea = input('Scrie-ti traducea')
                cuvinte_engleza.append(cuvant)
                cuvinte_romana.append(traducerea)
            else:
                print('nu exista traducerea')














