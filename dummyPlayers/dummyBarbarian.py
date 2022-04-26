import random
from types import NoneType

from player import *

class Barbarian(Player):
    def __init__(self):

    #Might Erase
        self.name = "Barbarian"
        self.logEQ = None
        self.lvl = 1
        self.hp = 10
        self.curr_hp = self.hp
        self.ac = 14
        self.prof_bns = 2
        self.is_defeated = False
        self.initiative = 0
        
        self.strength = 20
        self.dexterity = 14
        self.constitution = 18
        self.intelligence = 8
        self.wisdom = 8
        self.charisma = 12
        
        self.dex_bns = 2
        self.dex_bns = 2
        self.atk_bns = 5
        self.dmg_per_rnd = 2
        
    def lvl_change(self, lvls):
        return super().lvl_change(lvls)
    
    def roll_init(self):
        return super().roll_init()
  