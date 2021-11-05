from shipGacha import *
from combatSpaceHex import *
from shipCombat import ACombatGame


gameShipLib = []
gachaShip(gameShipLib)
gachaShip(gameShipLib)
#gameShipLib[0].fullInspect()
#g1 = ACombatGame(30, gameShipLib[0], gameShipLib[1])
#print(g1.combatLib)
#g1.testCombatGame()
#g1.timedCombatGame()


aoe = operationSpace(5, 6)

aoe.addEntity(aoe.starSpaceHexes[12], gameShipLib[0])
aoe.entities[0].placeSpace.coord
print(aoe.entities[0].name, "At Hex", aoe.entities[0].placeSpace.coord['o'])
aoe.moveEntity(gameShipLib[0], 'UR')
