class Weapon:
    created = 0

    def __init__(self, name, tier, type):
        self.name = name
        self.tier = tier
        self.type = type
        Weapon.created += 1

    def increase_tier(self, tier):
        self.tier = tier

    def __repr__(self):
        return f"{self.name} is of type {self.tier}"


class Build:
    def __init__(self):
        self.build = {
            "katana": None, "ranged": None, "charm": None, "ghost-weapon-1": None, "ghost-weapon-2": None
        }

    def change_gear(self, weapon):
        self.build[weapon.type.lower()] = weapon
   

class Character(Build):
    def __init__(self, class_name):
        super().__init__()  
        self.class_name = class_name

    def show_build(self):
        print(f"{self.class_name} class with gear: {self.build}")


assassin = Character("Assassin")

assassin.show_build()

katana = Weapon("Wind Katana", "Rare", "Katana")
charm = Weapon("Assassin Charm", "Epic", "Charm")

assassin.change_gear(katana)
assassin.change_gear(charm)

assassin.show_build()







