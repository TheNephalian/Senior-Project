import math 

# fuction that will get the creature rating when the user inputs the hit points
# range for HP is 1-850

def cal_HP_defensive_CR(HP):
    if (HP > 0 and HP <= 6):
        HP_def_CR = 0
        return HP_def_CR
    
    elif (HP <= 35):
        HP_def_CR = 1/8
        return HP_def_CR
    
    elif (HP <= 49):
        HP_def_CR = 1/4
        return HP_def_CR
    
    elif (HP <= 70):
        HP_def_CR = 1/2
        return HP_def_CR
    
    elif (HP <= 85):
        HP_def_CR = 1
        return HP_def_CR
    
    elif (HP <= 100):
        HP_def_CR = 2
        return HP_def_CR
    
    elif (HP <= 115):
        HP_def_CR = 3
        return HP_def_CR 
    
    elif (HP <= 130):
        HP_def_CR = 4
        return HP_def_CR
    
    elif (HP <= 145):
        HP_def_CR = 5
        return HP_def_CR
    
    elif (HP <= 160):
        HP_def_CR = 6
        return HP_def_CR
    
    elif (HP <= 175):
        HP_def_CR = 7
        return HP_def_CR
    
    elif (HP <= 190):
        HP_def_CR = 8
        return HP_def_CR
    
    elif (HP <= 205):
        HP_def_CR = 9
        return HP_def_CR
    
    elif (HP <= 220):
        HP_def_CR = 10
        return HP_def_CR
    
    elif (HP <= 235):
        HP_def_CR = 11
        return HP_def_CR
    
    elif (HP <= 250):
        HP_def_CR = 12
        return HP_def_CR
    
    elif (HP <= 265):
        HP_def_CR = 13
        return HP_def_CR
    
    elif (HP <= 280):
        HP_def_CR = 14
        return HP_def_CR
    
    elif (HP <= 295):
        HP_def_CR = 15
        return HP_def_CR
    
    elif (HP <= 310):
        HP_def_CR = 16
        return HP_def_CR
    
    elif (HP <= 325):
        HP_def_CR = 17
        return HP_def_CR
    
    elif (HP <= 340):
        HP_def_CR = 18
        return HP_def_CR
    
    elif (HP <= 355):
        HP_def_CR = 19
        return HP_def_CR
    
    elif (HP <= 400):
        HP_def_CR = 20
        return HP_def_CR
    
    elif (HP <= 445):
        HP_def_CR = 21
        return HP_def_CR
    
    elif (HP <= 490):
        HP_def_CR = 22
        return HP_def_CR
    
    elif (HP <= 535):
        HP_def_CR = 23
        return HP_def_CR
    
    elif (HP <= 580):
        HP_def_CR = 24
        return HP_def_CR
    
    elif (HP <= 625):
        HP_def_CR = 25
        return HP_def_CR
    
    elif (HP <= 670):
        HP_def_CR = 26
        return HP_def_CR
    
    elif (HP <= 715):
        HP_def_CR = 27
        return HP_def_CR
    
    elif (HP <= 760):
        HP_def_CR = 28
        return HP_def_CR
    
    elif (HP <= 805):
        HP_def_CR = 29
        return HP_def_CR
    
    elif (HP <= 850):
        HP_def_CR = 30
        return HP_def_CR
    
    else: 
        print("Error in defensiveCR.py cal_HP_defensive_CR")
        
# function that will calculate in what armor class creature is depending on their HP
# AC range 13-19

def calculate_stuff(HP):
    if(HP <= 115):
        AC = 13
        return AC
    
    elif(HP <= 130):
        AC = 14
        return AC
    
    elif(HP <= 175):
        AC = 15
        return AC
    
    elif(HP <= 205):
        AC = 16
        return AC
    
    elif(HP <= 250):
        AC = 17
        return AC
    
    elif(HP <= 310):
        AC = 18
        return AC
    
    elif(HP <= 850):
        AC = 19
        return AC
    
    else:
        print("Error in defensiveCR.py calculate_stuff")
        
# Gets the offcial CR by adjusting the CR given from the HP according by what the user input AC to be
#AC is the true AC from each CR depedning on the HP in_AC is the input value that user input into armor class

def get_CR_rating(AC, HP_def_CR, in_AC,saveProfVal):
    in_AC = in_AC - saveProfVal
    if(in_AC >= 19):
        if(AC == 13):
            if(HP_def_CR == 0):
                if(saveProfVal == 0):
                    return 1/2
                elif(saveProfVal == 2):
                    return 1
                else:
                    return 2
            elif(HP_def_CR == 1/8):
                if(saveProfVal == 0):
                    return 1
                elif(saveProfVal == 2):
                    return 2
                else:
                    return 3
            elif(HP_def_CR == 1/4):
                if(saveProfVal == 0):
                    return 2
                elif(saveProfVal == 2):
                    return 3
                else:
                    return 4
            elif(HP_def_CR == 1/2):
                if(saveProfVal == 0):
                    return 3
                elif(saveProfVal == 2):
                    return 4
                else:
                    return 5
            else:
                if(saveProfVal == 0):
                    return HP_def_CR + 3
                elif(saveProfVal == 2):
                    return HP_def_CR + 4
                else:
                    return HP_def_CR + 5
        elif(AC == 14):
            if(saveProfVal == 0):
                return HP_def_CR + 2
            elif(saveProfVal == 2):
                return HP_def_CR + 3
            else:
                return HP_def_CR + 4
        elif(AC == 15):
            if(saveProfVal == 0):
                return HP_def_CR + 2
            elif(saveProfVal == 2):
                return HP_def_CR + 3
            else:
                return HP_def_CR + 4
        elif(AC == 16):
            if(saveProfVal == 0):
                return HP_def_CR + 1
            elif(saveProfVal == 2):
                return HP_def_CR + 2
            else:
                return HP_def_CR + 3
        elif(AC == 17):
            if(saveProfVal == 0):
                return HP_def_CR + 1
            elif(saveProfVal == 2):
                return HP_def_CR + 2
            else:
                return HP_def_CR + 3
        elif(AC == 18):
            if(saveProfVal == 0):
                return HP_def_CR
            elif(saveProfVal == 2):
                return HP_def_CR + 1
            else:
                return HP_def_CR + 2
        elif(AC == 19):
            if(saveProfVal == 0):
                return HP_def_CR
            elif(saveProfVal == 2):
                return HP_def_CR + 1
            else:
                return HP_def_CR + 2
        
    elif(in_AC == 18):
        #
        if(AC == 13):
            if(HP_def_CR == 0):
                if(saveProfVal == 0):
                    return 1/4
                elif(saveProfVal == 2):
                    return 1/2
                else:
                    return 1
            elif(HP_def_CR == 1/8):
                if(saveProfVal == 0):
                    return 1/2
                elif(saveProfVal == 2):
                    return 1
                else:
                    return 2
            elif(HP_def_CR == 1/4):
                if(saveProfVal == 0):
                    return 1
                elif(saveProfVal == 2):
                    return 2
                else:
                    return 3
            elif(HP_def_CR == 1/2):
                if(saveProfVal == 0):
                    return 2
                elif(saveProfVal == 2):
                    return 3
                else:
                    return 4
            else:
                if(saveProfVal == 0):
                    return HP_def_CR + 2
                elif(saveProfVal == 2):
                    return HP_def_CR + 3
                else:
                    return HP_def_CR + 4
        elif(AC == 14):
            if(saveProfVal == 0):
                return HP_def_CR + 2
            elif(saveProfVal == 2):
                return HP_def_CR + 3
            else:
                return HP_def_CR + 4
        elif(AC == 15):
            if(saveProfVal == 0):
                return HP_def_CR + 1
            elif(saveProfVal == 2):
                return HP_def_CR + 2
            else:
                return HP_def_CR + 3
        elif(AC == 16):
            if(saveProfVal == 0):
                return HP_def_CR + 1
            elif(saveProfVal == 2):
                return HP_def_CR + 2
            else:
                return HP_def_CR + 3
        elif(AC == 17):
            if(saveProfVal == 0):
                return HP_def_CR
            elif(saveProfVal == 2):
                return HP_def_CR + 1
            else:
                return HP_def_CR + 2
        elif(AC == 18):
            if(saveProfVal == 0):
                return HP_def_CR
            elif(saveProfVal == 2):
                return HP_def_CR + 1
            else:
                return HP_def_CR + 2
        elif(AC == 19):
            if(saveProfVal == 0):
                return HP_def_CR
            elif(saveProfVal == 2):
                return HP_def_CR + 1
            else:
                return HP_def_CR + 2
        
    elif(in_AC == 17):
        #
        if(AC == 13):
            if(HP_def_CR == 0):
                if(saveProfVal == 0):
                    return 1/4
                elif(saveProfVal == 2):
                    return 1/2
                else:
                    return 1
            elif(HP_def_CR == 1/8):
                if(saveProfVal == 0):
                    return 1/2
                elif(saveProfVal == 2):
                    return 1
                else:
                    return 2
            elif(HP_def_CR == 1/4):
                if(saveProfVal == 0):
                    return 1
                elif(saveProfVal == 2):
                    return 2
                else:
                    return 3
            elif(HP_def_CR == 1/2):
                if(saveProfVal == 0):
                    return 2
                elif(saveProfVal == 2):
                    return 3
                else:
                    return 4
            else:
                if(saveProfVal == 0):
                    return HP_def_CR + 2
                elif(saveProfVal == 2):
                    return HP_def_CR + 3
                else:
                    return HP_def_CR + 4
        elif(AC == 14):
            if(saveProfVal == 0):
                return HP_def_CR + 1
            elif(saveProfVal == 2):
                return HP_def_CR + 2
            else:
                return HP_def_CR + 3
        elif(AC == 15):
            if(saveProfVal == 0):
                return HP_def_CR + 1
            elif(saveProfVal == 2):
                return HP_def_CR + 2
            else:
                return HP_def_CR + 3
        elif(AC == 16):
            if(saveProfVal == 0):
                return HP_def_CR
            elif(saveProfVal == 2):
                return HP_def_CR + 1
            else:
                return HP_def_CR + 2
        elif(AC == 17):
            if(saveProfVal == 0):
                return HP_def_CR
            elif(saveProfVal == 2):
                return HP_def_CR + 1
            else:
                return HP_def_CR + 2
        elif(AC == 18):
            if(saveProfVal == 0):
                return HP_def_CR
            elif(saveProfVal == 2):
                return HP_def_CR + 1
            else:
                return HP_def_CR + 2
        elif(AC == 19):
            if(saveProfVal == 0):
                return HP_def_CR - 1
            elif(saveProfVal == 2):
                return HP_def_CR
            else:
                return HP_def_CR + 1
        
    elif(in_AC == 16):
        #
        if(AC == 13):
            if(HP_def_CR == 0):
                if(saveProfVal == 0):
                    return 1/8
                elif(saveProfVal == 2):
                    return 1/4
                else:
                    return 1/2
            elif(HP_def_CR == 1/8):
                if(saveProfVal == 0):
                    return 1/4
                elif(saveProfVal == 2):
                    return 1/2
                else:
                    return 1
            elif(HP_def_CR == 1/4):
                if(saveProfVal == 0):
                    return 1/2
                elif(saveProfVal == 2):
                    return 1
                else:
                    return 2
            elif(HP_def_CR == 1/2):
                if(saveProfVal == 0):
                    return 1
                elif(saveProfVal == 2):
                    return 2
                else:
                    return 3
            else:
                if(saveProfVal == 0):
                    return HP_def_CR + 1
                elif(saveProfVal == 2):
                    return HP_def_CR + 2
                else:
                    return HP_def_CR + 3
        elif(AC == 14):
            if(saveProfVal == 0):
                return HP_def_CR + 1
            elif(saveProfVal == 2):
                return HP_def_CR + 2
            else:
                return HP_def_CR + 3
        elif(AC == 15):
            if(saveProfVal == 0):
                return HP_def_CR
            elif(saveProfVal == 2):
                return HP_def_CR + 1
            else:
                return HP_def_CR + 2
        elif(AC == 16):
            if(saveProfVal == 0):
                return HP_def_CR
            elif(saveProfVal == 2):
                return HP_def_CR + 1
            else:
                return HP_def_CR + 2
        elif(AC == 17):
            if(saveProfVal == 0):
                return HP_def_CR
            elif(saveProfVal == 2):
                return HP_def_CR + 1
            else:
                return HP_def_CR + 2
        elif(AC == 18):
            if(saveProfVal == 0):
                return HP_def_CR - 1
            elif(saveProfVal == 2):
                return HP_def_CR
            else:
                return HP_def_CR + 1
        elif(AC == 19):
            if(saveProfVal == 0):
                return HP_def_CR - 1
            elif(saveProfVal == 2):
                return HP_def_CR
            else:
                return HP_def_CR + 1
        
    elif(in_AC == 15):
        #
        if(AC == 13):
            if(HP_def_CR == 0):
                if(saveProfVal == 0):
                    return 1/8
                elif(saveProfVal == 2):
                    return 1/4
                else:
                    return 1/2
            elif(HP_def_CR == 1/8):
                if(saveProfVal == 0):
                    return 1/4
                elif(saveProfVal == 2):
                    return 1/2
                else:
                    return 1
            elif(HP_def_CR == 1/4):
                if(saveProfVal == 0):
                    return 1/2
                elif(saveProfVal == 2):
                    return 1
                else:
                    return 2
            elif(HP_def_CR == 1/2):
                if(saveProfVal == 0):
                    return 1
                elif(saveProfVal == 2):
                    return 2
                else:
                    return 3
            else:
                if(saveProfVal == 0):
                    return HP_def_CR + 1
                elif(saveProfVal == 2):
                    return HP_def_CR + 2
                else:
                    return HP_def_CR + 3
        elif(AC == 14):
            if(saveProfVal == 0):
                return HP_def_CR
            elif(saveProfVal == 2):
                return HP_def_CR + 1
            else:
                return HP_def_CR + 2
        elif(AC == 15):
            if(saveProfVal == 0):
                return HP_def_CR
            elif(saveProfVal == 2):
                return HP_def_CR + 1
            else:
                return HP_def_CR + 2
        elif(AC == 16):
            if(saveProfVal == 0):
                return HP_def_CR
            elif(saveProfVal == 2):
                return HP_def_CR + 1
            else:
                return HP_def_CR + 2
        elif(AC == 17):
            if(saveProfVal == 0):
                return HP_def_CR - 1
            elif(saveProfVal == 2):
                return HP_def_CR
            else:
                return HP_def_CR + 1
        elif(AC == 18):
            if(saveProfVal == 0):
                return HP_def_CR - 1
            elif(saveProfVal == 2):
                return HP_def_CR
            else:
                return HP_def_CR + 1 
        elif(AC == 19):
            if(saveProfVal == 0):
                return HP_def_CR - 2 
            elif(saveProfVal == 2):
                return HP_def_CR - 1
            else:
                return HP_def_CR
        
    elif(in_AC == 14):
        #
        if(AC == 13):
            if(HP_def_CR == 0):
                if(saveProfVal == 0):
                    return HP_def_CR
                elif(saveProfVal == 2):
                    return 1/8
                else:
                    return 1/4
            elif(HP_def_CR == 1/8):
                if(saveProfVal == 0):
                    return HP_def_CR
                elif(saveProfVal == 2):
                    return 1/4
                else:
                    return 1/2
            elif(HP_def_CR == 1/4):
                if(saveProfVal == 0):
                    return HP_def_CR
                elif(saveProfVal == 2):
                    return 1/2
                else:
                    return 1
            elif(HP_def_CR == 1/2):
                if(saveProfVal == 0):
                    return HP_def_CR
                elif(saveProfVal == 2):
                    return 1
                else:
                    return 2
            else:
                if(saveProfVal == 0):
                    return HP_def_CR
                elif(saveProfVal == 2):
                    return HP_def_CR + 1
                else:
                    return HP_def_CR + 2
        elif(AC == 14):
            if(saveProfVal == 0):
                return HP_def_CR
            elif(saveProfVal == 2):
                return HP_def_CR + 1
            else:
                return HP_def_CR + 2
        elif(AC == 15):
            if(saveProfVal == 0):
                return HP_def_CR
            elif(saveProfVal == 2):
                return HP_def_CR + 1
            else:
                return HP_def_CR + 2
        elif(AC == 16):
            if(saveProfVal == 0):
                return HP_def_CR - 1
            elif(saveProfVal == 2):
                return HP_def_CR
            else:
                return HP_def_CR + 1
        elif(AC == 17):
            if(saveProfVal == 0):
                return HP_def_CR - 1
            elif(saveProfVal == 2):
                return HP_def_CR
            else:
                return HP_def_CR + 1
        elif(AC == 18):
            if(saveProfVal == 0):
                return HP_def_CR - 2 
            elif(saveProfVal == 2):
                return HP_def_CR - 1
            else:
                return HP_def_CR
        elif(AC == 19):
            if(saveProfVal == 0):
                return HP_def_CR - 2 
            elif(saveProfVal == 2):
                return HP_def_CR - 1
            else:
                return HP_def_CR
        
    elif(in_AC <= 13):
        #
        if(AC == 13):
            if(HP_def_CR == 0):
                if(saveProfVal == 0):
                    return HP_def_CR
                elif(saveProfVal == 2):
                    return 1/8
                else:
                    return 1/4
            elif(HP_def_CR == 1/8):
                if(saveProfVal == 0):
                    return HP_def_CR
                elif(saveProfVal == 2):
                    return 1/4
                else:
                    return 1/2
            elif(HP_def_CR == 1/4):
                if(saveProfVal == 0):
                    return HP_def_CR
                elif(saveProfVal == 2):
                    return 1/2
                else:
                    return 1
            elif(HP_def_CR == 1/2):
                if(saveProfVal == 0):
                    return HP_def_CR
                elif(saveProfVal == 2):
                    return 1
                else:
                    return 2
            else:
                if(saveProfVal == 0):
                    return HP_def_CR
                elif(saveProfVal == 2):
                    return HP_def_CR + 1
                else:
                    return HP_def_CR + 2
        elif(AC == 14):
            if(saveProfVal == 0):
                return HP_def_CR
            elif(saveProfVal == 2):
                return HP_def_CR + 1
            else:
                return HP_def_CR + 2
        elif(AC == 15):
            if(saveProfVal == 0):
                return HP_def_CR - 1
            elif(saveProfVal == 2):
                return HP_def_CR
            else:
                return HP_def_CR + 1
        elif(AC == 16):
            if(saveProfVal == 0):
                return HP_def_CR - 1
            elif(saveProfVal == 2):
                return HP_def_CR
            else:
                return HP_def_CR + 1
        elif(AC == 17):
            if(saveProfVal == 0):
                return HP_def_CR - 2 
            elif(saveProfVal == 2):
                return HP_def_CR - 1
            else:
                return HP_def_CR
        elif(AC == 18):
            if(saveProfVal == 0):
                return HP_def_CR - 2 
            elif(saveProfVal == 2):
                return HP_def_CR - 1
            else:
                return HP_def_CR
        elif(AC == 19):
            if(saveProfVal == 0):
                return HP_def_CR - 3
            elif(saveProfVal == 2):
                return HP_def_CR - 2
            else:
                return HP_def_CR - 1
    else:
        print("Error in defensiveCR.py get_CR_rating")

def cal_init_def_CR(hp, ac,saveProfVal):
    if(hp <= 0):
        init_def_CR = 0
        return init_def_CR
    else:
        if(hp > 850):
            hp = 850
        init_def_CR = cal_HP_defensive_CR(hp)
        corr_AC = calculate_stuff(hp)
        
        init_def_CR = get_CR_rating(corr_AC, init_def_CR, ac,saveProfVal)
        if(init_def_CR < 1):
            return init_def_CR
        elif(init_def_CR > 30):
            init_def_CR = 30
            return init_def_CR
        else:
            return int(init_def_CR)

def get_Average_of_Deff_and_Off(deffCR, OffCR):
    averg = (deffCR + OffCR)/2
    return int(averg)
