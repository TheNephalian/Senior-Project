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
        self.num_multi_atk = [3]
        self.atk_bns = [3]
        self.num_dmg_dice = [3]
        self.type_dmg_dice = [3]
        self.avg_dmg_dice = [3]
        self.atk_attr = [3]
        self.atk_dmgBns = [3]

        self.single_action_attacks = []
        self.multiattack_attacks = []

        self.atk_dmg = []
        
        class custom_attack():
            def __init__(self, window):
                self.ui = window

                self.deals_dmg = None
                self.num_dmg_dice = 0
                self.dieAve = 2.5
                self.dmg_die_type = None
                self.isAOE = None
        
        self.custom_attack = custom_attack(self.ui)

        self.setNoneStats()
        self.setAttackArrays(self.ui)

    def setNoneStats(self):
        self.setProfBns()
        self.dex_bns = self.setAttrBns(self.dex)

    def clearData(self):
        self.num_multi_atk.clear()
        self.atk_bns.clear()
        self.num_dmg_dice.clear()
        self.type_dmg_dice.clear()
        self.avg_dmg_dice.clear()
        self.atk_attr.clear()
        self.atk_dmgBns.clear()

        self.single_action_attacks.clear()
        self.multiattack_attacks.clear()

        self.atk_dmg.clear()

    def setAttackArrays(self, ui):
        self.clearData()

        if (self.multiattack_checked == True):
            self.set_multiattack_array(ui)

        else:
            self.set_single_action_array(ui)

        self.set_custom_action(ui)

    def set_multiattack_array(self, ui):
        self.set_num_multi_attack(ui)

        self.set_action_stat_arrays(ui)

    def set_single_action_array(self, ui):
        self.set_action_stat_arrays(ui)

    def set_custom_action(self, ui):
        self.custom_attack.does_dmg = ui.doesDamageCheckBox.isChecked()
        self.custom_attack.isAOE = ui.aoeButton.isChecked()
        
        dieType = self.custom_attack.dmg_die_type = ui.typeOfDieComboBox.currentIndex()

        if (dieType == 0):
            self.custom_attack.dieAve = 2.5
		
        elif (dieType == 1):
            self.custom_attack.dieAve = 3.5

        elif (dieType == 2):
            self.custom_attack.dieAve = 4.5

        elif (dieType  == 3):
            self.custom_attack.dieAve = 5.5

        elif (dieType == 4):
            self.custom_attack.dieAve = 6.5

    def set_action_stat_arrays(self, ui):
        self.set_num_dmg_dice(ui)
        self.set_type_dmg_dice(ui)
        self.set_avg_dmg_dice()
        self.set_atk_attr(ui)
        self.set_atk_dmgBns(ui)

    def set_num_multi_attack(self, ui):
        self.num_multi_atk.append(ui.spinBox.value())
        self.num_multi_atk.append(ui.spinBox_2.value())
        self.num_multi_atk.append(ui.spinBox_3.value())
        self.num_multi_atk.append(ui.spinBox_4.value())

    def set_num_dmg_dice(self, ui):
        self.num_dmg_dice.append(ui.numDieSpinBox.value())
        self.num_dmg_dice.append(ui.numDieSpinBox_2.value())
        self.num_dmg_dice.append(ui.numDieSpinBox_3.value())
        self.num_dmg_dice.append(ui.numDieSpinBox_4.value())

    def set_type_dmg_dice(self, ui):
        self.type_dmg_dice.append(ui.actionDice_1.currentText())
        self.type_dmg_dice.append(ui.actionDice_2.currentText())
        self.type_dmg_dice.append(ui.actionDice_3.currentText())
        self.type_dmg_dice.append(ui.actionDice_4.currentText())

    def set_avg_dmg_dice(self):
        for i in range(0, 4):
            if (self.type_dmg_dice[i] == "4"):
                self.avg_dmg_dice.append(2.5)
			
            elif (self.type_dmg_dice[i] == "6"):
                self.avg_dmg_dice.append(3.5)
                
            elif (self.type_dmg_dice[i] == "8"):
                self.avg_dmg_dice.append(4.5)

            elif (self.type_dmg_dice[i] == "10"):
                self.avg_dmg_dice.append(5.5)

            elif (self.type_dmg_dice[i] == "12"):
                self.avg_dmg_dice.append(6.5)

    def set_atk_attr(self, ui):
        self.atk_attr.append(ui.attrComboBox_1.currentIndex())
        self.atk_attr.append(ui.attrComboBox_2.currentIndex())
        self.atk_attr.append(ui.attrComboBox_3.currentIndex())
        self.atk_attr.append(ui.attrComboBox_4.currentIndex())

    def set_atk_dmgBns(self, ui):
        for i in range(0, 4):
            if (self.atk_attr[i] == 0):
                self.atk_dmgBns.append(self.setAttrBns(ui.strSpinBox.value()))
			
            elif (self.atk_attr[i] == 1):
                self.atk_dmgBns.append(self.setAttrBns(ui.dexSpinBox.value()))

            elif (self.atk_attr[i] == 2):
                self.atk_dmgBns.append(self.setAttrBns(ui.conSpinBox.value()))
			
            elif (self.atk_attr[i] == 3):
                self.atk_dmgBns.append(self.setAttrBns(ui.intSpinBox.value()))

            elif (self.atk_attr[i] == 4):
                self.atk_dmgBns.append(self.setAttrBns(ui.wisSpinBox.value()))
			
            elif (self.atk_attr[i] == 5):
                self.atk_dmgBns.append(self.setAttrBns(ui.chaSpinBox.value()))

            else:
                print("Could not determine element", i, "of dpr_calculation.atk_attr[3]")

    def setProfBns(self):
        self.prof_bns = math.floor((self.challnge_rtg - 9) / 2)

    def setAttrBns(self, attr):
        attr_bns = math.floor((attr - 10) / 2)

        return attr_bns

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
        print("WIP")
        #print("Action 1 rolls for", self.single_action_attacks[1][0], "d", self.single_action_attacks[2][0], "+", )

    def roll_init(self):
        return super().roll_init()
        
    def takes_dmg(self, dmg):
        super().takes_dmg(dmg)
    
    '''This function is hardcoded for initial custom creature combat simulations'''
    def attack(self, enemy):
        totalDmg = 20
    
        self.attack(self, enemy, totalDmg)

    '''This function is hardcoded for initial custom creature combat simulations'''
    def attack(self, enemy, dmg):
        targetIndex = random.randint(0, len(enemy.players) - 1)
        
        target = enemy.players[targetIndex]
        
        atk_roll = self.attack_roll()

        print(self.name, "attacks", target.name + "!")
        print(self.name, "rolled a", atk_roll, "against", target.name + "'s AC of", target.ac)

        if (atk_roll >= target.ac):
            print(self.name, "hits!")
   
            target.takes_dmg(dmg)
            self.hasattacked = True
        
        else:
            print(self.name, "misses!")
            self.hasattacked = True
			
        print()

    '''This function is hardcoded for initial custom creature combat simulations'''
    def attack_roll(self):
        atk_roll = 20

        return atk_roll