class Weapon:
    
    created = 0
    
    def __init__(self, name, tier, type):
        self.name = name
        self.tier = tier
        self.type = type
        Weapon.created = Weapon.created + 1
   
   
    def increase_tier(self, tier):
        self.tier = tier
        
    def __repr__(self):
        return f"Weapon {self.name} is of type {self.tier}"
       

class Build:
    def __init__(self):
        self.build = {"katana": None, "ranged": None, "charm": None, "ghost-weapon-1": None, "ghost-weapon-2": None}
        
    def change_gear(self, weapon):
        self.build[weapon.type.lower()] = weapon
        
        
    
assassin = Build()
print(assassin.build)
weapon1 = Weapon("Wind Katana", "Rare", "Katana")
assassin.change_gear(weapon1)
print(assassin.build)







