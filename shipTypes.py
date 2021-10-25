#Started 10/23/2021

class Ship:
    ammount = 0
    shiptype = 'CIV'
    shields = 100
    hull = 100

    def __init__(self, hullnumber, name):
        self.command = 'ASCS'
        self.name = name
        self.hullnumber = hullnumber

        print("New Ship Launched", end=': ')
        print(self.command, '-', name, sep='', end=', ')
        Ship.ammount += 1

    def inspect(self):
        print(self.command,'-' , self.name, sep='', end=', ')
        print(self.shiptype, '-', self.hullnumber,':', sep='')
        print("FP:", self.FP, " EVA:", self.EVA, " SPD:",  self.SPD, " Armor:", self.Armor, sep='')
        print("Shield Capcity at", "%.2f%%" % (self.shields / self.__class__.shields * 100.0))
        print("Hull Integrity at", "%.2f%%" % (self.hull / self.__class__.hull * 100.0))
        print("-<->--------------------------------------<->-")



#Battleships
class Battleship(Ship):
    ammount = 0
    shiptype = 'BB'

    EVA = 30
    SPD = 25
    FP = 300
    Armor = 5 #Superheavy
    shields = 10000 
    hull = 10000

    def __init__(self, hullnumber, name):
        super().__init__(hullnumber, name)

        print(self.shiptype, '-', hullnumber, sep='')
        Battleship.ammount += 1

    def self_repair(self):
        self.hull = self.__class__.hull
        print(self.name, "Repaired!")
