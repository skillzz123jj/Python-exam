



class Weapon:
    
    created = 0
    
    def __init__(self, name, tier):
        self.name = name
        self.tier = tier
        Weapon.created = Weapon.created + 1
   
   
    def increase_tier(self, tier):
        self.tier = tier
       

weapon1 = Weapon("Wind Katana", "Rare")
print(f"Weapon: {weapon1.name}, Tier: {weapon1.tier}")
print(f"Weapons created: {Weapon.created}")

weapon2 = Weapon("Magma Bomb", "Legendary")
print(f"Weapon: {weapon2.name}, Tier: {weapon2.tier}")
print(f"Weapons created: {Weapon.created}")

weapon1.increase_tier("Epic")
print(f"Weapon: {weapon1.name}, Tier: {weapon1.tier}")




