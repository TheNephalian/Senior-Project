from offensiveCR import cal_Offensive_CR

'''Testing of functions'''
print(cal_Offensive_CR(2)); '''Should return 1/4'''
print(cal_Offensive_CR(21)); '''Should return 3'''
print(cal_Offensive_CR(210)); '''Should return 24'''
print(cal_Offensive_CR(410)); '''Should print error message 'Damage too high'. Also, returns None as no value is actually returned by cal_Offensive_CR'''