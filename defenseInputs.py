from operator import truediv
from re import X
from defensiveCR import *
from creature import *
import math

'''
Vulnerabilities - if checked, the creature's effective hit points is halved

user input hit point value /2 -> defCRfun(hp) -> hpCR
user input ac value -> defCRfun(ac) -> acCR

hpCR, acCR -> defCRfun(hp, ac) -> defCR

Resistances - if yes, the creature's hit points are effectively multiplied by 1.5

user input hit point value * 1.5 -> defCRfun(hp) -> hpCR
user input ac value -> defCRfun(ac) -> acCR

hpCR, acCR -> defCRfun(hp, ac) -> defCR

Immunities - if yes, the creature's hit points are effectively doubled

user input hit point value * 2 -> defCRfun(hp) -> hpCR

Size - Die - hp/die:
Tiny - d4 - 2.5 hp
Small - d6 - 3.5
Medium - d8 - 4.5
Large - d10 - 5.5
Huge - d12 - 6.5
Gargantuan - d20 - 10.5


Constitution Attribute Range - Hp bonus/die:


0-1 - -5
2-3 - -4
4-5 - -3
6-7 - -2
8-9 - -1
10-11 - +0
12-13 - +1
14-15 - +2
16-17 - +3
18-19 - +4
20-21 - +5
22... +6
24... +7
26... +8
28... +9
30+ - +10

Example:
Large, d10
10d10
From stats, 15 Constitution

Hp = 10 * 5.5 + 10 * 2 = 75

Medium, d8
4d8
From stats, 7 Constitution

Hp = 4 * 4.5 + 4 * (-2) = 10


'''
'''this function will get the input for the die'''
def die(input_of_die):
    if (input_of_die < 0):
        print("error")
    elif(input_of_die <= 189):
        return input_of_die
    else:
        print("error")
        
def resistancesORimmunity(ri,hp):
    if (ri == "Resistances"):
        hp = hp * 1.5
        return math.floor(hp)
    elif(ri == "Immunities"):
        hp = hp * 2
        return math.floor(hp)
    else:
        return math.floor(hp)

'''this function will get constitution attribute range'''
def Constitution(constit):
    if (constit <= 1 ):
        con = -5
        return con
    elif (constit <= 3):
        con = -4
        return con
    elif (constit <= 5):
        con = -3
        return con
    elif (constit <= 7):
        con = -2
        return con
    elif (constit <= 9):
        con = -1
        return con
    elif (constit <= 11):
        con = 0
        return con
    elif (constit <= 13):
        con = 1
        return con
    elif (constit <= 15):
        con = 2
        return con
    elif (constit <= 17):
        con = 3
        return con
    elif (constit <= 19):
        con = 4
        return con
    elif (constit <= 21):
        con = 5
        return con
    elif (constit <= 23):
        con = 6
        return con
    elif (constit <= 25):
        con = 7
        return con
    elif (constit <= 27):
        con = 8
        return con
    elif (constit <= 29):
        con = 9
        return con
    elif (constit >= 30):
        con = 10
        return con

'''this function will get the get the die and the hp added based on what size the user inputs '''
def Size(inputSize):
    if(inputSize == "Tiny"):
        c1 = myCreature("d4", 2.5, "Tiny")
        return c1
    elif(inputSize == "Small"):
        c1 = myCreature("d6", 3.5, "Small")
        return c1
    elif(inputSize == "Medium"):
        c1 = myCreature("d8", 4.5, "Medium")
        return c1
    elif(inputSize == "Large"):
        c1 = myCreature("d10", 5.5, "Large")
        return c1
    elif(inputSize == "Huge"):
        c1 = myCreature("d12", 6.5, "Huge")
        return c1
    elif(inputSize == "Gargantuan"):
        c1 = myCreature("d20", 10.5, "Gargantuan")
        return c1
'''
Vulnerabilities
If a creature has any, it's hp are 'effectively' halved
'''

def doesIthaveVulnerabilities(vul, hp):
    if vul == True:
        hp = hp / 2
        return math.floor(hp)
    else:
        return hp

'''
Save Proficiencies
Up to 6 total

AC is 'effectively' increased by 2 if the creature has 3 or 4,
	'effectively' increased by 4 if 5 or 6
'''

def saveProficienciesCal(cal):
    if cal == "0-2":
        increase = 0
        return increase
    elif cal == "3-4":
        increase = 2
        return increase
    else:
        increase = 4
        return increase
    
    
# Example:
# Large, d10
# 10d10
# From stats, 15 Constitution

# Hp = 10 * 5.5 + 10 * 2 = 75

#print(die(10))
#print(Constitution(15)) # 2
#y = Size("Large")
#print(y.hp) # 5

'''this fun gets the total HP based on the dice, constitution, size, and vulnerabilities '''
def this_fun_cal_totalHP(dice, constitution, size, vul, ri):
    if (dice == 0 and constitution == 0):
        HP = 0
        return HP 
    else :
        #dice = die(dice)
        constitution = Constitution(constitution)
        size = Size(size)
        HP =  dice * size.hp + dice * constitution
        HP = resistancesORimmunity(ri,HP) 
        HP = doesIthaveVulnerabilities(vul, HP)
        if(HP < 1):
            return 1
        else:
            return math.floor(HP)

def this_fun_adds_AC(prof, currentAC):
    profadded = saveProficienciesCal(prof)
    AC = currentAC + profadded
    return AC
    
    
#print(cal_init_def_CR(this_fun_cal_totalHP(1,1,"Tiny",False,False),this_fun_adds_AC(5,3))) # 0
print(round(this_fun_cal_totalHP(0,1,"Tiny",False,False))) #-2