import math

from dummyCreature import *
class monster(creature):
    def __init__(self, window):
        self.ui = window

        self.name = self.ui.nameLineEdit.text()
        self.armor_cls = self.ui.ArmorSpinBox.value()
        self.hit_pts = self.ui.hitPointsSpinBox.value()
        self.curr_hp = self.hit_pts
        self.challnge_rtg = int(self.ui.sliderValTxt.text())
        self.prof_bns = None

        self.is_defeated = False
        self.hasattacked = False

        self.str = self.ui.strSpinBox.value()
        self.dex = self.ui.dexSpinBox.value()
        self.con = self.ui.conSpinBox.value()
        self.int = self.ui.intSpinBox.value()
        self.wis = self.ui.wisSpinBox.value()
        self.cha = self.ui.chaSpinBox.value()

        self.dex_bns = None

        self.multiattack_checked = self.ui.multiAttackCheckBox.isChecked()
        self.multiattack_nums = [3]
        self.num_dmg_dice = [3]
        self.dmg_die_type = [3]
        self.attack_attr = [3]
        self.dmg_bns = [3]

        self.single_action_attacks = []
        self.multiattack_attacks = []
        
        class custom_attack():
            def __init__(self, window):
                self.ui = window

                self.deals_dmg = None
                self.num_dmg_dice = 0
                self.dmg_die_type = None
                self.isAOE = None
        
        custom_attack = custom_attack(self.ui)

        self.setNoneStats()
        self.setAttackArrays(self.ui)

    def setNoneStats(self):
        self.setProfBns()
        self.setDexBns()

    def setAttackArrays(self, ui):
        if (self.multiattack_checked == True):
            return

        else:
            return

    def setProfBns(self):
        self.prof_bns = math.floor((self.challnge_rtg - 9) / 2)

    def setDexBns(self):
        self.dex_bns = math.floor((self.dex - 10) / 2)

    def print_stats(self):
        print()
        print("Name:", self.name)
        print("AC:", self.armor_cls)
        print("Hit Points:", self.hit_pts)
        print("Challenge Rating:", self.challnge_rtg, "Proficiency Bonus:", self.prof_bns)
        print("Initiative Bonus:", self.dex_bns)
        print()
        print("STR:", self.str, "DEX:", self.dex, "CON", self.con, "INT:", self.int, "WIS:", self.wis, "CHA", self.cha)

        self.print_attack_stats()

    '''WIP'''
    def print_attack_stats(self):
        print(self.name, "has the following action stats:")
        #print("Action 1 rolls for", self.single_action_attacks[1][0], "d", self.single_action_attacks[2][0], "+", )

    def roll_init(self):
        return super().roll_init()
        
    def takes_dmg(self, dmg):
        super().takes_dmg(dmg)
        
    def attack(self, enemy):
        totalDmg = 0
    
        super().attack(enemy, totalDmg)