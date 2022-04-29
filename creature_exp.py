import math 

def cr_to_exp(CR):
    if(CR == 0):
        EXP = 10
        return EXP
    elif(CR == 1):
        EXP = 200
        return EXP
    elif(CR == 2):
        EXP = 450
        return EXP
    elif(CR == 3):
        EXP = 700
        return EXP
    elif(CR == 4):
        EXP = 1100
        return EXP
    elif(CR == 5):
        EXP = 1800
        return EXP
    elif(CR == 6):
        EXP = 2300
        return EXP
    elif(CR == 7):
        EXP = 2900
        return EXP
    elif(CR == 8):
        EXP = 3900
        return EXP
    elif(CR == 9):
        EXP = 5000
        return EXP
    elif(CR == 10):
        EXP = 5900
        return EXP
    elif(CR == 11):
        EXP = 7200
        return EXP
    elif(CR == 12):
        EXP = 8400
        return EXP
    elif(CR == 13):
        EXP = 10000
        return EXP
    elif(CR == 14):
        EXP = 11500
        return EXP
    elif(CR == 15):
        EXP = 13000
        return EXP
    elif(CR == 16):
        EXP = 15000
        return EXP
    elif(CR == 17):
        EXP = 18000
        return EXP
    elif(CR == 18):
        EXP = 20000
        return EXP
    elif(CR == 19):
        EXP = 22000
        return EXP
    elif(CR == 20):
        EXP = 25000
        return EXP
    elif(CR == 21):
        EXP = 33000
        return EXP
    elif(CR == 22):
        EXP = 41000
        return EXP
    elif(CR == 23):
        EXP = 50000
        return EXP
    elif(CR == 24):
        EXP = 62000
        return EXP
    elif(CR == 25):
        EXP = 75000
        return EXP
    elif(CR == 26):
        EXP = 90000
        return EXP
    elif(CR == 27):
        EXP = 105000
        return EXP
    elif(CR == 28):
        EXP = 120000
        return EXP
    elif(CR == 29):
        EXP = 135000
        return EXP
    elif(CR == 30):
        EXP = 155000
        return EXP
    
    
def player_exp(lvl):
    if(lvl == 1):
        EXP_arry = [25,50,75,100]
        return EXP_arry
    elif(lvl == 2):
        EXP_arry = [50,100,150,200]
        return EXP_arry
    elif(lvl == 3):
        EXP_arry = [75,150,225,400]
        return EXP_arry
    elif(lvl == 4):
        EXP_arry = [125,250,375,500]
        return EXP_arry
    elif(lvl == 5):
        EXP_arry = [250,500,750,1100]
        return EXP_arry
    elif(lvl == 6):
        EXP_arry = [300,600,900,1400]
        return EXP_arry
    elif(lvl == 7):
        EXP_arry = [350,750,1100,1700]
        return EXP_arry
    elif(lvl == 8):
        EXP_arry = [450,900,1400,2100]
        return EXP_arry
    elif(lvl == 9):
        EXP_arry = [550,1100,1600,2400]
        return EXP_arry
    elif(lvl == 10):
        EXP_arry = [600,1200,1900,2800]
        return EXP_arry
    elif(lvl == 11):
        EXP_arry = [800,1600,2400,3600]
        return EXP_arry
    elif(lvl == 12):
        EXP_arry = [1000,2000,3000,4500]
        return EXP_arry
    elif(lvl == 13):
        EXP_arry = [1100,2200,3400,5100]
        return EXP_arry
    elif(lvl == 14):
        EXP_arry = [1250,2500,3800,5700]
        return EXP_arry
    elif(lvl == 15):
        EXP_arry = [1400,2800,4300,6400]
        return EXP_arry
    elif(lvl == 16):
        EXP_arry = [1600,3200,4800,7200]
        return EXP_arry
    elif(lvl == 17):
        EXP_arry = [2000,3900,5900,8800]
        return EXP_arry
    elif(lvl == 18):
        EXP_arry = [2100,4200,6300,9500]
        return EXP_arry
    elif(lvl == 19):
        EXP_arry = [2400,4900,7300,10900]
        return EXP_arry
    elif(lvl == 20):
        EXP_arry = [2800,5700,8500,12700]
        return EXP_arry