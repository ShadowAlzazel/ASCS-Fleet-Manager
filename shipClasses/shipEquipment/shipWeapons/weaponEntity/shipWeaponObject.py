#RNG in km
#RLD in Seconds
#M, L, A, denote the guns radius in inches
#All batteries designed for a single case

class shipWeapon:

    def __init__(self, vesselID, turretDesignation):
        self.batteryID = '-'.join([vesselID, turretDesignation])
        self.reloadTurn = 100 #preloaded

    def reloadGun(self):
        if self.reloadTurn < self.gunStats['RLD']:
            self.reloadTurn += 1
        else: 
            self.reloadTurn = self.gunStats['RLD']
