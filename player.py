import random
import math


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
        self.hasattacked = False

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
        init = random.randint(1, 20) + self.dex_bns
        return init

    def attack_roll(self):
        atk_roll = random.randint(1, 20) + self.atk_bns
        return atk_roll

    def attack(self, enemy):
        if (self.is_defeated == True):
            #print(self.name, "is defeated and is to be removed from combat.")
            #print()

            return

        atk_roll = self.attack_roll()

        #print(self.name, "attacks", enemy.creature.name + "!")
        #print(self.name, "rolled a", atk_roll, "against",
              #enemy.creature.name + "'s AC of", enemy.creature.armor_cls)

        if (atk_roll >= enemy.creature.armor_cls):
            #print(self.name, "hits!")

            enemy.creature.takes_dmg(self.dmg_per_rnd)
            self.hasattacked = True

        else:
            #print(self.name, "misses!")
            self.hasattacked = True

        #print()

    def takes_dmg(self, dmg):
        self.curr_hp = self.hp - dmg
        self.hp = self.curr_hp

        #print(self.name, "takes", dmg, "damage!")
        #print(self.name + "'s hit points =", self.hp)

        if (self.hp <= 0):
            self.defeated()

    def defeated(self):
        self.is_defeated = True

        #print(self.name, "is defeated!")

    def lvl_change(self, lvls):
        self.lvl = lvls

    def dpr_change(self, dmg_per_rnd):
        self.dmg_per_rnd = dmg_per_rnd

    def hp_change(self, hp):
        self.hp = hp

    def has_attacked(self):
        thisattack = self.hasattacked
        return thisattack

    def has_not_attacked(self):
        self.hasattacked = False

    def saving_throw(self, dmg, saveDC):
        saving_throw = random.randint(1, 20) + self.prof_bns + 2

        #print(self.name, "rolls a saving throw of",
              #saving_throw, "against save DC", saveDC)

        if (saving_throw >= saveDC):
            #print(self.name, "successfully saves!")

            self.takes_dmg(math.floor(dmg / 2))

        else:
            #print(self.name, "failed their saving throw!")

            self.takes_dmg(dmg)
