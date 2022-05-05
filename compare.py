from logging import Handler
from re import X
from typing import final
from dummyCreature import creature
from dummyCreatures import dummyCyclops, dummyMinotaur, dummyBugBear, dummyOrc, dummyZombie, dummyGiantRat
from dummyPlayers import dummyFighter, dummyRanger, dummyRogue, dummyWizard
from player import *
from creature_exp import *
import numpy as np
import matplotlib.pyplot as plt
import combat

class compareCRandEC():
    def __init__(self,creature, players):
        self.creature = creature
        
        self.players = []
        for i in range (0, len(players)):
            self.players.append(players[i])
        
        
    
    def playerEXP(self):
        expArry = []
        for i in range (0,len(self.players)):
            if(len(self.players)-1 >= i):
                expArry.append(player_exp(self.players[i].lvl))
        
        return expArry
                         
  
    def creatureEXP(self):
        Creature_exp = cr_to_exp(3)
        print("creature exp", Creature_exp)
        return Creature_exp
    
    def enconter_diff(self):
        list_players_exp = self.playerEXP()
        creature_exp = self.creatureEXP()
        Easy = 0
        Medium = 0
        Hard  = 0 
        Deadly = 0
        
        print(list_players_exp)
        for i in list_players_exp:
            for j, exp_num in enumerate(i):
                if (j == 0):
                    Easy += exp_num
                elif (j == 1):
                    Medium += exp_num
                elif (j == 2):
                    Hard += exp_num
                else:
                    Deadly += exp_num
        
        if (Easy >= creature_exp):
            print("easy exp", Easy)
            ec_var = "Easy"
            return ec_var
        elif (Medium >= creature_exp):
            print("medium exp", Medium)
            ec_var = "Medium"
            return ec_var
        elif (Hard >= creature_exp):
            print("hard exp", Hard)
            ec_var = "Hard"
            return ec_var
        elif (Deadly >= creature_exp):
            print("deadly exp", Deadly)
            ec_var = "Deadly"
            return ec_var
          
                
        
    def percentWinRate(self, numRounds, roundsWon):
        winPercentage = roundsWon / numRounds
        return winPercentage
    
    def compare_Winpercent_and_CE(self):
        percent = self.percentWinRate(4,3)
        percent_var = ""
        if(percent <= .25):
            percent_var = "Easy"
            print("easy ", percent)
        elif(percent <= .50):
            percent_var = "Medium"
            print("medium ", percent)
        elif(percent <= .75):
            percent_var = "Hard"
            print("hard ", percent)
        elif(percent <= 1.00):
            percent_var = "Deadly"
            print("deadly ", percent)
        
        ec = self.enconter_diff()
        
        if(ec == percent_var):
            print("Percentile win rate is equal to the correct creature encounter difficulty")
        else:
            print("Percentile win rate is not equal to the correct creature encounter difficulty")
            
            
    def simulate_rec(self):
        x = 100
        some_num = 0
        players_won = 0
        creature_won = 0
        hp_val = 0
        hp_val2 = 0
        hp_val3 = 0
        hp_val4 = 0
        creature_hp = self.creature.hit_pts
        if (len(self.players) == 4):
            hp_val = self.players[0].hp
            hp_val2 = self.players[1].hp
            hp_val3 = self.players[2].hp
            hp_val4 = self.players[3].hp
        elif (len(self.players) == 3):
            hp_val = self.players[0].hp
            hp_val2 = self.players[1].hp
            hp_val3 = self.players[2].hp
        elif (len(self.players) == 2):
            hp_val = self.players[0].hp
            hp_val2 = self.players[1].hp
        else:
            hp_val = self.players[0].hp
            
        while (x != 0):
            fighting = combat.combatSimulation(self.creature, self.players)
            print("current hp for p1: ",self.players[0].hp)
            x -= 1
            self.reset_players_hp(creature_hp, hp_val, hp_val2, hp_val3, hp_val4)
            fighting.combatSim()
            if (self.creature.is_defeated):
                players_won += 1
            else:
                creature_won += 1
            some_num += 1
        print("some_num: ", some_num)
        print("creature w's: ", creature_won)
        print("players w's: ", players_won)
        percentage = creature_won / some_num
        self.reset_players_hp(creature_hp, hp_val, hp_val2, hp_val3, hp_val4)
        return percentage
     
    def final_solution(self):
        golden_num = self.simulate_rec()
        over_twenty = False
        if (self.creature.hit_pts < 1):
            print("creature hp points are negative: ", self.creature.hit_pts)
        else:
            if (golden_num > .45 and golden_num < .55):
                for i in self.players:
                    print ("player_lvl change: ", i.lvl)
                    
                print ("golden ratio: ", golden_num)
                return golden_num
            elif (golden_num > .55):
                for i in self.players:
                    curr_lvl = i.lvl
                    curr_lvl += 1
                    if (curr_lvl > 20):
                        over_twenty = True
                    i.lvl_change(curr_lvl)
                    print ("player_lvl change", i.lvl)     
                if (over_twenty != True):
                    self.new_hpAndDmpr()
                    #self.final_solution()
                else:
                    print("player lvl was over twenty")
            elif (golden_num < .45):
                for i in self.players:
                    if (i.lvl > 1):
                        curr_lvl = i.lvl
                        curr_lvl -= 1
                        if (curr_lvl > 20):
                            over_twenty = True
                        i.lvl_change(curr_lvl)
                        print ("player_lvl change", i.lvl)      
                if (over_twenty != True):
                    self.new_hpAndDmpr()
                    #self.final_solution()
                else:
                    print("player lvl was over twenty")
                
    def reset_players_hp(self, creature_hp, hp_val, hp_val2, hp_val3, hp_val4):
        self.creature.hit_pts = creature_hp
        self.creature.is_defeated = False
        print("creature is_defeated", self.creature.is_defeated)
        print("creature hp: ", self.creature.hit_pts)
        if (len(self.players) == 4):
            self.players[0].hp_change(hp_val)
            self.players[1].hp_change(hp_val2)
            self.players[2].hp_change(hp_val3)
            self.players[3].hp_change(hp_val4)
            print("current hp 0: ",self.players[0].hp)
            print("current hp 1: ",self.players[1].hp)
            print("current hp 2: ",self.players[2].hp)
            print("current hp 3: ",self.players[3].hp)
            self.players[0].is_defeated = False
            self.players[1].is_defeated = False
            self.players[2].is_defeated = False
            self.players[3].is_defeated = False
            print("current p1 is_defeated: ",self.players[0].is_defeated)
            print("current p2 is_defeated: ",self.players[1].is_defeated)
            print("current p3 is_defeated: ",self.players[2].is_defeated)
            print("current p4 is_defeated: ",self.players[3].is_defeated)
        elif (len(self.players) == 3):
            self.players[0].hp_change(hp_val)
            self.players[1].hp_change(hp_val2)
            self.players[2].hp_change(hp_val3)
            print("current hp 0: ",self.players[0].hp)
            print("current hp 1: ",self.players[1].hp)
            print("current hp 2: ",self.players[2].hp)
            self.players[0].is_defeated = False
            self.players[1].is_defeated = False
            self.players[2].is_defeated = False
            print("current p1 is_defeated: ",self.players[0].is_defeated)
            print("current p2 is_defeated: ",self.players[1].is_defeated)
            print("current p3 is_defeated: ",self.players[2].is_defeated)
        elif (len(self.players) == 2):
            self.players[0].hp_change(hp_val)
            self.players[1].hp_change(hp_val2)
            print("current p1 hp 0: ",self.players[0].hp)
            print("current p2 hp 1: ",self.players[1].hp)
            self.players[0].is_defeated = False
            self.players[1].is_defeated = False
            print("current p1 is_defeated: ",self.players[0].is_defeated)
            print("current p2 is_defeated: ",self.players[1].is_defeated)
        else:
            self.players[0].hp_change(hp_val)
            print("current hp 0: ",self.players[0].hp)
            self.players[0].is_defeated = False
            print("current p1 is_defeated: ",self.players[0].is_defeated)
            print("current p1 lvl_: ",self.players[0].lvl)
            
    def new_hpAndDmpr(self):
        x = np.array(range(1, 21))

        fighterY = 15.3552 * np.log(1.5775*x)
        fighterHpY = 50.405 * np.log(1.2194*x)
        fighterCurve, = plt.plot(x, fighterY)
        fighterHpCurve, = plt.plot(x, fighterHpY)
        fighterXData = fighterCurve.get_xdata()
        fighterYData = fighterCurve.get_ydata()
        fighterHpYdata = fighterHpCurve.get_ydata()

        rangerY = 13.0185 * np.log(1.4682*x)
        rangerHpY = 50.405 * np.log(1.2194*x)
        rangerCurve, = plt.plot(x, rangerY)
        rangerHpCurve, = plt.plot(x,rangerHpY)
        rangerXData = rangerCurve.get_xdata()
        rangerYData = rangerCurve.get_ydata()
        rangerHpYData = rangerHpCurve.get_ydata()

        rogueY = 11.6833 * np.log(1.5341*x)
        rogueHpY = 38.3879 * np.log(1.2317*x)
        rogueCurve, = plt.plot(x, rogueY)
        rogueHpCurve, = plt.plot(x,rogueHpY)
        rogueXData = rogueCurve.get_xdata()
        rogueYData = rogueCurve.get_ydata()
        rogueHpYData = rogueHpCurve.get_ydata()

        wizardY = 14.6876 * np.log(1.2266*x)
        wizardHpY = 38.3879 * np.log(1.2317*x)
        wizardCurve, = plt.plot(x, wizardY)
        wizardHpCurve, = plt.plot(x, wizardHpY)
        wizardXData = wizardCurve.get_xdata()
        wizardYData = wizardCurve.get_ydata()
        wizardHpYData = wizardHpCurve.get_ydata()
        
        for i in self.players:
            if (i.name == "Fighter"):
                curr_lvl = i.lvl
                i.dpr_change(np.rint(fighterYData[curr_lvl-1]))
                i.hp_change(np.rint(fighterHpYdata[curr_lvl-1]))
            elif (i.name == "Ranger"):
                curr_lvl = i.lvl
                i.dpr_change(np.rint(rangerYData[curr_lvl-1]))
                i.hp_change(np.rint(rangerHpYData[curr_lvl-1]))
            elif (i.name == "Rogue"):
                curr_lvl = i.lvl
                i.dpr_change(np.rint(rogueYData[curr_lvl-1]))
                i.hp_change(np.rint(rogueHpYData[curr_lvl-1]))
            elif (i.name == "Wizard"):
                curr_lvl = i.lvl
                i.dpr_change(np.rint(wizardYData[curr_lvl-1]))
                i.hp_change(np.rint(wizardHpYData[curr_lvl-1]))
            