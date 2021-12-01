#Realm Distorters
from shipClasses.shipEquipment.shipWeapons.weaponEntity import shipWeapon


#"""--<->----------------------------REALM-DISTORTERS------------------------------<->--"""
#uses warp technology to create sinusodial space-time waves that distort matter

class double_A8_RealmDistorter(shipWeapon):
    gunName = 'Double (A8) Realm Distorter'
    gunStats = {
        "ATK": 279, "RLD": 3, "HIT": 79, "RNG": 2, "QNT": 2, "PEN": 0, "DIS": -1
    }
    def __init__(self, vesselID, batteryNumber):
        super().__init__(vesselID, batteryNumber)