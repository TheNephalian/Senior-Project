import random
class Player():
    def __init__(self):
        self.name = "Dummy"
        self.lvl = 1
        self.hp = 0
        self.curr_hp = self.hp
        self.ac = 0
        self.prof_bns = 0
        self.is_defeated = False
        self.initiative = 0
        
        self.strength = 10
        self.dexterity = 10
        self.constitution = 10
        self.intelligence = 10
        self.wisdom = 10
        self.charisma = 10
        
        self.dex_bns = 0
        self.atk_bns = 0
        self.dmg_per_rnd = 0
        
    def roll_init(self):
        init = random.randint(1,20) + self.dex_bns
        return init
    
    def attack_roll(self):
        atk_roll = random.randint(1,20) + self.atk_bns
        return atk_roll

    def attack(self, enemy):
        print(self.name, "attacks", enemy.creature.name + "!")

        atk_roll = self.attack_roll()

        if (atk_roll >= enemy.creature.armor_cls):
            print(self.name, "hits!")
            enemy.creature.takes_dmg(self.dmg_per_rnd)

        else:
            print(self.name, "misses!")
    
    def take_dmg(self, dmg):
        self.curr_hp = self.hp - dmg
        self.hp = self.curr_hp
        
        if(self.hp <= 0):
            self.is_defeated = True
    
    def lvl_change(self, lvls):
        self.lvl = lvls