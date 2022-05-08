from audioop import avg
import math
import random
from single_action_attack import *
from multiattack_attack import *
from preferred_attack import *

from dummyCreature import *
class monster(creature):
    def __init__(self, window):
        self.ui = window

        self.name = self.ui.nameLineEdit.text()

        #self.armor_cls = 15 #This is used for testing, hardcoding the creature's AC
        self.armor_cls = self.ui.ArmorSpinBox.value()  #This is used to grab the creature's real AC from the UI

        #self.hit_pts = 50   #This is used for testing, hard coding the creature's hit points
        self.hit_pts = self.ui.hitPointsSpinBox.value()    #This is used to grab creature's real hit points from the UI

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

        self.multiattack_attacks = []
        self.single_action_attacks = []

        self.single_action_attack = single_action_attack()
        self.multiattack_action = multiattack_attack()
        self.atk_dmg = []

        self.pref_attack = None

        class custom_attack():
            def __init__(self, window):
                self.ui = window

                self.dmg = 0
                self.deals_dmg = None
                self.num_dmg_dice = 0
                self.dieAve = 2.5
                self.dmg_die_type = None
                self.isAOE = None

            def clear(self):
                self.dmg = 0
                self.deals_dmg = None
                self.num_dmg_dice = 0
                self.dieAve = 2.5
                self.dmg_die_type = None
                self.isAOE = None
        
        self.custom_attack = custom_attack(self.ui)

        self.setNoneStats()
        self.setAttackArrays(self.ui)
        self.setCustomAttack(self.ui)
        self.setActionArrays(self.ui)

        #for i in range(0, len(self.multiattack_attacks)):
            #print("Outside Multiattack", i + 1, ":", self.multiattack_attacks[i].num_dmg_dice, "d", self.multiattack_attacks[i].avg_dmg_dice, "+", self.multiattack_attacks[i].atk_dmgBns, "x", self.multiattack_attacks[i].num_multi_atk, self.multiattack_attacks[i].atk_bns, "to hit")

        #for i in range(0, len(self.single_action_attacks)):
            #print("Single Action Attack", i + 1, ":", self.single_action_attacks[i].num_dmg_dice, "d", self.single_action_attacks[i].avg_dmg_dice, "+", self.single_action_attacks[i].atk_dmgBns, self.single_action_attacks[i].atk_bns, "to hit")

        #print("Best Single Action Attack:", self.single_action_attack.num_dmg_dice, "d", self.single_action_attack.avg_dmg_dice, "+", self.single_action_attack.atk_dmgBns, ", to hit", self.single_action_attack.atk_bns)

        #print("Custom Action:", self.custom_attack.num_dmg_dice, "d", self.custom_attack.dieAve, self.custom_attack.isAOE)

    def setActionArrays(self, ui):
        if (ui.multiAttackCheckBox.isChecked() == True):
            self.setMultiAttackAttacks()
        
        else:
            self.setSingleActionAttacks(ui)

    def setMultiAttackAttacks(self):
        for i in range(0, 4):
            #print("self.num_multi_atk[i]: i =", i, "value =", self.num_multi_atk[i])

            if (self.num_multi_atk[i] != 0):
                for i in range(0, self.num_multi_atk[i]):
                    self.multiattack_action = multiattack_attack()

                    self.multiattack_action.atk_bns = self.atk_bns[i]
                    self.multiattack_action.num_dmg_dice = self.num_dmg_dice[i]
                    self.multiattack_action.avg_dmg_dice = self.avg_dmg_dice[i]
                    self.multiattack_action.atk_dmgBns = self.atk_dmgBns[i]

                    self.multiattack_attacks.append(self.multiattack_action)

                    #print("Attack added to multiattack array.")

            #else:
                #print("num_multi_atk[i] = 0. No attack added to multiattack array.")

        return

    def setSingleActionAttacks(self, ui):
        if (ui.actionName_1.text() != ""):
            self.single_action_attack = single_action_attack()
            atk = self.single_action_attack

            atk.atk_bns = self.atk_bns[0]
            atk.num_dmg_dice = self.num_dmg_dice[0]
            atk.avg_dmg_dice = self.avg_dmg_dice[0]
            atk.atk_dmgBns = self.atk_dmgBns[0]

            self.single_action_attacks.append(atk)

        if (ui.actionName_2.text() != ""):
            self.single_action_attack = single_action_attack()
            atk = self.single_action_attack

            atk.atk_bns = self.atk_bns[1]
            atk.num_dmg_dice = self.num_dmg_dice[1]
            atk.avg_dmg_dice = self.avg_dmg_dice[1]
            atk.atk_dmgBns = self.atk_dmgBns[1]

            self.single_action_attacks.append(atk)

        if (ui.actionName_3.text() != ""):
            self.single_action_attack = single_action_attack()
            atk = self.single_action_attack
            
            atk.atk_bns = self.atk_bns[2]
            atk.num_dmg_dice = self.num_dmg_dice[2]
            atk.avg_dmg_dice = self.avg_dmg_dice[2]
            atk.atk_dmgBns = self.atk_dmgBns[2]

            self.single_action_attacks.append(atk)

        if (ui.actionName_4.text() != ""):
            self.single_action_attack = single_action_attack()
            atk = self.single_action_attack
        
            atk.atk_bns = self.atk_bns[3]
            atk.num_dmg_dice = self.num_dmg_dice[3]
            atk.avg_dmg_dice = self.avg_dmg_dice[3]
            atk.atk_dmgBns = self.atk_dmgBns[3]

            self.single_action_attacks.append(atk)

        self.compareSingleActionAttacks()

        return

    def compareSingleActionAttacks(self):
        for i in range(0, len(self.single_action_attacks)):
            dmg = math.floor(self.single_action_attacks[i].num_dmg_dice * self.single_action_attacks[i].avg_dmg_dice + self.single_action_attacks[i].atk_dmgBns)

            best_singleActionAttack_dmg = math.floor(self.single_action_attack.num_dmg_dice * self.single_action_attack.avg_dmg_dice + self.single_action_attack.atk_dmgBns)

            #print(i, self.single_action_attacks[i].num_dmg_dice, self.single_action_attacks[i].avg_dmg_dice, self.single_action_attacks[i].atk_dmgBns, dmg)

            if (dmg > best_singleActionAttack_dmg):
                #print(dmg, "is greater than current attack's dmg of", best_singleActionAttack_dmg)
                #print("Setting new single attack.")

                self.single_action_attack.atk_bns = self.single_action_attacks[i].atk_bns
                self.single_action_attack.num_dmg_dice = self.single_action_attacks[i].num_dmg_dice
                self.single_action_attack.avg_dmg_dice = self.single_action_attacks[i].avg_dmg_dice
                self.single_action_attack.atk_dmgBns = self.single_action_attacks[i].atk_dmgBns

        return

    def setNoneStats(self):
        self.setProfBns()
        self.dex_bns = self.setAttrBns(self.dex)

    def setCustomAttack(self, ui):
        self.custom_attack.deals_dmg = ui.doesDamageCheckBox.isChecked()
        self.custom_attack.num_dmg_dice = ui.customNumOfDiespinBox.value()
        self.custom_attack.dmg_die_type = ui.typeOfDieComboBox.currentIndex()

        if (self.custom_attack.dmg_die_type == 0):
            self.custom_attack.dieAve = 2.5

        elif (self.custom_attack.dmg_die_type == 1):
            self.custom_attack.dieAve = 3.5

        elif (self.custom_attack.dmg_die_type == 2):
            self.custom_attack.dieAve = 4.5

        elif (self.custom_attack.dmg_die_type == 3):
            self.custom_attack.dieAve = 5.5

        elif (self.custom_attack.dmg_die_type == 4):
            self.custom_attack.dieAve = 6.5

        else:
            print("Could not determine dieAve in setCustomAttack() monster_stats.py")

        self.custom_attack.isAOE = ui.aoeButton.isChecked()

        if (self.custom_attack.deals_dmg == True):
            if (self.custom_attack.isAOE == True):
                self.custom_attack.deals_dmg = 2 * self.custom_attack.num_dmg_dice * self.custom_attack.dieAve

            else:
                self.custom_attack.dmg = self.custom_attack.num_dmg_dice * self.custom_attack.dieAve

    def clearData(self):
        self.num_multi_atk.clear()
        self.atk_bns.clear()
        self.num_dmg_dice.clear()
        self.type_dmg_dice.clear()
        self.avg_dmg_dice.clear()
        self.atk_attr.clear()
        self.atk_dmgBns.clear()

        self.single_action_attack.clear()
        self.multiattack_attacks.clear()

        self.custom_attack.clear()

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
        self.set_atk_bns(ui)
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

    def set_atk_bns(self, ui):
        self.atk_bns.append(int(ui.plusLabel_1.text()))
        self.atk_bns.append(int(ui.plusLabel_2.text()))
        self.atk_bns.append(int(ui.plusLabel_3.text()))
        self.atk_bns.append(int(ui.plusLabel_4.text()))

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
        if (self.challnge_rtg > 1):
            self.prof_bns = math.floor((self.challnge_rtg + 7) / 4)

        elif(self.challnge_rtg <= 1):
            self.prof_bns = 2

        else:
            print("Could not determine monster.prof_bns with monster_stats.setProfBns. monster.challnge_rtg =", self.challnge_rtg)

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
    
    def determineWhichAttack(self):
        print("Determining creature's pref_attack...")

        avg_singleActionAttack_dmg = 0
        avg_multiAttack_dmg = 0
        avg_customActionAttack_dmg = 0

        if (self.multiattack_checked == False):
            avg_singleActionAttack_dmg = self.single_action_attack.num_dmg_dice * self.single_action_attack.avg_dmg_dice + self.single_action_attack.atk_dmgBns

            #print("avg_singleActionAttack_dmg:", avg_singleActionAttack_dmg)

        elif (self.multiattack_checked == True):
            for i in range(0, len(self.multiattack_attacks)):
                avg_multiAttack_dmg = avg_multiAttack_dmg + (self.multiattack_attacks[i].num_dmg_dice * self.multiattack_attacks[i].avg_dmg_dice + self.multiattack_attacks[i].atk_dmgBns)

                #print(self.multiattack_attacks[i].num_dmg_dice, self.multiattack_attacks[i].avg_dmg_dice, self.multiattack_attacks[i].atk_dmgBns)

            #print("avg_multiAttack_dmg:", avg_multiAttack_dmg)
        
        if (self.custom_attack.deals_dmg == True):
            avg_customActionAttack_dmg = self.custom_attack.num_dmg_dice * self.custom_attack.dieAve

            if (self.custom_attack.isAOE == True):
                avg_customActionAttack_dmg = avg_customActionAttack_dmg * 2

            #print("avg_customActionAttack_dmg:", avg_customActionAttack_dmg)

        if (self.multiattack_checked == False):
            if (avg_singleActionAttack_dmg > avg_customActionAttack_dmg):
                self.pref_attack = preferred_attack.single_action_attack

                #print("Set creature's pref_attack to single_action_attack")

            else:
                self.pref_attack = preferred_attack.custom_attack

                #print("Set creature's pref_attack to custom_attack")

        elif (self.multiattack_checked == True):
            if (avg_multiAttack_dmg > avg_customActionAttack_dmg):
                self.pref_attack = preferred_attack.multiattack

                #print("Set creature's pref_attack to multiattack")

            else:
                self.pref_attack = preferred_attack.custom_attack

                #print("Set creature's pref_attack to custom_attack")

        else:
            print("Could not determined creature's pref_attack in monster_stats.determineWhichAttack")

            return

        print(self.name + "'s preferred attack is", self.pref_attack._name_)

    def has_attacked(self):
        return self.hasattacked

    def attack(self, enemy):
        #self.hasattacked = True

        self.determineWhichAttack()

        totalDmg = 0

        if (self.pref_attack == preferred_attack.multiattack):
            for i in range(len(self.multiattack_attacks)):
                atk_die_type = None
                
                if (self.multiattack_attacks[i].avg_dmg_dice == 2.5):
                    atk_die_type = 4

                elif (self.multiattack_attacks[i].avg_dmg_dice == 3.5):
                    atk_die_type = 6

                elif (self.multiattack_attacks[i].avg_dmg_dice == 4.5):
                    atk_die_type = 8

                elif (self.multiattack_attacks[i].avg_dmg_dice == 5.5):
                    atk_die_type = 10

                elif (self.multiattack_attacks[i].avg_dmg_dice == 6.5):
                    atk_die_type = 12

                else:
                    print("Can't determine multiattack die_type in multiattack_attacks monster_stats.attack")

                num_die = self.multiattack_attacks[i].num_dmg_dice
                dmg_bns = self.multiattack_attacks[i].atk_dmgBns

                totalDmg = self.cal_attack_dmg(num_die, atk_die_type, dmg_bns)

                self.deal_multi_damage(enemy, totalDmg, i)
    
        elif (self.pref_attack == preferred_attack.single_action_attack):
            die_type = 4

            if (self.single_action_attack.avg_dmg_dice == 2.5):
                die_type = 4
            elif (self.single_action_attack.avg_dmg_dice == 3.5):
                die_type = 6
            elif (self.single_action_attack.avg_dmg_dice == 4.5):
                die_type = 8
            elif (self.single_action_attack.avg_dmg_dice == 5.5):
                die_type = 10
            elif (self.single_action_attack.avg_dmg_dice == 6.5):
                die_type = 12
            else:
                print("Could not determine die_type in single_action_attack monster_stats.attack")

            num_die = self.single_action_attack.num_dmg_dice
            dmg_bns = self.single_action_attack.atk_dmgBns

            totalDmg = self.cal_attack_dmg(num_die, die_type, dmg_bns)

            self.deal_damage(enemy, totalDmg)

        elif (self.pref_attack == preferred_attack.custom_attack):
            num_die = self.custom_attack.num_dmg_dice
            die_type = 4

            if (self.custom_attack.dieAve == 2.5):
                die_type = 4
            elif (self.custom_attack.dieAve == 3.5):
                die_type = 6
            elif (self.custom_attack.dieAve == 4.5):
                die_type = 8
            elif (self.custom_attack.dieAve == 5.5):
                die_type = 10
            elif (self.custom_attack.dieAve == 6.5):
                die_type = 12
            else:
                print("Could not determine die_type in custom_attack monster_stats.attack")

            #print(num_die, die_type)

            totalDmg = self.cal_attack_dmg(num_die, die_type, 0)

            self.deal_customAttack_damage(enemy, totalDmg)

            #self.hasattacked = True

        else:
            print("Could not determine single or multiattack in monster_stats.attack")

        self.hasattacked = True

    def deal_customAttack_damage(self, enemy, dmg):
        targetIndex1 = random.randint(0, len(enemy.players) - 1)

        target = enemy.players[targetIndex1]
        
        target2 = 0

        if (self.custom_attack.isAOE == True):
            targetIndex2 = random.randint(0, len(enemy.players) - 1)

            if (len(enemy.players) > 1):
                while (targetIndex1 == targetIndex2):
                    targetIndex2 = random.randint(0, len(enemy.players) - 1)

                target2 = enemy.players[targetIndex2]

        saveBns = 0

        for i in range (0, len(self.atk_bns)):
            if (self.atk_bns[i] > saveBns):
                saveBns = self.atk_bns[i]

        saveDC = 8 + self.prof_bns + saveBns

        target.saving_throw(dmg, saveDC)

        if (target2 != 0):
            target2.saving_throw(dmg, saveDC)
            self.hasattacked == True

        self.hasattacked == True

        print()

        return

    def deal_multi_damage(self, enemy, dmg, i):
        targetIndex = random.randint(0, len(enemy.players) - 1)
        
        target = enemy.players[targetIndex]

        if (target.is_defeated == True):
            print("Attack target is already down. Omitting attack.")
            return
        
        atk_roll = self.multi_attack_roll(i)

        print(self.name, "attacks", target.name, "for its", str(i + 1) + "th attack!")
        print(self.name, "rolled a", atk_roll, "against", target.name + "'s AC of", target.ac)

        if (atk_roll >= target.ac):
            print(self.name, "hits!")
            print(self.name, "rolls", self.multiattack_attacks[i].num_dmg_dice, "d", self.multiattack_attacks[i].avg_dmg_dice, "+", self.multiattack_attacks[i].atk_dmgBns)
   
            target.takes_dmg(dmg)
            self.hasattacked = True
        
        else:
            print(self.name, "misses!")
            self.hasattacked = True
			
        print()

    def multi_attack_roll(self, i):
        atk_roll = random.randint(1, 20) + self.multiattack_attacks[i].atk_bns

        return atk_roll

    def cal_attack_dmg(self, num_die, atk_die_type, dmg_bns):
        #print(num_die, atk_die_type, dmg_bns)

        atk_dmg = 0

        for i in range(0, num_die):
            atk_dmg = atk_dmg + random.randint(1, atk_die_type)

        atk_dmg = atk_dmg + dmg_bns

        return atk_dmg

    def deal_damage(self, enemy, dmg):
        targetIndex = random.randint(0, len(enemy.players) - 1)
        
        target = enemy.players[targetIndex]
        
        atk_roll = self.attack_roll()

        print(self.name, "attacks", target.name + "!")
        print(self.name, "rolled a", atk_roll, "against", target.name + "'s AC of", target.ac)

        if (atk_roll >= target.ac):
            print(self.name, "hits!")
            print(self.name, "rolls", self.single_action_attack.num_dmg_dice, "d", self.single_action_attack.avg_dmg_dice, "!")
   
            target.takes_dmg(dmg)
            self.hasattacked = True
        
        else:
            print(self.name, "misses!")
            self.hasattacked = True
			
        print()

    def attack_roll(self):
        atk_roll = random.randint(1, 20) + self.single_action_attack.atk_bns 

        return atk_roll