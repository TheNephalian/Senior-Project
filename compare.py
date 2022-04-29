from logging import Handler
from dummyCreature import creature
from dummyCreatures import dummyCyclops, dummyMinotaur, dummyBugBear, dummyOrc, dummyZombie, dummyGiantRat
from dummyPlayers import dummyFighter, dummyRanger, dummyRogue, dummyWizard
from player import *
from creature_exp import *

class compareCRandEC():
    def __init__(self):
        self.creature = dummyBugBear.BugBear()
        
        self.players = []
        p1 = dummyFighter.Fighter()
        p1.lvl_change(1)
        
        p2 = dummyRanger.Ranger()
        p2.lvl_change(2)
        
        p3 = dummyRogue.Rogue()
        p3.lvl_change(3)

        p4 = dummyWizard.Wizard()
        p4.lvl_change(4)

        self.players.append(p1)
        self.players.append(p2)
        self.players.append(p3)
        self.players.append(p4)
        
    
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
        Meduim = 0
        Hard  = 0 
        Deadly = 0
        
        print(list_players_exp)
        for i in list_players_exp:
            for j, exp_num in enumerate(i):
                if (j == 0):
                    Easy += exp_num
                elif (j == 1):
                    Meduim += exp_num
                elif (j == 2):
                    Hard += exp_num
                else:
                    Deadly += exp_num
        
        if (Easy >= creature_exp):
            print("easy exp", Easy)
            return Easy
        elif (Meduim >= creature_exp):
            print("meduim exp", Meduim)
            return Meduim
        elif (Hard >= creature_exp):
            print("hard exp", Hard)
            return Hard
        elif (Deadly >= creature_exp):
            print("deadly exp", Deadly)
            return Deadly
          
                
        
        
        