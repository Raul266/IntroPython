def printGreeeting():
    print('Buna ziua!Bine ati venit!')
def printGreetingByName(nume, prenume):
    print(f'Buna ziua {nume} {prenume}')
def mediaNr(a, b, c):
    return (a+b+c)/3
def piValue():
    return 3.14

#exerciutiu
#daca persoana este majora, altfel false
def verificareMajor(varsta):
    if varsta >= 18:
        return True
    else:
        return False

# zona de apelare (desktop)
printGreeeting()
printGreeeting()
printGreetingByName('Albus' , 'Raul')
printGreetingByName('Albus' , 'Simona')
printGreetingByName('Albus' , 'Ion')
print(mediaNr(3,3,4))
print(piValue())
print(verificareMajor(18))

#prima data se ia varsta utilizatorului
age = int(input('introduceti varsta dvs'))
if verificareMajor(age):
    print('cont creat.bine ai venit in aplicatie')
else:
    print('nu ai varsta minima necesara (18) pt a paria')

