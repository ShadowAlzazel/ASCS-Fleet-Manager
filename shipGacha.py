#Started 10/29/21

import json
import sys
from random import randint
from shipClasses import *

with open("sortedShipNames.json", "r") as sortedShipNamesFile:
    sortedShipNames = json.load(sortedShipNamesFile)

with open("currentShipClasses.json", "r") as currentShipClassesFile:
    currentShipClasses = json.load(currentShipClassesFile)

nameOrigins = ['IJN', 'KMS', 'HMS', 'FFNF', 'USS']   #name from a historical origin
nameTypes = ['CVA', 'BB', 'BC', 'CS', 'CA', 'CVL', 'CL', 'DD']   #name from ship type
currentTypes = ['BB', 'BC', 'CS', 'CA', 'DD']  #current available ship types

#turn string into available class
def getClass(strShipClass):
    return getattr(sys.modules[__name__], strShipClass)


#Get random name from json file
def randShipName():
    x = nameOrigins[randint(0, len(nameOrigins) - 1)]
    y = nameTypes[randint(0, len(nameTypes) - 1)]
    q = randint(0, len(sortedShipNames[0][x][y]) - 1)

    rName = sortedShipNames[0][x][y][q]
    return rName


#Get random ship Class from json file
def randShipClass():
    x = currentTypes[randint(0, len(currentTypes) - 1)]
    q = randint(0, len(currentShipClasses[0][x]) - 1)

    rClass = currentShipClasses[0][x][q]
    return rClass


#random stat generator
def randShipStats(aShip):
    aShip.shipStats['FP'] += (randint(-5, 5))
    aShip.shipStats['ACC'] += (randint(-2, 2))
    aShip.shipStats['EVA'] += (randint(-2, 2))
    aShip.shipStats['SPD'] += (randint(-2, 2))
    aShip.shipStats['luck'] += (randint(-1, 1))


#create a ship with random stats
def gachaShip(givenLib):
    randPenantNum = randint(1, 10000)
    l = len(givenLib)

    gachaClass = getClass(randShipClass())
    aGachaShip = gachaClass(randPenantNum, randShipName())
    givenLib.append(aGachaShip)
    randShipStats(givenLib[l])


#Create a specific ship
def buildShip(givenLib, f ,g, rS = False):
    assert f in nameOrigins
    assert g in nameTypes 
    randPenantNum = randint(1, 10000)
    h = randint(0, len(sortedShipNames[0][f][g]) - 1)
    l = len(givenLib)

    gachaClass = getClass(randShipClass())
    buildShip = gachaClass(randPenantNum, sortedShipNames[0][f][g][h])
    givenLib.append(buildShip)
    if rS == True:
        randShipStats(givenLib[l])


def gachaOrder(aLib):
    x = input("Enter 'Gacha' for a Random Pull, Else enter 'Build':")
    if x == 'Gacha' or x == 'gacha':
        gachaShip(aLib)
    elif x == 'Build' or x == 'build':
        u = input("Enter an available Faction from:", nameOrigins)
        v = input("Enter an availabe ship type from:", nameTypes)
        r = input("Allow for random stats? Enter T or F:")   
        if r == 'True' or r == 'T':
            r = True
        else: 
            r = False  
        buildShip(aLib, u, v, r)
    else:
        print("Order failed. Try again.")
    
    aLib[-1].fullInspect()


#ShipLib2 = []

#buildShip(ShipLib2, 'IJN', 'CA')
#gachaOrder(ShipLib2)
#gachaShip(ShipLib2)
#ShipLib2[-1].fullInspect()
