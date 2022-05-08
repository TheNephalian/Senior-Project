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
        x = 1000
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
            #print("current hp for p1: ",self.players[0].hp)
            x -= 1
            creature_plyer_hp = self.reset_players_hp(creature_hp, hp_val, hp_val2, hp_val3, hp_val4)
            if(creature_plyer_hp == True):
                #print("negative hp values break")
                return -1
            else:
                fighting.combatSim()
                if (self.creature.is_defeated):
                    players_won += 1
                else:
                    creature_won += 1
                some_num += 1
        #print("some_num: ", some_num)
        print("creature w's: ", creature_won)
        print("players w's: ", players_won)
        percentage = creature_won / some_num
        creature_plyer_hp = self.reset_players_hp(creature_hp, hp_val, hp_val2, hp_val3, hp_val4)
        if(creature_plyer_hp == True):
            #print("negative hp values break")
            return -1
        else:
            return percentage
     
    def final_solution(self, num_sim, lvl_chg):
        avg_players_lvl = 0
        for i in self.players:
            avg_players_lvl += i.lvl
        avg_players_lvl = avg_players_lvl / len(self.players)
        avg_players_lvl = int(avg_players_lvl)
                
        golden_num = self.simulate_rec()
        over_twenty = False
        if (golden_num == -1):
            print("simulation over cause hp values did not reset")
        else:
            if ((golden_num > .45 and golden_num < .55) or num_sim >= 20):
                for i in self.players:
                    print ("player_lvl change: ", i.lvl)
                print ("golden ratio: ", golden_num)
                print("creature cr: ", self.creature.challnge_rtg)
                num_sim = num_sim * 1000
                print("num of simulations: ", num_sim)
                print("num of lvl changes: ", lvl_chg)
                return golden_num
            if (golden_num == 0):
                for i in self.players:
                    print ("player_lvl change: ", i.lvl)
                print ("golden ratio: ", golden_num)
                print("creature cr: ", self.creature.challnge_rtg)
                num_sim = num_sim * 1000
                print("num of simulations: ", num_sim)
                print("num of lvl changes: ", lvl_chg)
                return golden_num
            elif (golden_num > .55):
                for i in self.players:
                    curr_lvl = i.lvl
                    curr_lvl += 1
                    if (curr_lvl > 20):
                        over_twenty = True
                    i.lvl_change(curr_lvl)
                    print ("player_lvl change {i.name} :", i.lvl)     
                if (over_twenty != True):
                    print("in lvl add one")
                    self.new_hpAndDmpr()
                    self.final_solution(num_sim+1,lvl_chg+1)
                    # if (avg_players_lvl > self.creature.challnge_rtg):
                    #     print("players avg lvl is greater than creature cr: ", avg_players_lvl)
                    #     print("creature cr: ", self.creature.challnge_rtg)
                    #     num_sim = num_sim * 1000
                    #     print("num of simulations: ", num_sim)
                    # else:
                    #     self.final_solution(num_sim+1, times_in_sim-1)
                    #     num_sim = num_sim * 1000
                    #     print("time num of simulations: ", num_sim)
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
                        print ("player_lvl change {i.name} :", i.lvl)      
                if (over_twenty != True):
                    print("in lvl minus one")
                    self.new_hpAndDmpr()
                    print("creature cr: ", self.creature.challnge_rtg)
                    self.final_solution(num_sim+1, lvl_chg+1)
                    # if (avg_players_lvl < self.creature.challnge_rtg):
                    #     print("players avg lvl is less than creature cr: ", avg_players_lvl)
                    #     print("creature cr: ", self.creature.challnge_rtg)
                    #     num_sim = num_sim * 1000
                    #     print("num of simulations: ", num_sim)
                    # else:
                    #     num_sim = num_sim * 1000
                    #     print("time num of simulations: ", num_sim)
                    #     self.final_solution(num_sim+1)
                else:
                    print("player lvl was over twenty")
                
    def reset_players_hp(self, creature_hp, hp_val, hp_val2, hp_val3, hp_val4):
        is_val_negative = False
        self.creature.hit_pts = creature_hp
        if(self.creature.hit_pts <= 0):
            #print("creature is value is negative: ", self.creature.hit_pts)
            is_val_negative = True
            return is_val_negative
        else:
            self.creature.is_defeated = False
            #print("creature is_defeated", self.creature.is_defeated)
            #print("creature hp: ", self.creature.hit_pts)    
            if (len(self.players) == 4):
                self.players[0].hp_change(hp_val)
                self.players[1].hp_change(hp_val2)
                self.players[2].hp_change(hp_val3)
                self.players[3].hp_change(hp_val4)
                #print("current hp 0: ",self.players[0].hp)
                #print("current hp 1: ",self.players[1].hp)
                #print("current hp 2: ",self.players[2].hp)
                #print("current hp 3: ",self.players[3].hp)
                for i in self.players:
                    if(i.hp <= 0):    
                        #print("negative players")
                        is_val_negative = True
                        break
                    else:
                        i.is_defeated = False
                        #print("current value of is_defeated: ",i.is_defeated)
                        #print("current lvl plyer", i.lvl)
            elif (len(self.players) == 3):
                self.players[0].hp_change(hp_val)
                self.players[1].hp_change(hp_val2)
                self.players[2].hp_change(hp_val3)
                #print("current hp 0: ",self.players[0].hp)
                #print("current hp 1: ",self.players[1].hp)
                #print("current hp 2: ",self.players[2].hp)
                for i in self.players:
                    if(i.hp <= 0):  
                        #print("negative players")  
                        is_val_negative = True
                        break
                    else:
                        i.is_defeated = False
                        #print("current value of is_defeated: ",i.is_defeated)
                        #print("current lvl plyer", i.lvl)
            elif (len(self.players) == 2):
                self.players[0].hp_change(hp_val)
                self.players[1].hp_change(hp_val2)
                #print("current p1 hp 0: ",self.players[0].hp)
                #print("current p2 hp 1: ",self.players[1].hp)
                for i in self.players:
                    if(i.hp <= 0):    
                        #print("negative players")
                        is_val_negative = True
                        break
                    else:
                        i.is_defeated = False
                        #print("current value of is_defeated: ",i.is_defeated)
                        #print("current lvl plyer", i.lvl)
            else:
                self.players[0].hp_change(hp_val)
                #print("current hp 0: ",self.players[0].hp)
                for i in self.players:
                    if(i.hp <= 0):
                        #print("negative players")
                        is_val_negative = True
                        break
                    else:
                        i.is_defeated = False
                        #print("current is_defeated: ",i.is_defeated)
                        #print("plyer lvl", i.lvl)
                        #print("plyer hp", i.hp)
                
            return is_val_negative
            
    def new_hpAndDmpr(self):
        #print("in newhpAndDmpr")
        x = np.array(range(1, 21))

        fighterY = ((2.8947368421052633*x)+2.1052631578947327)
        fighterHpY = ((7.947368421052632*x)+2.05263157894737)
        fighterCurve, = plt.plot(x, fighterY)
        fighterHpCurve, = plt.plot(x, fighterHpY)
        fighterXData = fighterCurve.get_xdata()
        fighterYData = fighterCurve.get_ydata()
        fighterHpYdata = fighterHpCurve.get_ydata()

        rangerY = ((1.4736842105263157*x)+5.526315789473685)
        rangerHpY = ((7.947368421052632*x)+2.05263157894737)
        rangerCurve, = plt.plot(x, rangerY)
        rangerHpCurve, = plt.plot(x,rangerHpY)
        rangerXData = rangerCurve.get_xdata()
        rangerYData = rangerCurve.get_ydata()
        rangerHpYData = rangerHpCurve.get_ydata()

        rogueY = ((1.4210526315789473*x)+6.578947368421055)
        rogueHpY = ((6.052631578947368*x)+1.94736842105263)
        rogueCurve, = plt.plot(x, rogueY)
        rogueHpCurve, = plt.plot(x,rogueHpY)
        rogueXData = rogueCurve.get_xdata()
        rogueYData = rogueCurve.get_ydata()
        rogueHpYData = rogueHpCurve.get_ydata()

        wizardY = ((2.3684210526315788*x)+2.631578947368425)
        wizardHpY = ((6.052631578947368*x)+1.94736842105263)
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
            
    def generate_cr_simulation(self,num_sim):
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
            
        while (num_sim != 0):
            fighting = combat.combatSimulation(self.creature, self.players)
            #print("current hp for p1: ",self.players[0].hp)
            num_sim -= 1
            creature_plyer_hp = self.reset_players_hp(creature_hp, hp_val, hp_val2, hp_val3, hp_val4)
            if(creature_plyer_hp == True):
                #print("negative hp values break")
                return -1
            else:
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
        creature_plyer_hp = self.reset_players_hp(creature_hp, hp_val, hp_val2, hp_val3, hp_val4)
        if(creature_plyer_hp == True):
            print("negative hp values break")
            return -1
        else:
            return percentage