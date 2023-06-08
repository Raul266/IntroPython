#if
piesa_faina = False
print('pornim radio')
if piesa_faina== True:
    print ('dam mai tare')
    print ('fredonam')
print('oprim radio')

# if else
# daca numarul este par printam acest lucru
# altfel printam impar
nr = 4
# ce inseamna par? adica se imparte exact la 2
# ce inseamna ca se imparte exact la 2? ne da restul 0
if nr % 2 == 0:
    print('nr par')
else:
    print('impar')

# este un nr pozitiv?
if (nr > 0):
    print('pozitiv')
else:
    print('nr este pozitiv')
# tema daca utilizatorul are sub 18 ani nu poate paria altfel poate!
varsta = int(input('introdu varsta'))
if varsta < 18:
    print('minorii nu pot paria')
else:
    print('te-ai inregistrat cu suces')
# if, else if, else
# cum ne saluta robotelul in functie de ora

ora = int(input('introdu ora'))#luam date de la tastatura ne asiguram ca am transformat string in int
if ora < 0:
    print('Ora invalida. Ora negativa')
elif ora<=11:
    print('Buna dimineata')
elif ora<=18:
    print('Buna ziua')
elif ora<=21:
    print('Buna seara')
elif ora <=24:
    print('Noapte buna')
else:
    print('Ora invalida. Ora prea mare')
