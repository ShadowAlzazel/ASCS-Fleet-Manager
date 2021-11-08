#a turn based combat game
from random import randint

class turnCombatGame:
    Query = {'No': ['No', 'no', 'N', 'n'], 'Yes': ['Yes', 'yes', 'Y', 'y'], 
                'Inspect': ['I', 'Inspect', 'i', 'inspect', 'ins'], 'Skip': ['Skip', 'skip', 'S', 's'],
                'Move': ['Move', 'move', 'm', 'M'], 'End': ['End', 'end', 'finish', 'Finish', 'E', 'e'],
                'Attack': ['Attack', 'attack', 'atk', 'Atk', 'a', 'A', 'ATK'], 'AutoAttack': ['AutAttack', 'autoattack', 'auto', 'aa', 'AA']}

    def __init__(self, operationSpace):
        self.gameSpace = operationSpace
        self.ships = operationSpace.spaceEntities['shipObject']
        self.turn = 0


    #hit calculator for a gun
    def gunHitCalc(self, gunBattery, aShipACC, bShipEVA):
        hitRate = (aShipACC - bShipEVA) + gunBattery.gunStats['HIT']
        randHit = randint(1, 100)
        if hitRate > randHit:
            return True
        else:
            return False

    #damage calculator for a gun
    def gunDamageCalc(self, gunBattery, aShipFP, aShipLuck, bShipLuck, batDistro):
        critRate = aShipLuck - bShipLuck + 5
        damageMult = 1
        damage = 0
        randCrit = randint(1, 100)
        if critRate > randCrit:
            damageMult = 1.25 + (aShipLuck / 100)

        damage = (gunBattery.gunStats['ATK'] + (aShipFP // batDistro) * damageMult)
        return damage


    #all availabe ship action query 
    def shipActions(self, aShip):
        shipturnActive = True
        shipMovement = aShip.shipStats['SPD']
        shipAttacks = 1
        aShip.reloadGuns()

        while shipturnActive:    
            mes = aShip.vesselID + ' ' + aShip.name +  ' ' + "Awaiting Orders...: "
            playerInput = input(mes)

            if playerInput in self.Query['Skip']:
                print("Ship Skipped! ")
                shipturnActive = False
                return

            elif playerInput in self.Query['Move']:
                if shipMovement != 0:
                    if self.moveShipAction(aShip):
                        shipMovement -= 1
                else: 
                    print("No More Moves Available")

            elif playerInput in self.Query['Attack']:
                if shipAttacks != 0:
                    if self.attackShipAction(aShip):
                        shipAttacks -= 1
                else: 
                    print('No Attacks Available')

            elif playerInput in self.Query['AutoAttack']:
                print("AutoAttack")

    #attack action; check for minimum  range, and guns in ranges
    def attackShipAction(self, aShip):
        nID = 0
        if not aShip.gunsReady():
            print("No guns loaded")
            return True

        nearbyShips = aShip.findTargets()
        if not nearbyShips:
            print("No ships in minimmum range")
            return False 
        else: 
            for k in nearbyShips:
                print("Targets within minimmum range:", k.entity.vesselID, k.entity.name, "At Hex", k.coord['hexNum'], 'TiD:', nID)
                nID += 1


        newOrder = input("Choose target to fire?")
        if newOrder in self.Query['No']:
            return False

        #attack input target and end attacks
        newOrder = int(newOrder)
        if newOrder <= nID:
            self.shipSalvoAction(aShip, nearbyShips[newOrder].entity)
            #return True 

    #move ship on board
    def moveShipAction(self, aShip):
        x = self.gameSpace.moveEntity(aShip, input("Direction needed: "))
        return x


    #fire all guns in range 
    def shipSalvoAction(self, aShip, bShip):
        #check if guns are loaded
        gunToFire = []
        for p in aShip.primaryBattery:
            if p.reloadTurn == p.gunStats['RLD']:
                gunToFire.append(p)
        for s in aShip.secondaryBattery:
            if s.reloadTurn == s.gunStats['RLD']:
                gunToFire.append(s)
        bEven = 0      
        for b in aShip.broadsideBattery:
            if b.reloadTurn == b.gunStats['RLD'] and bEven % 2 == 0:
                gunToFire.append(b)
            bEven += 1

        totalDamage = 0
        for g in gunToFire:
            salvoDamage = 0
            trueDamage = 0
            if aShip.gunInRange(g):
                batPow = 0  
                if g in aShip.primaryBattery:
                    batPow = aShip.shipStats['FP'] // len(aShip.primaryBattery)
                elif g in aShip.secondaryBattery:
                    batPow = aShip.shipStats['FP'] // len(aShip.secondaryBattery)
                elif g in aShip.broadsideBattery:
                    batPow = aShip.shipStats['FP'] // len(aShip.broadsideBattery)

                if self.gunHitCalc(g, aShip.shipStats['ACC'], bShip.shipStats['EVA']) == True:
                    salvoDamage += self.gunDamageCalc(g, aShip.shipStats['FP'], aShip.shipStats['LCK'], bShip.shipStats['LCK'], batPow)

                trueDamage = bShip.takeDamage(salvoDamage)
                if trueDamage > 0:
                    print(g.batteryID, "Has Hit", bShip.name, "For", trueDamage, "Damage!")
                g.reloadTurn = 0

            totalDamage += trueDamage
            salvoDamage = 0

        print(aShip.vesselID, aShip.name, "Has done", totalDamage, "Total Damage to", bShip.vesselID, bShip.name)


    def runTurn(self):
        for x in self.ships:
            self.shipActions(x)


    def runGame(self):
        gameRunning = True
        while gameRunning:
            self.runTurn()
            play = input("Continue?: ")
            if play in self.Query['No']:
                gameRunning = False
            else:
                self.turn += 1
