#ship proton colliders
from shipClasses.shipEquipment.shipWeapons.weaponEntity import shipWeapon


#"""--<->----------------------------PROTON-COLLIDERS------------------------------<->--"""
#smashes protons and neutrinos at a target using particle accelarators for destructive capabilities

class double_A12_ProtonColliders(shipWeapon):
    gun_name = 'Double (A12) Proton Colliders'
    gun_stats = {
        "ATK": 656, "RLD": 2, "HIT": 69, "RNG": 2, "QNT": 2, "PEN": 1, "DIS": 2
    }
    def __init__(self, vessel_ID, battery_turret_number):
        super().__init__(vessel_ID, battery_turret_number)


class triple_A12_ProtonColliders(shipWeapon):
    gun_name = 'Triple (A12) Proton Colliders'
    gun_stats = {
        "ATK": 656, "RLD": 2, "HIT": 69, "RNG": 2, "QNT": 3, "PEN": 1, "DIS": 2
    }
    def __init__(self, vessel_ID, battery_turret_number):
        super().__init__(vessel_ID, battery_turret_number)