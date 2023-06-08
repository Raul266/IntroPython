#bloc_apartament
# atribute = suprafata ,utilitati
from abc import abstractmethod,ABC
class Apartament:
    suprafata_mp  = None
    utilitati = []

    def __init__(self, suprafata_mp):
        self.suprafata_mp = suprafata_mp
    def suprafata_ap(self):
        print(f'Ati achizitionat un ap cu suprafata de {self.suprafata_mp}mp')


class Utilitate:
    consum  = None

    @abstractmethod
    def get_consum(self):
        pass

    def set_consum(self,consum):
        self.consum = consum

class Apa(Utilitate):

    def get_consum(self):
        print(f'Ati comsumat {self.consum} litrii de apa')

class Gaz(Utilitate):

    def get_consum(self):
        print(f'Ati consuma {self.consum} Cm3 de gaz')

class Electiricitate(Utilitate):

    def get_consum(self):
        print(f'Ati consumat {self.consum} Vati')

# Am adaugat electiricitate la ap
apartament1 = Apartament(90)
apartament1.suprafata_ap()
electricitate = Electiricitate()
apartament1.utilitati.append(electricitate)
electricitate.set_consum(50)
electricitate.get_consum()

# Am adaugat Apa la ap
apa = Apa()
apartament1.utilitati.append(apa)
apa.set_consum(10)
apa.get_consum()

# Am adaugat Gaz la ap
gaz = Gaz()
apartament1.utilitati.append(gaz)
gaz.set_consum(30)
gaz.get_consum()
