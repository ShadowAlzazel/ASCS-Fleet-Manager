from shipGacha import *
from combatSpaceSquares import *
from shipCombat import ACombatGame


gameShipLib = []
gachaShip(gameShipLib)
gachaShip(gameShipLib)
#gameShipLib[0].fullInspect()
#g1 = ACombatGame(30, gameShipLib[0], gameShipLib[1])
#print(g1.combatLib)
#g1.testCombatGame()
#g1.timedCombatGame()


aoe = operationSpace(8, 3)

aoe.addEntity(aoe.starSpaces[10], gameShipLib[0])
aoe.addEntity(aoe.starSpaces[9], gameShipLib[1])
#print(aoe.entities)

#aoe.entities[0].moveShip['up']
aoe.entities[0].spacePlace.coord
#aoe.move(aoe.entities[0], 'L')