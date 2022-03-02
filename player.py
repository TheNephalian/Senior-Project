import random


class myPlayer:
    def __init__(Player):
        Player.lvl = 1
        Player.hp = 0
        Player.curr_hp = Player.hp
        Player.ac = 0
        Player.prof_bns = 0
        Player.is_defeated = False
        
        Player.strength = 10
        Player.dexterity = 10
        Player.constitution = 10
        Player.intelligence = 10
        Player.wisdom = 10
        Player.charisma = 10
        
        Player.dex_bns = 0
        Player.atk_bns = 0
        Player.dmg_per_rnd = 0
        
    def roll_init(Player):
        init = random.randint(1,20) + Player.dex_bns
        return init
    
    def attack_roll(Player):
        atk_roll = random.randint(1,20) + Player.atk_bns
        return atk_roll
    
    def take_dmg(Player, dmg):
        Player.curr_hp = Player.hp - dmg
        Player.hp = Player.curr_hp
        
        if(Player.hp <= 0):
            Player.is_defeated = True
    
    def lvl_change(Player, lvls):
        
        Player.lvl = lvls
        