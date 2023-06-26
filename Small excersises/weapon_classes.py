# -*- coding: utf-8 -*-

# superclass
class Weapon:
    # constructor method: this class has these attributes:
    def __init__(self, name, damage, speed, weight):
        #attributes
        self.name = name
        self.damage = damage
        self.speed = speed
        self.weight = weight
    
    # methods
    def swing(self):
        print(f"Weapon {self.name} swings for {self.damage} with speed {self.speed}")
    def drop(self):
        print(f"Weapon {self.name} is removed from inventory. Weight reduced by {self.weight}")
    
# subclass
class Blunt_Wep(Weapon):
    def __init__(self, name, damage, speed, weight, crushing_dmg):
        # calling the superclass
        super().__init__(name, damage, speed, weight)
        self.crushing_dmg = crushing_dmg
    
    # modify parent's swing method to include crushing damage
    def swing(self):
        print(f"Weapon {self.name} swings for {self.damage} and crushing damage {self.crushing_dmg} with speed {self.speed}")

# Object / instance of class
Excalibur = Weapon("Excalibur", 30, 5, 7)
Morning_Star = Blunt_Wep('Morning Star', 50, 2, 15, 10)
Excalibur.swing()
Morning_Star.swing()
Morning_Star.drop()
print(Morning_Star.crushing_dmg)

# del Morning_Star
# Morning_Star.swing()