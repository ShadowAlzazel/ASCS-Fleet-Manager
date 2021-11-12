#a turn based combat game
from gameField.gameBoard import *
from random import randint

class turnCombatGame:
    Query = {'No': ['No', 'no', 'N', 'n'], 'Yes': ['Yes', 'yes', 'Y', 'y'], 
            'Inspect': ['I', 'Inspect', 'i', 'inspect', 'ins'], 'Skip': ['Skip', 'skip', 'S', 's'],
            'Move': ['Move', 'move', 'm', 'M'], 'End': ['End', 'end', 'finish', 'Finish', 'E', 'e'],
            'Attack': ['Attack', 'attack', 'atk', 'Atk', 'a', 'A', 'ATK'], 'AutoAttack': ['AutAttack', 'autoattack', 'auto', 'aa', 'AA']
            }

    def __init__(self, operationSpace):
        self.opsSpace = operationSpace
        self.gameShips = operationSpace.spaceEntities['shipObject']
        self.gameFleets = operationSpace.fleetEntities
        self.gameTurn = 0
        self.selectedHex = None 
        self.activeFleet = self.gameFleets[0]
        self.activeFleetIndex = 0
        for f in self.gameFleets:
            self._updateShips(f)     


    #fleet Actions
    def fleetTurn(self):
        self.selectedHex = None 
        q = self.activeFleetIndex
        if q == len(self.gameFleets) - 1:
            self.gameTurn += 1
            self.activeFleetIndex = 0
            self.activeFleet = self.gameFleets[0]
        else:
            self.activeFleetIndex += 1
            self.activeFleet = self.gameFleets[q + 1]

        self._updateShips(self.activeFleet)

    #update ships in fleet turn
    def _updateShips(self, aFleet):
        for s in aFleet.fleetShips:
            s.shipMovement = s.shipStats['SPD']
            s.shipAttacks = 1
            s.shipActive = True
            s.reloadGuns()

    #select shiphex
    def selectHex(self, aHex):
        if self.selectedHex:
            result = self._shipActions(aHex)
            if not result:
                self.selectedHex = None 
                self.selectHex(aHex)

        aShip = aHex.entity
        #can only select a ship
        if not aHex.empty and self.activeFleet.fleetCommand[0:3] == aShip.command[0:3]:
            self.selectedHex = aHex
            return True
        return False 
        
    #all availabe ship actions
    def _shipActions(self, aHex):
        result = False
        if not self.selectedHex.entity.shipActive:
            return False
        result = self._moveShipAction(aHex)        

        if not result:
            result = self._attackShipAction(aHex)

        return result

    #attack action; check for minimum  range, and guns in ranges
    def _attackShipAction(self, aHex):
        aShip = self.selectedHex.entity
        if not aShip.gunsReady():
            print("No guns loaded")
            return True

        #selected hex must be a target
        nearbyShipHexes = aShip.findTargets()
        if not aHex in nearbyShipHexes:
            print("Out of Target Range")
            return True

        result = self._shipSalvoAction(aShip, aHex.entity)
        return result


    #move ship on board
    def _moveShipAction(self, aHex):
        result = False
        if aHex.empty and (aHex in self.selectedHex.neighbors):
            selectedShip = self.selectedHex.entity
            if selectedShip.shipMovement != 0:
                result = self.opsSpace.moveClickEntity(selectedShip, aHex)
                if result:
                    selectedShip.shipMovement -= 1 
        return result


    #fire all guns in range 
    def _shipSalvoAction(self, aShip, bShip):
        shipExists = [bShip]
        #check if guns are loaded
        gunToFire = []
        for p in aShip.primaryBattery:
            if p.gunLoadTime == p.gunStats['RLD']:
                gunToFire.append(p)
        for s in aShip.secondaryBattery:
            if s.gunLoadTime == s.gunStats['RLD']:
                gunToFire.append(s)
        bEven = 0      
        for b in aShip.broadsideBattery:
            if b.gunLoadTime == b.gunStats['RLD'] and bEven % 2 == 0:
                gunToFire.append(b)
            elif bEven % 2 == 1:
                b.gunLoadTime = 0 #make half the boradside not reload 
            bEven += 1

        totalDamage = 0
        for g in gunToFire:
            if not shipExists:
                print("ship Destroyed!")
            salvoDamage = 0
            trueDamage = 0
            if aShip.gunInRange(g, bShip):
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
                g.gunLoadTime = 0

            totalDamage += trueDamage
            salvoDamage = 0

        print(aShip.vesselID, aShip.name, "Has done", totalDamage, "Total Damage to", bShip.vesselID, bShip.name)
        return True

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


