#Started 11/3/2021

class operationSpace:

    def __init__(self, l, w):
        n = 0
        self.l = l
        self.w = w
        self.starSpaces = []
        self.entities = []
        for y in range(0, w):
            for x in range(0, l):
                self.starSpaces.append(starSpace(x, y, n))
                n += 1  

    
    def addEntity(self, aStarPlace, newEntity):
        newEntity.spacePlace = aStarPlace 
        aStarPlace.entity = newEntity
        self.entities.append(newEntity)


    #takes in an object to move
    def move(self, movingEntity, d):
        up = ['UP', 'up', 'Up', 'u', 'U']
        right = ['RIGHT', 'Right', 'right', 'r', 'R']
        left = ['LEFT', 'Left', 'left', 'l', 'L']
        down = ['DOWN', 'Down', 'down', 'd', 'D']

        if d in up: 
            if movingEntity.spacePlace.coord['y'] == self.w - 1:
                print("At Top Border!")
            #elif len(self.starSpaces[movingEntity.spacePlace.coord['p'] + self.l].entity) > 1:
            #    print("Space Full!")
            else:
                self.mover(movingEntity, 'Up')

        elif d in right:
            if movingEntity.spacePlace.coord['x'] == self.l - 1:
                print("At Right Border!")
            #elif len(self.starSpaces[movingEntity.spacePlace.coord['p'] + 1].entity) > 1:
            #    print("Space Full!")
            else: 
                self.mover(movingEntity, 'Right')

        elif d in down:
            if movingEntity.spacePlace.coord['y'] == 0:
                print("At Bottom Border!")
            #elif len(self.starSpaces[movingEntity.spacePlace.coord['p'] - self.l].entity) > 1:
            #    print("Space Full!")
            else:
                self.mover(movingEntity, 'Down')

        elif d in left:
            if movingEntity.spacePlace.coord['x'] == 0:
                print("At Left Border!")
            #elif len(self.starSpaces[movingEntity.spacePlace.coord['p'] - 1].entity) > 1:
            #    print("Space Full!")
            else:
                self.mover(movingEntity, 'Left')
        else:
            print("Command Unaccertainable")
                      

    def mover(self, movingE, k):
        vectors = {'Up': self.l, 'Right': 1, 'Down': -(self.l), 'Left': -1}
        oldCoord = movingE.spacePlace.coord['p']
        movingE.spacePlace = self.starSpaces[oldCoord + vectors[k]]
        self.starSpaces[oldCoord + vectors[k]].entity = movingE
        self.starSpaces[oldCoord].entity = []


class starSpace: 
    
    def __init__(self, x, y, p):
        self.coord = {'x': x, 'y': y, 'p': p}
        self.entity = []

