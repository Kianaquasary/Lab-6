# Косарпур Киана - 344494 -  Вариант 4

class Rifle:
    def __init__(self, _magazineRound, _fireRate, _fireRange):
        self.magazineRound = _magazineRound
        self.fireRate = _fireRate
        self.fireRange = _fireRange

    def FireRate(self):   
        delay = self.magazineRound / self.fireRate * 60
        return round(delay, 1)   

    def FireRange(self):   
        dif = self.fireRate / self.fireRange
        return round(dif, 2) 


class Avtomat(Rifle):  
    def __init__(self, _magazineRound=30, _fireRate=600 , _fireRange=300 ):
        self.magazineRound = _magazineRound
        self.fireRate = _fireRate
        self.fireRange = _fireRange
        super().__init__(self.magazineRound, self.fireRate, self.fireRange)
        self.delay = super().FireRate()
        self.dif = super().FireRange()

    def reload(self, _bullets):  
        self.magazineRound += _bullets
        super().__init__(self.magazineRound, self.fireRate, self.fireRange)
        self.delay = super().FireRate()
        print("Time to empty the weapon's magazine:", self.delay)
    def print(self):
        print("The magazine of AK-47 rifle will be empty in", self.delay, " seconds")
        print("Ratio of fire rate to firing range: ", self.dif)
 
class Sniper(Rifle):  
    def __init__(self, _magazineRound=10, _fireRate=35 , _fireRange=1200 ):
        self.magazineRound = _magazineRound
        self.fireRate = _fireRate
        self.fireRange = _fireRange
        super().__init__(self.magazineRound, self.fireRate, self.fireRange)
        self.delay = super().FireRate()
        self.dif = super().FireRange()

    def reload(self, _bullets):  
        self.magazineRound += _bullets
        super().__init__(self.magazineRound, self.fireRate, self.fireRange)
        self.delay = super().FireRate()
        print("Time to empty the weapon's magazine:", self.delay)
    def print(self):
        print("The magazine of SVD rifle will be empty in", self.delay, " seconds")
        print("Ratio of fire rate to firing range: ", self.dif)



ak47 = Avtomat()
ak47.print()
ak47.reload(60)


print("********************")
    
SVD = Sniper()
SVD.print()
SVD.reload(10)