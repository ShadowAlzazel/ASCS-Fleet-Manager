#Energy Lasers
from shipClasses.shipEquipment.shipWeapons.weaponEntity import shipWeapon

#"""--<->----------------------------ENERGY-LASERS------------------------------<->--"""
#Energy Laser:
#charged and energized electromagnetic waves

class triple_L17_GammaRayLasers(shipWeapon):
    gun_name = 'Triple (L17) Gamma Ray Lasers'
    gun_stats = {
        "ATK": 468, "RLD": 1, "HIT": 93, "RNG": 1, "QNT": 3, "PEN": 0, "DIS": 2.5
    }
    def __init__(self, vessel_ID, battery_turret_number):
        super().__init__(vessel_ID, battery_turret_number)


class double_L13_XRayLasers(shipWeapon):
    gun_name = 'Double (L13) X-Ray Lasers'
    gun_stats = {
        "ATK": 303, "RLD": 1, "HIT": 94, "RNG": 1, "QNT": 2, "PEN": 0, "DIS": 2.5
    }
    def __init__(self, vessel_ID, battery_turret_number):
        super().__init__(vessel_ID, battery_turret_number)


class triple_L13_XRayLasers(shipWeapon):
    gun_name = 'Triple (L13) X-Ray Lasers'
    gun_stats = {
        "ATK": 303, "RLD": 1, "HIT": 94, "RNG": 1, "QNT": 3, "PEN": 0, "DIS": 2.5
    }
    def __init__(self, vessel_ID, battery_turret_number):
        super().__init__(vessel_ID, battery_turret_number)


class triple_L9_UltravioletLasers(shipWeapon):
    gun_name = 'Triple (L9) Ultraviolet Lasers'
    gun_stats = {
        "ATK": 191, "RLD": 1, "HIT": 96, "RNG": 1, "QNT": 3, "PEN": 0, "DIS": 2.5
    }
    def __init__(self, vessel_ID, battery_turret_number):
        super().__init__(vessel_ID, battery_turret_number)


class triple_L5_WaveLasers(shipWeapon):
    gun_name = 'Triple (L5) Wave Lasers'
    gun_stats = {
        "ATK": 64, "RLD": 1, "HIT": 97, "RNG": 1, "QNT": 3, "PEN": 0, "DIS": 2.5
    }
    def __init__(self, vessel_ID, battery_turret_number):
        super().__init__(vessel_ID, battery_turret_number)


class double_L5_WaveLasers(shipWeapon):
    gun_name = 'Double (L5) Wave Lasers'
    gun_stats = {
        "ATK": 64, "RLD": 1, "HIT": 97, "RNG": 1, "QNT": 2, "PEN": 0, "DIS": 2.5
    }
    def __init__(self, vessel_ID, battery_turret_number):
        super().__init__(vessel_ID, battery_turret_number)



