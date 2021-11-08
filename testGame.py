import createTestShips
from spaceField import *
from shipCombat import turnCombatGame

gameShipLib = []
def createShips(someShipLib, n):
    while n > 0:
        createTestShips.gachaRandShip(someShipLib)
        n -= 1

createShips(gameShipLib, 3)
gameShipLib[0].fullInspect()

#aoe = createCombatSpace(10, 10, 10)   
#print(aoe.hexesFull)

#aGame = ACombatGame(30, gameShipLib[0], gameShipLib[1])
#aGame.testCombatGame()
#aGame.timedCombatGame()

aoe = createCombatSpace(10, 10, 0)
aoe.addCustomEntity(aoe.starSpaceHexes[0], gameShipLib[0])
aoe.addCustomEntity(aoe.starSpaceHexes[40], gameShipLib[1])
aoe.addCustomEntity(aoe.starSpaceHexes[22], gameShipLib[2])

s0 = gameShipLib[0]
s1 = gameShipLib[1]
s2 = gameShipLib[2]
s1.command = 'ERIC'

#t1 = s1.findTargets()
#print(t1[0].entity.vesselID)
#print(len(aoe.starSpaceHexes))

makeGameBoard(aoe)
civ = turnCombatGame(aoe)
civ.runGame()

#aoe.addCustomEntity(aoe.starSpaceHexes[6], gameShipLib[1])
#print(aoe.spaceEntities['spaceObject'][0].name, "At Hex", aoe.spaceEntities['spaceObject'][0].placeSpace.coord['hexNum'])
#print(aoe.spaceEntities['spaceObject'][1].name, "At Hex", aoe.spaceEntities['spaceObject'][1].placeSpace.coord['hexNum'])
#aoe.moveEntity(gameShipLib[0], 'UL')
#sas