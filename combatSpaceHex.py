#Started 11/4/2021 

class operationSpace:

    def __init__(self, length, width):
        n = 0
        self.l = length
        self.w = width
        self.starSpaceHexes = []
        self.entities = []

        for x in range(0, self.l * self.w):
            self.starSpaceHexes.append(starSpace(n))
            n += 1


    def addEntity(self, aStarSpace, newEntity):
        newEntity.placeSpace = aStarSpace
        aStarSpace.entity = newEntity
        self.entities.append(newEntity)


    def moveEntity(self, movingEntity, direction):
        uR = ['UR', 'ur', 'uR']
        uL = ['UL', 'ul', 'uL']
        dR = ['DR', 'dr', 'dR']
        dL = ['DL', 'dl', 'dL']
        tR = ['TR', 'tr', 'tR', 'R', 'r']
        tL = ['tL', 'tl', 'tL', 'L', 'l']

        curHexCoord = movingEntity.placeSpace.coord['o']

        if direction in tR:
            if (curHexCoord + 1) % self.l == 0:
                print("Cannot move Right! At right border!")
            else:
                self.moveLocation(movingEntity, 'Right')

        elif direction in tL:
            if (curHexCoord) % self.l == 0:
                print("Cannot move Left! At left border!")
            else:
                self.moveLocation(movingEntity, 'Left')

        elif direction in uR:
            if (curHexCoord) >= self.l * (self.w - 1):
                print("Cannot move Up-Right! At top border!")
            elif (curHexCoord // self.l) % 2 == 1 and (curHexCoord + 1) % self.l == 0:
                print("Cannot move Up-Right! Even Rank Border Hex!")
            else:
                self.moveLocation(movingEntity, 'UpRight')

        elif direction in uL:
            if (curHexCoord) >= self.l * (self.w - 1):
                print("Cannot move Up-Left! At top border!")   
            elif (curHexCoord // self.l) % 2 == 0 and curHexCoord % self.l == 0:
                print("Cannot move Up-Left! Odd Rank Border Hex!")  
            else:
                self.moveLocation(movingEntity, 'UpLeft') 

        elif direction in dR:
            if (curHexCoord) // self.l == 0:
                print("Cannot move Down! At bottom border!")
            elif (curHexCoord // self.l) % 2 == 1 and (curHexCoord + 1) % self.l == 0:
                print("Cannot move Down-Right! Even Rank Border Hex!")
            else:
                self.moveLocation(movingEntity, 'DownRight')

        elif direction in dL: 
            if (curHexCoord) // self.l == 0:
                print("Cannot move Down! At bottom border!")
            elif (curHexCoord // self.l) % 2 == 0 and curHexCoord % self.l == 0:
                print("Cannot move Down-Left! Odd Rank Border Hex")
            else: 
                self.moveLocation(movingEntity, 'DownLeft')
        else:
            print("Directions Unknown")


    def moveLocation(self, movingE, vector):
        oldHexCoord = movingE.placeSpace.coord['o']
        hexMoves = {'Right': 1, 
                    'Left': -1, 
                    'UpRight': (((oldHexCoord // self.l) % 2) + self.l),
                    'UpLeft': ((((oldHexCoord // self.l) % 2) + self.l) - 1),
                    'DownRight': (((oldHexCoord // self.l) % 2) - self.l),
                    'DownLeft': ((((-(oldHexCoord // self.l) % 2)) - self.l) - 1)
                    }
        print("Moving From Space Hex:", oldHexCoord, end=' ') 
        movingE.placeSpace = self.starSpaceHexes[oldHexCoord + hexMoves[vector]]
        self.starSpaceHexes[oldHexCoord + hexMoves[vector]].entity = movingE
        self.starSpaceHexes[oldHexCoord].entity = []
        print("To Space Hex", movingE.placeSpace.coord['o'])


class starSpace:

    def __init__(self, order):
        self.coord = {'o': order}
        self.entity = []
