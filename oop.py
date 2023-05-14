class PartyAnimal:
    x = 0
    def __init__(self):
        print('I am constructed')
    def party(self):
        self.x = self.x + 1
        print(self.x)
    def __del__(self):
        print('I am deconstructed')
an = PartyAnimal()
an.party()
an.party()
#print('Type', type(an))
#print('Dir', dir(an))

class Stiffler(PartyAnimal):
    def insult(self):
        print('Eat dick shitbreak')

ap = Stiffler()
ap.party()
ap.insult()