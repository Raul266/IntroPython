# # Classe
#  EX 1 ROBOT
import math
class Robot:
    garantie = 10
    number_of_robot = 0
    def __init__(self,nume, serial_number, hardwere,softwere,age,sleep):
        self.nume = nume
        self.serial_number = serial_number
        self.hardwere = hardwere
        self.softwere = softwere
        self.sleep = sleep
        self.age = age
        Robot.number_of_robot+=1

    def turn_on(self):
        if self.sleep == False:
            return f'{self.nume}  is already running'
        else:
            self.sleep = False
            return f'{self.nume} turned on'
        
    def end_of_life(self):
        if self.age > self.garantie:
            print(f'{self.nume} depasit perioada de garantie')
        else:
            print(f'{self.nume} mai are inca {self.garantie-self.age} ani de garantie')

    @classmethod # constructori alternativi, cand vrem sa creem o clasa
    def schimbare_garantie(cls,ani):
        cls.garantie = ani

    @classmethod
    def from_list(cls,lst): #aici este o conventie daca alegem elem din lista scriem from_list daca luam stringuri from_str
        nume, serial_number, hardwere, softwere, age, sleep = lst
        return cls(nume,serial_number,hardwere,softwere,age,sleep)

    # cu ajutorul acestei functii aflam dimensiunile cercului in funcrie de raza
    @staticmethod # o functie obisnuita doar ca se afla in interiorul unei clase (nu primeste nici self nici cls)
    def dimensiuni_cerc_circumferinta_aria(raza):
        return 2*math.pi*raza , math.pi*raza**2

class Aspirator(Robot):
    garantie = 15
    def __init__(self, nume, serial_number, hardwere, softwere, age,sleep,power):
        super().__init__(self, nume, serial_number, hardwere, softwere, age,sleep)
        self.power = power

r1 = Robot('John','12333','i5','python',11,True)
r2 = Robot('Marc','12344','i5','C++',3,True)
a1 = Aspirator('George','43333', 'i5', 'C++',3 , True,'1kw')
print(a1.nume)
print(a1.garantie)
print(r1.garantie)
print(Robot.garantie)
print(r1.garantie)
print(r1.__dict__)
print(Robot.__dict__)
print(r1.serial_number)
print(r1.sleep)
print(r1.turn_on())
print(r1.sleep)
print(r1.end_of_life())
print(r2.end_of_life())
Robot.schimbare_garantie(5)
print(r1.garantie)
print(r2.garantie)

robot_attributes = ['Mike','44444','i5','Java',2,True]
nume, serial_number , hardwere,softwere,age,sleep = robot_attributes
r3 = Robot(nume, serial_number , hardwere,softwere,age,sleep)
print(r3.nume)
r4 = Robot.from_list(robot_attributes) # aici am preluat atributele cu ajutorul functiei/metodei from_list
print(r4.nume)
print(Robot.dimensiuni_cerc_circumferinta_aria(10))




# EX 2 Angajat
class Angajat:
    def __init__(self,nume, prenume, post,salariu, vechime):
        self.nume = nume
        self.prenume = prenume
        self.post = post
        self.salariu = salariu
        self.vechime = vechime
    def marire_salariu_dupa_vechime(self):
        if self.vechime >= 3:
            self.salariu = self.salariu + 1000
            print(f'Salariul dv a fost marit cu 1000 de lei acum este {self.salariu} lei')
angajat = Angajat('Matei','Andrei','Tehnician',10000,3)
print(angajat.salariu)
angajat.marire_salariu_dupa_vechime()
print(angajat.salariu)

