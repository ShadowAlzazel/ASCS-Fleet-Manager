#Arc Throwers
from shipClasses.shipEquipment.shipWeapons.weaponEntity import shipWeapon

#"""--<->----------------------------Arc-Throwers------------------------------<->--"""
#Arc-Throwers:
#HAT3 Arc-Thrower A15-20 '(Hyper Array of Trasnformers with Exremely Energized Electrons)'

class double_A17_HAT3ArcThrowers(shipWeapon):
    gunName = 'Double (A17) HAT3 Arc-Throwers'
    gunStats = {
        "ATK": 529 * 2, "RLD": 3, "HIT": 51, "RNG": 2
    }
    def __init__(self, vesselID, batteryNumber):
        super().__init__(vesselID, batteryNumber)


class triple_A17_HAT3ArcThrowers(shipWeapon):
    gunName = 'Triple (A17) HAT3 Arc-Throwers'
    gunStats = {
        "ATK": 529 * 3, "RLD": 3, "HIT": 51, "RNG": 2
    }
    def __init__(self, vesselID, batteryNumber):
        super().__init__(vesselID, batteryNumber)


class triple_A11_TeslaArcThrowers(shipWeapon):
    gunName = 'Triple (A11) Tesla Arc-Throwers'
    gunStats = {
        "ATK": 297 * 3, "RLD": 3, "HIT": 51, "RNG": 2
    }
    def __init__(self, vesselID, batteryNumber):
        super().__init__(vesselID, batteryNumber)


class double_A8_AmplifiedArcThrowers(shipWeapon):
    
    gunStats = {
        "ATK": 237 * 2, "RLD": 2, "HIT": 51, "RNG": 1
    }
    def __init__(self, vesselID, batteryNumber):
        super().__init__(vesselID, batteryNumber)  


class double_A5_ArcThrowers(shipWeapon):
    gunName = 'Double (A5) Arc-Throwers'
    gunStats = {
        "ATK": 177 * 2, "RLD": 2, "HIT": 51, "RNG": 1
    }
    def __init__(self, vesselID, batteryNumber):
        super().__init__(vesselID, batteryNumber)
